#!/usr/bin/env bash

set -euf -o pipefail

./source-bundle.sh

export PS1=""
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
DIR=$(pwd)
export CRYPTOMIRROR_DATA_DIR=${DIR}/site/assets/files
python cryptomirror/cryptomirror.py

cd site
jekyll build
