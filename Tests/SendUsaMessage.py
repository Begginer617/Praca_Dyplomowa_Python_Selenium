from Pages.HomePage import HomePage
from Utils.data_geenrator import DataGenerator


# tworze metode testowa ktora importuje biblioteke driver
def test_send_contact_message(driver):
    # Tworzysz obiekt strony.
    home = HomePage(driver)
    data = DataGenerator()
    # Wywołujesz metodę z POM, która otwiera stronę.
    home.open()
    home.fill_contact_form_with_fake_data(data)
    home.submit_contact_form()