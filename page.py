from element import BasePageElement
from locators import MainPageLocators
from locators import LogInPageLocators
from locators import PaymentPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def select_one_way(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "flight-search-type-option-one-way")))
        #element = self.driver.find_element(*MainPageLocators.GO_ONE_WAY)
        element.click()

    def select_from(self, from_where):
        element = self.driver.find_element(*MainPageLocators.GO_FROM)
        element.clear()
        element.send_keys(from_where)
        element.send_keys(Keys.TAB)

    def select_to(self, to_where):
        element = self.driver.find_element(*MainPageLocators.GO_TO)
        element.clear()
        element.send_keys(to_where)
        element.send_keys(Keys.TAB)

    def select_date(self, date):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(*MainPageLocators.GO_DATE)
        element.click()
        element.send_keys(date)
        element.send_keys(Keys.TAB)

    def select_persons(self):
        element_select = self.driver.find_element(*MainPageLocators.GO_PERSONS)
        element_select.click()
        self.driver.implicitly_wait(10)
        element_persons = self.driver.find_element(*MainPageLocators.GO_NUM_PERSONS)
        element_persons.click()
        element_persons.click()
        element_childs = self.driver.find_element(*MainPageLocators.GO_NUM_CHILDRENS)
        element_childs.click()
        element_select.send_keys(Keys.TAB)

    def submit(self):
        element = self.driver.find_element(*MainPageLocators.GO_SUBMIT)
        element.click()


class SelectFlyPage(BasePage):

    def select_fly_price(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.flight-header__min-price.hide-mobile > flights-table-price > div.flights-table-price > div.core-btn-primary > span.flights-table-price__price")))
        #element = self.driver.find_element(*MainPageLocators.GO_FLY_PRICE)
        element.click()

    def select_fly_type(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "continue")))
        element.click()

class RecommendedPage(BasePage):

    def select_continue(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "continue")))
        element.click()

class CheckOutPage(BasePage):
    def select_checkout(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.button - next > button.core - btn - primary.core - btn - medium")))
        element.click()

    def select_no_sits(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "utton.core-btn-ghost.seat-prompt-popup-footer-btn")))
        element.click()

class LogIn(BasePage):

    def select_login(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.core-btn-secondary")))
        element.click()

    def insert_mail(self, mail):
        element = self.driver.find_element(*LogInPageLocators.GO_MAIL)
        element.send_keys(mail)

    def insert_pass(self, login_pass):
        element = self.driver.find_element(*LogInPageLocators.GO_PASS)
        element.send_keys(login_pass)

    def login(self):
        element = self.driver.find_element(*LogInPageLocators.GO_SUBMIT_LOGIN)
        element.click()

class PaymentPage(BasePage):

    def insert_account(self, num):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "cardNumber3821")))
        element.send_keys(num)

    def pay_now(self):
        element = self.driver.find_element(*PaymentPageLocators.CSS_SELECTOR)
        element.click()
