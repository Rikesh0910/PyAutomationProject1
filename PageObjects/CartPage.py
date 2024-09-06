from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    cart = (By.XPATH, "//a[text()='Cart']")
    checkout = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    total_amt = (By.XPATH, "//label[@id='totalm']")
    form_name = (By.XPATH, "//input[@id='name']")
    form_country = (By.XPATH, "//input[@id='country']")
    form_credit_card = (By.XPATH, "//input[@id='card']")
    purchase = (By.XPATH, "//button[text()='Purchase']")
    confirmation = (By.XPATH, "//p[@class='lead text-muted ']")
    close = (By.CSS_SELECTOR, "button[class='confirm btn btn-lg btn-primary']")

    def get_cart(self):
        return self.driver.find_element(*CartPage.cart)

    def checkout_cart(self):
        return self.driver.find_element(*CartPage.checkout)

    def check_total_amt(self):
        return self.driver.find_element(*CartPage.total_amt)

    def fill_form(self, name, country, credit_card_no):
        self.driver.find_element(*CartPage.form_name).send_keys(name)
        self.driver.find_element(*CartPage.form_country).send_keys(country)
        self.driver.find_element(*CartPage.form_credit_card).send_keys(credit_card_no)
        return self.driver

    def purchase_product(self):
        return self.driver.find_element(*CartPage.purchase)

    def product_confirmation(self):
        return self.driver.find_element(*CartPage.confirmation)

    def complete_purchase(self):
        return self.driver.find_element(*CartPage.close)