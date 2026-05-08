from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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


def test_js_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    button.click()
    alert = driver.switch_to.alert
    assert "I am a JS Alert" in alert.text
    alert.accept()


def test_js_confirm(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    button.click()
    alert = driver.switch_to.alert
    assert "I am a JS Confirm" in alert.text
    alert.accept()


def test_js_prompt(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
    button.click()
    alert = driver.switch_to.alert
    alert.send_keys("Hello")
    alert.accept()
    result = driver.find_element(By.ID, "result")
    assert "You entered: Hello" in result.text
