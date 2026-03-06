from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class HomePage(BasePage):

    # URL strony głównej — dzięki temu test nie musi znać adresu.
    URL = "https://automationintesting.online/"

    # Lokator przycisku "Book this room".
    # To jest przykład — jeśli na stronie jest inny przycisk, zmienimy go później.
    BOOK_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-primary")

    # Metoda otwierająca stronę główną.
    # Test wywoła home_page.open(), a driver wejdzie na URL.
    def open(self):
        self.driver.get(self.URL)

    # Metoda klikająca przycisk "Book this room".
    # Używa metody click() z BasePage, więc nie musisz pisać WebDriverWait.
    def go_to_booking(self):
        self.click(self.BOOK_BUTTON)