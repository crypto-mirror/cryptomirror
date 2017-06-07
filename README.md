# Cryptomirror

## About

Cryptomirror downloads files defined in `releases.py` and verifies them by hash value and GPG signature.

### Content owners

Software releases in `releases.py` are unmodified and retain the original license available on each publisher's website. All rights are retained by their respective owners. 

For removal or updates, submit an issue or pull request. 

### Updates

To update a version or include additional software for mirroring, submit a pull request with changes to values in `releases.py`.

## Usage

## Standalone Usage

Set the log directory with `CRYPTOMIRROR_LOG_FILE`, defaults to stdout.

Files are stored in `CRYPTOMIRROR_DATA_DIR`.

If you want to use Cryptomirror in verify only mode, set `CRYPTOMIRROR_MODE_VERIFY` to `True`.

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

## Site

Run `build-site.sh` and deploy to web server.

Theme from: https://github.com/pietromenna/jekyll-cayman-theme
