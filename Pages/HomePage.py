from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    URL = "https://automationintesting.online/"

    Send_Us_A_Message_Name = (By.ID, "name")
    Send_Us_A_Message_Email = (By.ID, "email")
    Send_Us_A_Message_Phone = (By.ID, "phone")
    Send_Us_A_Message_Subject = (By.ID, "subject")
    Send_Us_A_Message_Message = (By.ID, "description")
    Send_Us_A_Message_Submit_Button = (By.XPATH, '//*[@id="contact"]//button')


    HEADER = (By.XPATH, '//div[contains(@class, "modal")]//h2')
    FIRST_NAME = (By.XPATH, '//input[@id="firstname"]')

    def is_loaded(self):
        return self.is_visible(self.HEADER)

    # Wpisuje imię do pola "First name".
    def fill_first_name(self, name):
        self.type(self.FIRST_NAME, name)


    def open(self):
        self.driver.get(self.URL)
        return self

    def fill_contact_form_with_fake_data(self, data):
        # przewiń do formularza
        form = self.wait.until(EC.presence_of_element_located(self.Send_Us_A_Message_Name))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form)

        self.type(self.Send_Us_A_Message_Name, data.name())
        self.type(self.Send_Us_A_Message_Email, data.email())
        self.type(self.Send_Us_A_Message_Phone, data.phone())
        self.type(self.Send_Us_A_Message_Subject, data.subject())
        self.type(self.Send_Us_A_Message_Message, data.message())
        return self

    def submit_contact_form(self):
        # scroll na dół strony
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = self.wait.until(EC.element_to_be_clickable(self.Send_Us_A_Message_Submit_Button))
        # klik przez JS — jedyny stabilny sposób na tej stronie
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def open_in_calendar(self):
        pass
    def next_month(self):
        pass
    def previous_month(self):
        pass
    def pick_day(self):
        pass
    def open_check_in_calendar(self):
        pass
    def open_check_out_calendar(self):
        pass

