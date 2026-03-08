#„Weź klasę HomePage z pliku HomePage.py”.
from Pages.HomePage import HomePage


    # tworze metode testowa ktora importuje biblioteke driver
def test_send_contact_message(driver):
    # Tworzysz obiekt strony.
    home = HomePage(driver)
    # Wywołujesz metodę z POM, która otwiera stronę.
    home.open()
    home.fill_contact_form()




