from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    drive = webdriver.Chrome(options=options)
    yield drive
    drive.quit()


def test_dropdown(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    select.select_by_visible_text("Option 2")
    assert select.first_selected_option.text == "Option 2"
