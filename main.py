import unittest
from selenium import webdriver
import page

class Main(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.ryanair.com/ie/en/")

    def test_select(self):
        main_page = page.MainPage(self.driver)
        main_page.select_one_way()
        main_page.select_from("dub")
        main_page.select_to("sxf")
        main_page.select_date("11/12/2017")
        main_page.select_persons()
        main_page.submit()
        self.driver.implicitly_wait(30)
        fly_page = page.SelectFlyPage(self.driver)
        fly_page.select_fly_price()
        fly_page.select_fly_type()
        self.driver.implicity_wait(30)
        recommended_page = page.RecommendedPage(self.driver)
        recommended_page.select_continue()
        self.driver.implicity_wait(30)
        checkout_page = page.CheckOutPage(self.driver)
        checkout_page.select_checkout()
        self.driver.implicity_wait(10)
        checkout_page.select_no_sits()
        self.driver.implicity_wait(30)
        login_page = page.LogIn(self.driver)
        login_page.select_login
        login_page.insert_mail("maria_marin_84@hotmail.com")
        login_page.insert_pass("aoBGhn9Z")
        login_page.login()
        self.driver.implicity_wait(30)
        payment_page = page.PaymentPage(self.driver)
        payment_page.insert_account("5555 5555 5555 5557")
        payment_page.pay_now()
        element = self.driver.find_element_by_css_selector("//div[@id='checkout']/div/form/div/div[2]/div[2]/div[4]/div/div[2]/div/div/div/payment-method-retrieved-cards/payment-method-card/div/ul/li/span")
        assert element.text == 'Card number is too short'

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()