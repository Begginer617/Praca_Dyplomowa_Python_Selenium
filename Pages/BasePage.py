import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Klasa bazowa dla wszystkich Page Objectów.
    Zawiera wspólne metody: kliknięcia, wpisywania tekstu, czekania itd.
    """

    def __init__(self, driver, slow=True, delay=0.03):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.slow = slow
        self.delay = delay

    # ---------------------------------------------------------
    # Pomocnicze
    # ---------------------------------------------------------

    def _pause(self):
        """Pauza tylko gdy slow=True."""
        if self.slow:
            time.sleep(self.delay)

    def scroll_into_view(self, locator):
        """
        Przewija stronę do elementu.
        Używamy find_element, bo presence_of_element_located NIE przewija.
        """
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    def find(self, locator):
        """Zwraca element bez wykonywania akcji."""
        return self.wait.until(EC.presence_of_element_located(locator))

    # ---------------------------------------------------------
    # Retry — serce stabilności
    # ---------------------------------------------------------

    def _retry(self, func, attempts=3, wait=0.4):
        """
        Uniwersalny mechanizm retry.
        Próbuje wykonać funkcję kilka razy zanim rzuci wyjątek.
        """
        last_exception = None

        for _ in range(attempts):
            try:
                return func()
            except Exception as e:
                last_exception = e
                time.sleep(wait)

        raise last_exception

    # ---------------------------------------------------------
    # Kliknięcia
    # ---------------------------------------------------------

    def click(self, locator):
        """
        Standardowy klik Selenium + scroll + retry.
        """
        def action():
            self.scroll_into_view(locator)
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self._pause()
            element.click()

        return self._retry(action)

    def js_click(self, locator):
        """
        Kliknięcie przez JavaScript + scroll + retry.
        Najbardziej stabilna metoda.
        """
        def action():
            self.scroll_into_view(locator)
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)

        return self._retry(action)

    # ---------------------------------------------------------
    # Wpisywanie tekstu
    # ---------------------------------------------------------

    def type(self, locator, text):
        """Wpisywanie tekstu — wolne (debug) lub szybkie."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()

        if self.slow:
            for char in text:
                element.send_keys(char)
                time.sleep(self.delay)
        else:
            element.send_keys(text)

    # ---------------------------------------------------------
    # Pobieranie danych
    # ---------------------------------------------------------

    def get_text(self, locator):
        """Pobiera tekst z elementu."""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Sprawdza widoczność elementu."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False