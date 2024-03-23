"""
2024 (c) Education
"""
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest

URL = "https://postcard.qa.studio/"

def test_ground(browser: WebDriver):
    """
    SL-1. Smoke test
    """

    browser.get(URL)

    button = browser.find_element(By.ID, value="send")
    assert button.text == "Отправить", "Unexpected text on button"


#@pytest.mark.xfail(reason="Wait for fix bug")
def test_empty_input_send(browser: WebDriver):
    """
    SL-2. Negative case
    """

    browser.get(URL)

    email_label = browser.find_element(By.CSS_SELECTOR, value="div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == 'requered', "Unexpected attribute class"

    button = browser.find_element(By.ID, value="send")
    button.click()

    email_label = browser.find_element(By.CSS_SELECTOR, value="div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == 'requered error', "Unexpected attribute class"


def test_send_postcard(browser: WebDriver):
    """
    SL-3. Positive case
    """

    browser.get(URL)
    email = browser.find_element(By.ID, value="email")
    email.click()
    email.send_keys("fikajoy487@glaslack.com")

    cards = browser.find_element(By.CSS_SELECTOR, value="#photoContainer > div:nth-child(2) > img")
    cards.click()

    message = browser.find_element(By.CSS_SELECTOR, value= "#textarea")
    message.click()
    message.send_keys("self_education, hell ground")
    time.sleep(1)

    message = browser.find_element(By.CSS_SELECTOR, value = "#send")
    message.click()
    time.sleep(1)

    modal = browser.find_element(By.ID, value="modal")
    assert modal.text == "Открытка успешно отправлена!"