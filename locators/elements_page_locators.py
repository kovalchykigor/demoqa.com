
from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "[id='submit']")

    # populated fields
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, ".rct-title")
    CHECKED_ITEM = (By.CSS_SELECTOR, ".rct-icon.rct-icon-check")


class RadioButtonPageLocators:
    YES_RADIO = (By.CSS_SELECTOR, "[for='yesRadio']")
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "[for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "[for='noRadio']")

    SUCCESS_TEXT = (By.CSS_SELECTOR, ".text-success")


class WebTablesLocators:

    COLUMN_HEADERS = (By.CSS_SELECTOR, ".rt-resizable-header-content")
    TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tbody")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#searchBox")
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "[d='M864 256H736v-80c0-35.3-28.7-64-64-64H352c-35.3 0-64 28.7-64 64v80H160c-17.7 0-32 14.3-32 32v32c0 4.4 3.6 8 8 8h60.4l24.7 523c1.6 34.1 29.8 61 63.9 61h454c34.2 0 62.3-26.8 63.9-61l24.7-523H888c4.4 0 8-3.6 8-8v-32c0-17.7-14.3-32-32-32zm-200 0H360v-72h304v72z']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, ".rt-noData")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, ".rt-tr-group")

    #registration form
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    AGE = (By.CSS_SELECTOR, "#age")
    SALARY = (By.CSS_SELECTOR, "#salary")
    DEPARTMENT = (By.CSS_SELECTOR, "#department")
    SUBMIT = (By.CSS_SELECTOR, "#submit")


class ButtonsLocators:
    DOUBLE_CLICK_ME_BTN = (By.CSS_SELECTOR, "#doubleClickBtn")
    RIGHT_CLICK_ME_BTN = (By.CSS_SELECTOR, "#rightClickBtn")
    CLICK_ME_BTN = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "#doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "#rightClickMessage")

    CLICK_MESSAGES = (By.CSS_SELECTOR, "button.btn.btn-primary")


class LinksLocators:
    HOME_NEW_TAB_LINK = (By.CSS_SELECTOR, "#simpleLink")
    CREATED_REQUEST_LINK = (By.CSS_SELECTOR, "#created")
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "#bad-request")
    #Links
    API_LINKS = ((By.CSS_SELECTOR, "#created"), (By.CSS_SELECTOR, "#no-content"), (By.CSS_SELECTOR, "#moved"), (By.CSS_SELECTOR, "#bad-request"), (By.CSS_SELECTOR, "#unauthorized"), (By.CSS_SELECTOR, "#forbidden"), (By.CSS_SELECTOR, "#invalid-url"))
    EXPECTED_STATUS_CODE = (By.CSS_SELECTOR, "#linkResponse b:first-child")
    #api_calls
    API_CALLS = ["created", "no-content", "moved", "bad-request", "unauthorized", "forbidden", "invalid-url"]


class BrokenImageLocators:
    VALID_IMAGE = (By.CSS_SELECTOR, "div[id='Ad.Plus-970x250-1'] + div img[src='/images/Toolsqa.jpg']")
    BROKEN_IMAGE = (By.CSS_SELECTOR, "[src='/images/Toolsqa_1.jpg']")
    VALID_LINK = (By.CSS_SELECTOR, "div[id='Ad.Plus-970x250-1'] + div a[href='http://demoqa.com']")
    BROKEN_LINK = (By.CSS_SELECTOR, "div[id='Ad.Plus-970x250-1'] + div a[href='http://the-internet.herokuapp.com/status_codes/500']")


class UploadAndDownloadLocators:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "#downloadButton")
    CHOOSE_FILE_BUTTON = (By.CSS_SELECTOR, "#uploadFile")
    UPLOADED_FILE_PATH = (By.CSS_SELECTOR, "#uploadedFilePath")

class DynamicProperties:
    ENABLE_AFTER_BUTTON = (By.CSS_SELECTOR, "#enableAfter")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "#colorChange")
    VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, "#visibleAfter")





