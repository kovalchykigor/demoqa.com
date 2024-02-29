import base64
import os.path
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import requests
from generators.generator import generated_person
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesLocators, ButtonsLocators, LinksLocators, BrokenImageLocators, UploadAndDownloadLocators, DynamicProperties

import random


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = generated_person()

        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace('\n', ' ')
        permanent_address = person_info.permanent_address.replace('\n', ' ')

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 17

        for iteration in range(count):
            item = random.choice(item_list)
            self.go_to_element(item)
            item.click()


class CheckRadioButton(BasePage):
    locators = RadioButtonPageLocators

    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIO,
            'impressive': self.locators.IMPRESSIVE_RADIO,
            'no': self.locators.NO_RADIO
        }
        self.element_is_visible(choices[choice]).click()

    def get_output(self):
        return self.element_is_visible(self.locators.SUCCESS_TEXT).text


class WebTables(BasePage):
    locators = WebTablesLocators

    def get_column_headers_list(self):
        temp_list = self.elements_are_visible(self.locators.COLUMN_HEADERS)
        headers_list = []
        for element in temp_list:
            headers_list.append(element.text)
        return headers_list

    def get_table_rows(self):
        elements = self.elements_are_visible(self.locators.TABLE_ROWS)
        row = elements[3].text.split('\n')
        return row

    def add_new_person(self):
        person_info = generated_person()
        first_name = person_info.firstname
        last_name = person_info.lastname
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department

        self.element_is_visible(self.locators.ADD_BUTTON).click()

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SALARY).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)

        self.element_is_visible(self.locators.SUBMIT).click()
        return [first_name, last_name, email, age, salary, department]

    def search_person(self, person_info):
        self.element_is_visible(self.locators.SEARCH_FIELD).clear()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(person_info)

        search_result = self.elements_are_visible(self.locators.TABLE_ROWS)
        result = search_result[0].text.split("\n")

        return result

    def update_person_age(self, age):
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE).clear
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def return_table_rows(self):
        elements = self.elements_are_visible(self.locators.TABLE_ROWS)
        return elements[0].text

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        element = self.element_is_present(self.locators.NO_ROWS_FOUND).text
        return element

    def select_up_to_some_rows(self):
        rows = [5, 10, 20, 25, 50, 100]
        data = []
        for x in rows:
            count_row_button = self.element_is_present(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()

            option_locator = (By.CSS_SELECTOR, f"option[value='{x}']")
            self.element_is_visible(option_locator).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)

        return len(list_rows)

class Buttons(BasePage):
    locators = ButtonsLocators

    def button_click(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_ME_BTN))
        self.action_context_click(self.element_is_visible(self.locators.RIGHT_CLICK_ME_BTN))
        self.element_is_visible(self.locators.CLICK_ME_BTN).click()
        click_messages_list = self.elements_are_visible(self.locators.CLICK_MESSAGES)
        text_list = [element.text for element in click_messages_list]
        return text_list

class Links(BasePage):
    locators = LinksLocators

    def check_new_tab_simple_link(self):
        link = self.element_is_visible(self.locators.HOME_NEW_TAB_LINK)
        link_href = link.get_property('href')
        response = requests.get(link_href)
        status_code = response.status_code
        if status_code == 200:
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            new_tab_url = self.driver.current_url
            return link_href, new_tab_url
        else:
            return link_href, status_code

    def check_api_call_links(self,):
        api_calls = self.locators.API_CALLS
        api_links = self.locators.API_LINKS

        actual_status_code_list = []
        expected_status_code_list = []

        for index, link_locator in enumerate(api_links):
            api_call = api_calls[index]
            url = f"https://demoqa.com/{api_call}"

            self.element_is_visible(link_locator).click()
            actual_status_code = requests.get(url).status_code
            expected_status_code = self.element_is_visible(self.locators.EXPECTED_STATUS_CODE).text

            actual_status_code_list.append(str(actual_status_code))
            expected_status_code_list.append(expected_status_code)

        return actual_status_code_list, expected_status_code_list


class BrokenLinksImages(BasePage):
    locators = BrokenImageLocators

    def broken_image(self):
        element = self.element_is_visible(self.locators.BROKEN_IMAGE)
        image_width = self.check_image_loaded(element)
        return image_width

    def valid_image(self):
        element = self.element_is_visible(self.locators.VALID_IMAGE)
        image_width = self.check_image_loaded(element)
        return image_width

    def check_link_status_code(self, url):
        return requests.get(url).status_code


    def broken_link(self):
        self.element_is_visible(self.locators.BROKEN_LINK).click()
        status_code = requests.get("https://the-internet.herokuapp.com/status_codes/500").status_code
        return status_code


class UploadAndDownload(BasePage):
    locators = UploadAndDownloadLocators

    def upload(self):
        self.element_is_visible(self.locators.CHOOSE_FILE_BUTTON).send_keys(rf"E:\1.txt")
        uploaded_path = self.element_is_visible(self.locators.UPLOADED_FILE_PATH).text
        return uploaded_path

    def download_base64(self):
        output_filename = f"E:/{random.randint(0,100)}from_base64_to.jpeg"
        try:
            base64_string = self.element_is_visible(self.locators.DOWNLOAD_BUTTON).get_attribute('href')
            image_data = base64.b64decode(base64_string.split(",")[1])

            with open(output_filename, 'wb') as f:
                f.write(image_data)

            if os.path.exists(output_filename):
                return True
            else:
                return False
        except Exception as e:
            print(e)


class DynamicProperties(BasePage):

    locators = DynamicProperties

    def wait_before_enable_button(self):
        try:
            self.element_is_visible(self.locators.ENABLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        else:
            return True

    def check_color_change(self):
        color_change = self.element_is_clickable(self.locators.COLOR_CHANGE_BUTTON)
        color_before = color_change.value_of_css_property('color')
        time.sleep(5)
        color_after = color_change.value_of_css_property('color')
        return color_before, color_after

    def visible_after_5_seconds(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True







