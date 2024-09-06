from selenium.webdriver.common.by import By


class MobilePage:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.XPATH, "//h4[@class='card-title']")
    add_mobile = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    home = (By.XPATH, "(//a[@class='nav-link'])")


    def get_card(self):
        return self.driver.find_elements(*MobilePage.card_title)

    def mobile_add(self):
        return self.driver.find_element(*MobilePage.add_mobile)

    def nav_home(self):
        return self.driver.find_elements(*MobilePage.home)


