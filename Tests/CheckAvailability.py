from Pages.HomePage import HomePage


def test_check_availability_single_room(driver):
    home = HomePage(driver)
    home.open()
    home.is_loaded()
    home.select_today_and_random_checkout()
    # ewentualnie:
    # home.click_check_availability()