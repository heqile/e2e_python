#!/usr/bin/env bash

if [ -z $1 ]; then
    echo "Example: ./create_test.sh test_site"
    exit 0
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
cd test
test_name=$1
file_name="$test_name.py"
if [ -e $file_name ]; then
  echo "File $file_name already exists!"
else
  echo >> $file_name
fi

echo "from page.test_page import TestPage" >> $file_name
echo "" >> $file_name
echo "" >> $file_name
echo "# site_key is the same value in .json files" >> $file_name
echo "site = \"SITE\"" >> $file_name
echo "" >> $file_name
echo "" >> $file_name
echo "def test_login(selenium):" >> $file_name
echo "    login_page = LoginPage(selenium)" >> $file_name
echo "    login_page.get()" >> $file_name
echo "    assert login_page.is_current_page()" >> $file_name

