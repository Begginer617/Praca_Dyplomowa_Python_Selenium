from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class BookingPage(BasePage):

    # Nagłówek modala rezerwacji.
    # Modal pojawia się po kliknięciu "Book this room".
    HEADER = (By.XPATH, '//div[contains(@class, "modal")]//h2')

    # Pole "First name" w formularzu modala.
    FIRST_NAME = (By.XPATH, '//input[@id="firstname"]')

    # Przycisk "Submit" w modalu.
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Submit")]')

    # Sprawdza, czy modal rezerwacji jest widoczny.
    def is_loaded(self):
        return self.is_visible(self.HEADER)

    # Wpisuje imię do pola "First name".
    def fill_first_name(self, name):
        self.type(self.FIRST_NAME, name)

    # Kliknięcie przycisku "Submit".
    def submit(self):
        self.click(self.SUBMIT_BUTTON)