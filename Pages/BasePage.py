from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # Konstruktor – wywoływany przy tworzeniu obiektu strony.
    # Przechowuje driver i tworzy WebDriverWait, aby Selenium nie klikało za szybko.
    def __init__(self, driver):
        self.driver = driver
        # Ustawiamy timeout na 10 sekund – 1 sekunda to za mało i powoduje flaky testy.
        self.wait = WebDriverWait(driver, 10)

    # Metoda do klikania w element.
    # Czeka aż element będzie klikalny (widoczny + aktywny), a dopiero potem klika.
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Metoda do wpisywania tekstu w pole.
    # 1. Czeka aż pole będzie widoczne.
    # 2. Czyści pole (clear), żeby nie mieszać tekstu.
    # 3. Wpisuje podany tekst.
    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    # Metoda do pobierania tekstu z elementu.
    # Czeka aż element będzie widoczny i zwraca jego tekst.
    # Używane np. do asercji w testach.
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    # Metoda sprawdzająca, czy element jest widoczny na stronie.
    # Jeśli Selenium nie znajdzie elementu w czasie oczekiwania → zwróci False.
    # Przydatne do warunków typu: "czy komunikat o błędzie się pojawił?"
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    # Metoda zwracająca element (bez klikania, bez wpisywania).
    # Przydatne, gdy chcesz pobrać atrybut, np. element.get_attribute("value").
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # Metoda do czekania na dowolny warunek Selenium.
    # Umożliwia np. czekanie na zmianę URL, zniknięcie elementu, itp.
    def wait_for(self, condition):
        return self.wait.until(condition)