import datetime
import hashlib
import logging
import os
import shlex
import shutil
import subprocess
import tempfile

import gnupg

import releases
import util


class Release(object):
    """A software release."""
    def __init__(self, **kwargs):
        self.publisher = kwargs.get("publisher")
        self.publisher_keys = kwargs.get("publisher_keys")
        self.name = kwargs.get("name")
        self.version = kwargs.get("version")
        self.url = kwargs.get("url")
        self.gpg_signature = kwargs.get("gpg_signature")
        self.gpg_signature_url = kwargs.get("gpg_signature_url")
        self.sha1 = kwargs.get("sha1")
        self.sha256 = kwargs.get("sha256")
        self.sha512 = kwargs.get("sha512")


class Download(object):
    """Metadata for a downloaded copy of Software.

    Source is the URL of the Download.
    """
    def __init__(self, **kwargs):
        self.source = kwargs.get("source")
        self.gpg_signature_file = kwargs.get("gpg_signature_file")
        self.time = kwargs.get("time")
        self.validated = kwargs.get("validated")
        self.filepath = kwargs.get("filepath")

    def validate(self, release):
        """Validate GPG signature or hashes.
        Fails at the first failed verification.
        """
        dl_sha1 = util.file_hash(self.filepath, hashlib.sha1())
        dl_sha256 = util.file_hash(self.filepath, hashlib.sha256())
        dl_sha512 = util.file_hash(self.filepath, hashlib.sha512())

        if not util.check_hash("SHA1", dl_sha1, release.sha1):
            self.validated = False
            return
        if not util.check_hash("SHA256", dl_sha256, release.sha256):
            self.validated = False
            return
        if not util.check_hash("SHA512", dl_sha512, release.sha512):
            self.validated = False
            return

        # TODO configure homedir
        gpg = gnupg.GPG(homedir="/tmp/cryptomirror-gpg")
        for k in release.publisher_keys:
            logging.info("Fetching GPG key %s", k)
            gpg.recv_keys(k, keyserver='hkp://pgp.mit.edu')

        # Use subprocess until verify_file is fixed
        if self.gpg_signature_file:
            logging.info("Checking downloaded GPG signature")
            cmd = "gpg --verify {}".format(self.gpg_signature_file)
            proc = subprocess.run(shlex.split(cmd), check=True)
            verified = self.check_verify(proc)
            if not verified:
                self.validated = False
                return

        if release.gpg_signature:
            logging.info("Checking included GPG signature")
            fp = tempfile.NamedTemporaryFile()
            fp.write(release.gpg_signature)
            fp.seek(0)

            cmd = "gpg --verify {} {}".format(fp.name, self.filepath)
            proc = subprocess.run(shlex.split(cmd), check=True)
            verified = self.check_verify(proc)
            fp.close()
            if not verified:
                self.validated = False
                return

        # All validations have passed
        self.validated = True

    def check_verify(self, proc):
        """Verify the output of gpg --verify"""
        logging.debug(proc.stderr)
        if proc.returncode == 0:
            logging.info("Verified GPG signature for %s", self.filepath)
            return True
        else:
            logging.error("Failed to verify GPG signature for %s", self.filepath)
            return False

    def save(self):
        """Save the record to disk."""
        pass


def main():

    LOG_FILE = os.environ.get("CRYPTOMIRROR_LOG_FILE")
    if LOG_FILE:
        logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    DATA_DIR = os.environ.get("CRYPTOMIRROR_DATA_DIR", "/tmp/cryptomirror")
    SAVE_DOWNLOADS = True
    if os.environ.get("CRYPTOMIRROR_MODE_VERIFY", False):
        SAVE_DOWNLOADS = False

    logging.info("Saving files to: %s", DATA_DIR)
    logging.info("Keep downlaoded files: %s", SAVE_DOWNLOADS)
    try:
        os.mkdir(DATA_DIR, 0o755)
    except Exception:
        shutil.rmtree(DATA_DIR)
        os.mkdir(DATA_DIR, 0o755)

    # Fetch release and signature and validate
    for release in releases.RELEASES:
        rel = Release(**release)
        logging.info("Fetching release: %s %s", rel.name, rel.version)
        rel_filepath = util.download_file(rel.url, DATA_DIR)
        data = {"source": rel.url,
                "time": datetime.datetime.now(),
                "filepath": rel_filepath,
                "validated": False,
                }
        if not rel.gpg_signature:  # Sig not saved in releases.py
            if rel.gpg_signature_url:
                logging.info("Fetching GPG signature %s", rel.gpg_signature_url)
                sig_filepath = util.download_file(rel.gpg_signature_url, DATA_DIR)
                if sig_filepath:
                    data['gpg_signature_file'] = sig_filepath
                else:
                    logging.error("Failed to get GPG signature")
            else:
                logging.warning("No GPG signature for release: %s %s", rel.name, rel.version)

        download = Download(**data)
        download.validate(rel)
        if download.validated and not SAVE_DOWNLOADS:
            # Remove file from disk
            os.remove(download.filepath)
            download.filepath = None

        download.save()


if __name__ == "__main__":
    main()
