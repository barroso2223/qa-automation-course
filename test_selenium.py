from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


@pytest.fixture
def driver():
    drive = webdriver.Chrome()
    yield drive
    drive.quit()


def test_google_title(driver):
    driver.get("https://google.com")
    assert "Google" in driver.title


def test_google_search(driver):
    driver.get("https://google.com")
    search_box = driver.find_element(By.ID, "APjFqb")
    search_box.send_keys("NFL Draft 2026")
    assert search_box.get_attribute("value") == "NFL Draft 2026"


def test_navigate_to_login(driver):
    driver.get("https://the-internet.herokuapp.com")
    link = driver.find_element(By.LINK_TEXT, "Form Authentication")
    link.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url


def test_login(driver):
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
