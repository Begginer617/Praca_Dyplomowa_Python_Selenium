def test_driver_starts_and_opens_page(driver):
    driver.get("https://automationintesting.online/#booking")
    assert "automationintesting" in driver.current_url

