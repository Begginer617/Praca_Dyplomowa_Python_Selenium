import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class HomePage(BasePage):

    # NIE używamy URL tutaj — open() robi to w dwóch krokach
    URL = "https://automationintesting.online/"

    # sekcja booking
    Booking_Section = (By.ID, "booking")

    # Twoje działające lokatory
    Calendar_Check_In_Field = (
        By.XPATH,
        '//*[@id="booking"]/div/div/div/form/div/div[1]/div[1]/div/input'
    )
    Calendar_Check_Out_Field = (
        By.XPATH,
        '//*[@id="booking"]/div/div/div/form/div/div[1]/div[2]/div/input'
    )

    def open(self):
        # KROK 1 — wymuszenie starej wersji (bez hash)
        self.driver.get("https://automationintesting.online/?force-old")
        time.sleep(1)

        # KROK 2 — wejście na widok z bookingiem (hash NIE zniknie)
        self.driver.get("https://automationintesting.online/#/booking")
        time.sleep(1)

        return self

    def is_loaded(self):
        # czekamy aż booking pojawi się w DOM
        self.wait.until(EC.presence_of_element_located(self.Booking_Section))
        return self

    def open_check_in_calendar(self):
        print("Próba otwarcia kalendarza CHECK-IN")
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