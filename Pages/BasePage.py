import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # Konstruktor klasy.
    # slow=True → test działa wolniej (do podglądu).
    # delay → ile sekund czekać przed akcją.
    def __init__(self, driver, slow=True, delay=0.1):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.slow = slow
        self.delay = delay

    # Prywatna metoda – pauza tylko gdy slow=True.
    def _pause(self):
        if self.slow:
            time.sleep(self.delay)

    # Klikanie w element.
    # Dodajemy pauzę PRZED kliknięciem, żeby widzieć co zostało wpisane.
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self._pause()  # ← tu spowalniamy kliknięcie submit
        element.click()

    # Wpisywanie tekstu.
    # Jeśli slow=True → wpisuje znak po znaku, jak człowiek.
    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()

        if self.slow:
            # wpisywanie wolne, litera po literze
            for char in text:
                element.send_keys(char)
                time.sleep(self.delay)
        else:
            # normalne szybkie wpisywanie
            element.send_keys(text)

    # Pobieranie tekstu z elementu.
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    # Sprawdza widoczność elementu.
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    # Zwraca element bez akcji.
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # Czeka na dowolny warunek Selenium.
    def wait_for(self, condition):
        return self.wait.until(condition)