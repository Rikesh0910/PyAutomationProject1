from selenium.webdriver.common.by import By


class LaptopPage:

    def __init__(self, driver):
        self.driver = driver

    laptop_page = (By.XPATH, "//a[@class='list-group-item'][3]")
    laptop_titles = (By.XPATH, "//a[@class='hrefch']")
    add = (By.CSS_SELECTOR, "a[class='btn btn-success btn-lg']")

    def goTo_LaptopPage(self):
        return self.driver.find_element(*LaptopPage.laptop_page)

    def get_laptop_titles(self):
        return self.driver.find_elements(*LaptopPage.laptop_titles)

    def laptop_add(self):
        return self.driver.find_element(*LaptopPage.add)

