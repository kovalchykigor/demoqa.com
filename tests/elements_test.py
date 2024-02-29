import time

import pytest

from pages.elements import TextBoxPage, CheckBoxPage, CheckRadioButton, WebTables, Buttons, Links, BrokenLinksImages, \
    UploadAndDownload, DynamicProperties
from selenium.webdriver.common.by import By


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            input_full_name, input_email, input_current_address, input_permanent_address = text_box_page.fill_all_fields()
            output_full_name, output_emai, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert input_full_name == output_full_name, "THE 'FULL NAME' DOES NOT MATCH"
            assert input_email == output_emai, "THE 'EMAIL' DOES NOT MATCH"
            assert input_current_address == output_current_address, "THE 'CURRENT ADDRESS' DOES NOT MATCH"
            assert input_permanent_address == output_permanent_address, "THE 'PERMANENT ADDRESS' DOES NOT MATCH"

    class TestCheckBox:

        def test_open_full_list(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = CheckRadioButton(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()

            radio_button_page.click_on_the_radio_button('yes')
            yes = radio_button_page.get_output()
            assert yes == 'Yes', f" 'Yes' != {yes}"

            radio_button_page.click_on_the_radio_button('impressive')
            impressive = radio_button_page.get_output()
            assert impressive == 'Impressive', f" 'Impressive' != {impressive}"

            radio_button_page.click_on_the_radio_button('no')
            no = radio_button_page.get_output()
            assert no == 'No', f" 'No' != {no}"

    class TestWebTables:
        link = "https://demoqa.com/webtables"

        def test_web_table_check_column_headers(self, driver):
            web_table = WebTables(driver, self.link)
            web_table.open()
            headers = web_table.get_column_headers_list()
            assert headers == ['First Name', 'Last Name', 'Age', 'Email', 'Salary', 'Department', 'Action'], \
                "HEADERS DOES'NT EQUAL TO EXPECTED"

        def test_web_table_add_person(self, driver):
            web_table = WebTables(driver, self.link)
            web_table.open()
            new_person_added = web_table.add_new_person()
            new_person_in_table = web_table.get_table_rows()
            assert new_person_added in new_person_in_table

        def test_web_table_search_person(self, driver):
            web_table = WebTables(driver, self.link)
            web_table.open()
            person_info = web_table.add_new_person()
            search_results = web_table.search_person(person_info)
            assert person_info[0] in search_results, "INPUT PERSON NOT EQUAL OUTPUT PERSON"

        def test_web_table_update_person_info(self, driver):
            web_table = WebTables(driver, self.link)
            web_table.open()

            person_info = web_table.add_new_person()  # list
            age = web_table.update_person_age(person_info[4])  # age
            web_table.search_person(person_info[1])  # last name
            time.sleep(3)
            rows = web_table.return_table_rows()

            assert age in rows, f"THERE IS NO '{age}' in '{rows}' !"

        def test_web_table_delete_person(self, driver):
            web_table = WebTables(driver, self.link)
            web_table.open()

            person_info = web_table.add_new_person()
            web_table.search_person(person_info[1])
            web_table.delete_person()
            # time.sleep(2)
            text = web_table.check_deleted()
            print("text= ", text)
            assert text == "No rows found", f"{text} != 'No rows found'"

        def test_web_table_change_count_row(self, driver):
            web_table = WebTables(driver, self.link)
            web_table.open()
            actual_rows = web_table.select_up_to_some_rows()
            expected_rows = [5, 10, 20, 25, 50, 100]

            assert actual_rows == expected_rows, f"'ACTUAL_ROWS' {actual_rows} DOESN'T EQUAL" \
                                                 f" TO 'EXPECTED' {expected_rows}"

    class TestButtons:
        link = "https://demoqa.com/buttons"

        def test_buttons_click(self, driver):
            button_page = Buttons(driver, self.link)
            button_page.open()

            actual_list = button_page.button_click()
            expected_list = ['Double Click Me', 'Right Click Me', 'Click Me']
            assert actual_list == expected_list, f"THE ACTUAL TEXT MESSAGES " \
                                                 f"'{actual_list}' NO EQUAL TO EXPECTED '{expected_list}'"

    class TestLinks:
        link = "https://demoqa.com/links"

        def test_api_call_links(self, driver):
            links = Links(driver, self.link)
            links.open()

            actual_status_code_list, expected_status_code_list = links.check_api_call_links()
            print(actual_status_code_list)
            print(expected_status_code_list)
            assert actual_status_code_list == expected_status_code_list, f"ACTUAL STATUS CODE LIST {actual_status_code_list}" \
                                                                         f" != EXPECTED STATUS CODE LIST {expected_status_code_list}"

    class TestBrokenImage:
        link = "https://demoqa.com/broken"

        @pytest.mark.xfail
        def test_broken_image(self, driver):
            broken_image = BrokenLinksImages(driver, self.link)
            broken_image.open()
            image_width = broken_image.broken_image()
            assert image_width > 0, "IMAGE NOT LOADED"

        def test_valid_image(self, driver):
            test_valid_image = BrokenLinksImages(driver, self.link)
            test_valid_image.open()
            image_width = test_valid_image.valid_image()
            assert image_width > 0, "IMAGE NOT LOADED"

        @pytest.mark.xfail
        def test_links(self, driver):
            test_valid_link = BrokenLinksImages(driver, self.link)
            valid_link = test_valid_link.check_link_status_code("https://demoqa.com")
            broken_link = test_valid_link.check_link_status_code("https://the-internet.herokuapp.com/status_codes/500")
            assert valid_link == 200, "valid_link STATUS CODE IS NOT 200"
            assert broken_link == 200, "broken_link STATUS CODE IS NOT 200"

    class TestUploadAndDownload:
        link = "https://demoqa.com/upload-download"

        def test_upload_file(self, driver):
            upload = UploadAndDownload(driver, self.link)
            upload.open()
            uploaded_path = upload.upload()
            assert uploaded_path is not None, f"uploaded_path IS None"

        def test_download_file(self, driver):
            download = UploadAndDownload(driver, self.link)
            download.open()
            download_true = download.download_base64()
            assert download_true == True

    class TestDynamicProperties:
        link = "https://demoqa.com/dynamic-properties"

        def test_check_enable_button(self, driver):
            will_enable_button = DynamicProperties(driver, self.link)
            will_enable_button.open()
            result = will_enable_button.wait_before_enable_button()
            assert result == True

        def test_check_color_change(self, driver):
            color_change = DynamicProperties(driver, self.link)
            color_change.open()
            result1, result2 = color_change.check_color_change()
            print(result1)
            print(result2)
            assert result1 is not result2

        def test_visible_after_5_seconds(self, driver):
            visible_after = DynamicProperties(driver, self.link)
            visible_after.open()
            result = visible_after.visible_after_5_seconds()
            assert result == True
