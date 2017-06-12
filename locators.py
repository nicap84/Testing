from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_FROM = (By.XPATH, "(//input[@type='text'])[2]")
    GO_TO = (By.XPATH, "(//input[@type='text'])[4]")
    GO_ONE_WAY = (By.ID, "flight-search-type-option-one-way")
    GO_DATE = (By.NAME, "dateInput0")
    GO_CALENDAR = (By.XPATH, "//div[@id='row-dates-pax']/div/div/div/div/div[3]/div/div/div[2]/popup-content/core-datepicker/div/div/ul/li[2]/ul[2]/li[16]/span")
    GO_PERSONS = (By.CSS_SELECTOR, "div.dropdown-handle > core-icon.chevron > div > svg")
    GO_NUM_PERSONS = (By.XPATH, "(//button[@type='button'])[3]")
    GO_NUM_CHILDRENS = (By.XPATH, "(//button[@type='button'])[7]")
    GO_SUBMIT = (By.XPATH, "//div[@id='search-container']/div/div/form/div[4]/button[2]")

class SelectFlyPagePageLocators(object):
    GO_FLY_PRICE = (By.CSS_SELECTOR, "div.flight-header__min-price.hide-mobile > flights-table-price > div.flights-table-price > div.core-btn-primary > span.flights-table-price__price")
    GO_FLY_TYPE = (By.ID, "continue")

class LogInPageLocators(object):
    GO_LOGIN = (By.CSS_SELECTOR, "button.core-btn-secondary")
    GO_MAIL = (By.ID, "email3227")
    GO_PASS = (By.ID, "password3258")
    GO_SUBMIT_LOGIN = (By.CSS_SELECTOR, "button-spinner > button.core-btn-primary")

class PaymentPageLocators(object):
    GO_PAY = (By.CSS_SELECTOR, "button.core - btn - primary.core - btn - medium")