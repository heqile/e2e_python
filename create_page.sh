#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
cd page
class_name=$1
file_name="$class_name.py"
if [ -e $file_name ]; then
  echo "File $file_name already exists!"
else
  echo >> $file_name
fi

echo "from commun.base_page import BasePage" >> $file_name
echo "from commun.base_page_element import BasePageElement" >> $file_name
echo "" >> $file_name
echo "" >> $file_name
echo "class $class_name(BasePage):" >> $file_name
echo "    page_name = \"$class_name\"" >> $file_name
echo "    page_element = None" >> $file_name
echo "" >> $file_name
echo "    def initialize_page_elements(self):" >> $file_name
echo "        # locator_key is the same value in .json files" >> $file_name
echo "        self.contact_button_1 = BasePageElement(self.driver, self._element_locator(locator_key=\"page_element\"))" >> $file_name
echo "" >> $file_name
echo "    def action(self):" >> $file_name
echo "        # do something" >> $file_name
echo "        # self.action_chain.move_to_element(self.contact_button_1.get_element()).perform()" >> $file_name
echo "        pass"  >> $file_name
