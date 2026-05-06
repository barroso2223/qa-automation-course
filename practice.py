from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def test_login_page(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    assert "The Internet" in driver.title


def test_login_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("secure"))
    assert "secure" in driver.current_url
