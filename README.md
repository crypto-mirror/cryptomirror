# Cryptomirror

## About

Cryptomirror downloads files defined in `releases.py` and verifies them by hash value and GPG signature.

This is useful for easily downloading many popular encryption related softwares at once for offline
use or storage in case they later become unavailable.

[https://cryptomirror.com](https://cryptomirror.com)

### Content owners

Software releases in `releases.py` are unmodified and retain the original license available on each
publisher's website. All rights are retained by their respective owners.

For removal or updates, submit an issue or pull request. 

### Updates

To update a version or include additional software for mirroring, submit an issue or pull request
with changes to values in `releases.py`.

## Usage

## Standalone Usage

Standalone usage downloads all files defined in `releases.py`. Files are stored in `CRYPTOMIRROR_DATA_DIR`.

If you want to use Cryptomirror in verify only mode, set `CRYPTOMIRROR_MODE_VERIFY` to `True`. This
will download the files in `releases.py` and verify their integrity so you can determine if the
software is being tampered in transit on your connection. In verify only mode, downloaded sofware is
deleted after verification is passed.

Set the log directory with `CRYPTOMIRROR_LOG_FILE`, defaults to stdout.

Environment variable defaults:
```
export CRYPTOMIRROR_LOG_FILE=None
export CRYPTOMIRROR_MODE_VERIFY=False
export CRYPTOMIRROR_DATA_DIR=/tmp/cryptomirror
```

### Run

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python cryptomirror/cryptomirror.py
```

## Site Build Usage

Run `build-site.sh` and deploy to web server.

Theme from: https://github.com/pietromenna/jekyll-cayman-theme
