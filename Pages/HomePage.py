import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class HomePage(BasePage):

    URL = "https://automationintesting.online/"

    # -----------------------------
    #  LOCATORY – CONTACT FORM
    # -----------------------------
    Send_Us_A_Message_Name = (By.ID, "name")
    Send_Us_A_Message_Email = (By.ID, "email")
    Send_Us_A_Message_Phone = (By.ID, "phone")
    Send_Us_A_Message_Subject = (By.ID, "subject")
    Send_Us_A_Message_Message = (By.ID, "description")
    Send_Us_A_Message_Submit_Button = (By.XPATH, '//*[@id="contact"]//button')

    # -----------------------------
    #  LOCATORY – BOOKING
    # -----------------------------
    Booking_Section = (By.ID, "booking")

    Calendar_Check_In_Field = (
        By.XPATH,
        '//*[@id="booking"]/div/div/div/form/div/div[1]/div[1]/div/input'
    )
    Calendar_Check_Out_Field = (
        By.XPATH,
        '//*[@id="booking"]/div/div/div/form/div/div[1]/div[2]/div/input'
    )

    Check_Availability_Button = (
        By.XPATH,
        '//*[@id="booking"]//button[contains(text(),"Check Availability")]'
    )

    # -----------------------------
    #  OPEN PAGE (STABLE VERSION)
    # -----------------------------
    def open(self):
        self.driver.get(self.URL)
        time.sleep(1)
        return self

    # -----------------------------
    #  CONTACT FORM METHODS
    # -----------------------------
    def fill_contact_form_with_fake_data(self, data):
        form = self.wait.until(EC.presence_of_element_located(self.Send_Us_A_Message_Name))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form)

        self.type(self.Send_Us_A_Message_Name, data.name())
        self.type(self.Send_Us_A_Message_Email, data.email())
        self.type(self.Send_Us_A_Message_Phone, data.phone())
        self.type(self.Send_Us_A_Message_Subject, data.subject())
        self.type(self.Send_Us_A_Message_Message, data.message())
        return self

    def submit_contact_form(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = self.wait.until(EC.element_to_be_clickable(self.Send_Us_A_Message_Submit_Button))
        self.driver.execute_script("arguments[0].click();", button)
        return self

    # -----------------------------
    #  BOOKING METHODS
    # -----------------------------
    def wait_for_booking(self):
        for _ in range(10):
            if "Check Availability" in self.driver.page_source:
                return True
            time.sleep(1)
        raise Exception("Booking section never loaded!")

    def open_check_in_calendar(self):
        self.js_click(self.Calendar_Check_In_Field)
        return self

    def open_check_out_calendar(self):
        self.js_click(self.Calendar_Check_Out_Field)
        return self

    def select_today_and_random_checkout(self):
        self.open_check_in_calendar()
        time.sleep(0.5)
        self.open_check_out_calendar()
        return self

    def click_check_availability(self):
        self.click(self.Check_Availability_Button)
        return self

    def is_loaded(self):
        # Czekamy aż sekcja booking pojawi się w DOM
        try:
            self.wait.until(EC.presence_of_element_located(self.Booking_Section))
            return self
        except:
            raise Exception("Booking section did not load!")
