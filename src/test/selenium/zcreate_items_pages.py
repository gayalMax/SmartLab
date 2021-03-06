import monolithic
import time
import unittest
from selenium.webdriver.common.keys import Keys
from random import randrange
from selenium.webdriver.common.action_chains import ActionChains


class TestCreateItemSetsPage(monolithic.MonolithicTest):
    def step_01_go_to_the_create_items_page(self):
        self.login()
        button = self.browser.find_element_by_xpath(
            "//a[.='Create Items']")
        button.click()
        time.sleep(1)
        self.assertCurrentUrl(self.domain+'admin/items/create')

    def step_02_find_all_fields(self):
        self.currentUrl = self.domain+'admin/items/create'
        self.serial_number = str(randrange(1000000))
        self.input_serial_number = self.browser.find_element_by_xpath(
            "//input[@name='serialNumber']")
        self.createbutton = self.browser.find_element_by_xpath(
            "//button[.='Create Item']")
        time.sleep(5)

    def step_03_check_if_in_the_same_page_after_empty_button_click(self):
        self.createbutton.click()
        time.sleep(1)
        self.assertCurrentUrl(self.currentUrl)

    def step_04_fill_only_serial_number_and_submit(self):
        self.input_serial_number.send_keys(self.serial_number)
        self.createbutton.click()
        time.sleep(1)
        self.assertCurrentUrl(self.currentUrl)

    def step_05_fill_only_itemset_and_submit(self):
        self.clearInputField(self.input_serial_number)
        itemset = self.browser.find_element_by_xpath("//div[@role='button']")
        itemset.click()
        keyboard_itemSet = self.browser.find_element_by_xpath(
            "//li[.='monitor']")
        keyboard_itemSet.click()
        self.createbutton.click()
        time.sleep(1)
        self.assertCurrentUrl(self.currentUrl)

    def step_06_fill_only_lab_and_submit(self):
        time.sleep(1)
        lab = self.browser.find_element_by_xpath(
            "//div[@id='mui-component-select-lab']")
        lab.click()
        time.sleep(1)
        lab1 = self.browser.find_element_by_xpath(
            "//li[starts-with(.,'test lab')]")
        lab1.click()
        self.createbutton.click()
        time.sleep(1)
        self.assertCurrentUrl(self.currentUrl)

    def step_07_fill_all_fileds_and_submit(self):
        self.input_serial_number.send_keys(self.serial_number)
        itemset = self.browser.find_element_by_xpath("//div[@role='button']")
        itemset.click()
        keyboard_itemSet = self.browser.find_element_by_xpath(
            "//li[.='monitor']")
        keyboard_itemSet.click()
        lab = self.browser.find_element_by_xpath(
            "//div[@id='mui-component-select-lab']")
        lab.click()
        lab1 = self.browser.find_element_by_xpath(
            "//li[starts-with(.,'test lab')]")
        lab1.click()
        self.createbutton.click()
        time.sleep(1)
        self.assertCurrentUrl(self.currentUrl)

    def step_08_go_to_view_items_page(self):
        button = self.browser.find_element_by_xpath("//a[.='View Items']")
        button.location_once_scrolled_into_view
        time.sleep(1)
        button.click()
        time.sleep(1)
        self.assertCurrentUrl(self.domain+'admin/items/list')

    def step_09_click_refresh_button_and_check_items(self):
        time.sleep(1)
        refresh = self.browser.find_element_by_xpath(
            "//button[@title='Refresh Item List']")
        refresh.location_once_scrolled_into_view
        ActionChains(self.browser).move_to_element(refresh).click()
        time.sleep(2)
        data = self.browser.find_elements_by_tag_name("td")
        self.assertIn(self.serial_number, [each.text.lower() for each in data])

    def step_10_check_search_bar(self):
        self.search_input = self.browser.find_element_by_xpath(
            '//input[@placeholder="Search"]')
        self.search_input.send_keys(self.serial_number)
        time.sleep(2)
        element = self.browser.find_element_by_xpath(
            "//td[.='"+self.serial_number+"']")
        self.assertEqual(element.text.lower(), self.serial_number)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
