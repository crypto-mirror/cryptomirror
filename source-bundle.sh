#!/usr/bin/env bash

set -euf -o pipefail

TS=$(date +"%Y%m%d")
COMMIT=$(git rev-parse --short HEAD)
NAME="cryptomirror-${TS}-${COMMIT}.tar"

rm -rf cryptomirror/__pycache__
rm -rf cryptomirror/.ropeproject/

if [ -d "site" ]; then
  cd site
  rm -r src
  mkdir src
  rm -r assets/files
  mkdir -p assets/files
  jekyll clean
  cd -
fi

tar cf ${NAME} README.md  cryptomirror  requirements.txt  site source-bundle.sh build-site.sh

shasum ${NAME}
shasum -a 256 ${NAME}

gpg --armor --local-user 3D642F21 --detach-sign ${NAME}

mkdir -p site/src
mv ${NAME} site/src/
mv ${NAME}.asc site/src/

# Update links to new tar
sed "s/cryptomirror.tar/${NAME}/g" site/_includes/page-header.html.tmp > site/_includes/page-header.html
