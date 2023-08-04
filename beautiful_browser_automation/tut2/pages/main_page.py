class MainPage(BasePage):

    def get_header(self):
        return self.find_element(Locators.PageHeader).text

    def select_car_batteries(self):
        self.click_on(Locators.SELECT_MENU)
        self.click_on(Locators.SELECT_MENU°_CAR_BATTERIES)

    def go_to_delivery(self):
        self.click_on(Locators.DeliveryPageLink)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_product_name(self, product_id):
        return self.find_element(Locators.product_link(product_id)).text
