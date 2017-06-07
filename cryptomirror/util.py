import logging
import os
import requests


def file_hash(fname, hash_func):
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def check_hash(hash_type, downloaded, expected):
    if expected:
        logging.info("Downloaded %s: %s expected: %s", hash_type, downloaded, expected)
        if downloaded == expected:
            logging.info("%s matched", hash_type)
            return True
        else:
            logging.error("%s NOT matched", hash_type)
            return False
    else:
        logging.warning("Skipping %s", hash_type)


def get_public_ip():
    r = requests.get('https://api.ipify.org?format=json')
    return r.json().get('ip')


def download_file(url, download_dir):
    filepath = os.path.join(download_dir, os.path.basename(url))
    logging.info("Downloading %s %s", url, filepath)
    resp = requests.get(url, stream=True)
    with open(filepath, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
        return filepath
    return False
