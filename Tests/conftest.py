import time
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    time.sleep(1)   # opóźnienie po teście
    driver.quit()

