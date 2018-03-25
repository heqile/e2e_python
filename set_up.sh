#!/usr/bin/bash

chmod 755 create_page.sh
chmod 755 create_test.sh
virtualenv .venv
source .venv/bin/active
pip insatll --upgrade pip
pip install -r requirements.txt
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=$DIR
