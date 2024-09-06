import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CartPage import CartPage
from PageObjects.LaptopPage import LaptopPage
from PageObjects.MobilePage import MobilePage
from utilities.BaseClass import BaseClass



class Testone(BaseClass):

    def test_one(self):
        log = self.getLogger()
        log.info("the test starts")
        self.driver.execute_script("window.scrollTo(0, 800)")
        mobile = MobilePage(self.driver)
        iter_cards = mobile.get_card()
        for card in iter_cards:
            if card.text == "Iphone 6 32gb":
                card.click()
                break
        mobile.mobile_add().click()
        log.info("new mobile added")
        self.handle_alert()
        log.info("Waiting for home navigation link to be clickable")
        nav_items = mobile.nav_home()
        for item in nav_items:
            log.info(f"Found nav item: '{repr(item.text)}'")
            if "Home" in item.text.strip():
                WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(item))
                item.click()
                log.info("Clicked on Home link")
                break
            else:
                log.warning("Home link not found among navigation items")
        log.info("now moving on to laptop page")
        self.driver.execute_script("window.scrollTo(0, 200)")
        lap = LaptopPage(self.driver)
        log.info("Navigating to the laptop page")
        lap.goTo_LaptopPage().click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='MacBook Pro']"))
        )
        log.info("Fetching laptop titles")
        lap_titles = lap.get_laptop_titles()
        for title in lap_titles:
            self.driver.execute_script("arguments[0].scrollIntoView();", title)
            if 'MacBook Pro' in title.text:
                title.click()
                break
        log.info("now adding a laptop to the cart")
        lap.laptop_add().click()
        self.handle_alert()
        log.info('new laptop added')
        cart = CartPage(self.driver)
        cart.get_cart().click()
        cart.checkout_cart().click()
        time.sleep(5)
        check_amt = cart.check_total_amt().text
        log.info("the total amt is: " + check_amt)
        log.info("filling form to purchase product")
        cart.fill_form("Ricky", "India", "123")
        cart.purchase_product().click()
        final_confirmation = cart.product_confirmation().text
        log.info(final_confirmation)
        cart.complete_purchase().click()
        log.info("the test is over")













