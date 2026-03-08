from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class HomePage(BasePage):
    # LOKALIZATORY

    URL = "https://automationintesting.online/"

    BOOK_NOW = (By.XPATH, '//a[contains(@href, "#booking")]')
    CHECK_AVAILABILITY = (By.XPATH, '//a[contains(@class, "openBooking")]')
    CHECK_IN = (By.XPATH, '//input[@id="checkin"]')
    CHECK_OUT = (By.XPATH, '//input[@id="checkout"]')
    WELCOME_TEXT = (By.XPATH, '//p[contains(@class, "lead")]')
    Footer_text = (By.XPATH, '//*[@id="root-container"]/div/nav/div/a')
    Footer_rooms_Nav_link = (By.XPATH, '//a[contains(@href, "#rooms")]')
    Footer_booking_Nav_link = (By.XPATH, '//a[contains(@href, "#booking")]')
    Footer_Amenities_Nav_link = (By.XPATH, '//*[@id="navbarNav"]/ul/li[3]/a]')
    Footer_Location_Nav_link = (By.XPATH, '//*[@id="navbarNav"]/ul/li[4]/a]')
    Footer_Contact_Nav_link = (By.XPATH, '//*[@id="navbarNav"]/ul/li[5]/a')
    Footer_Admin_Nav_link = (By.XPATH, '//*[@id="navbarNav"]/ul/li[6]/a')
    Send_Us_A_Message_Name =(By.XPATH, '//*[@id="name"]')
    Send_Us_A_Message_Email = (By.XPATH, '//*[@id="email"]')
    Send_Us_A_Message_Phone = (By.XPATH, '//*[@id="phone"]')
    Send_Us_A_Message_Subject = (By.XPATH, '//*[@id="subject"]')
    Send_Us_A_Message_Message = (By.XPATH, '//*[@id="message"]')
    Send_Us_A_Message_Submit_Button = (By.XPATH, '//*[@id="contact"]/div/div/div/div/div/form/div[6]/button')

    # METODY

    def open(self):
        self.driver.get(self.URL)

    def click_check_availability_to_booking(self):
        self.click(self.CHECK_AVAILABILITY)

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        assert element.is_displayed()
        return self.wait.until(EC.visibility_of_element_located(locator)).text