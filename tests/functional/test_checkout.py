from selenium.webdriver.common.by import By
from .conftest import take_screenshot

def test_checkout_completo(driver, base_url):
    driver.get(base_url)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Eduarda")
    driver.find_element(By.ID, "last-name").send_keys("Araujo")
    driver.find_element(By.ID, "postal-code").send_keys("90000")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    assert "checkout-complete" in driver.current_url
    take_screenshot(driver, "checkout_completo.png")

def test_checkout_vazio(driver, base_url):
    driver.get(base_url)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    take_screenshot(driver, "checkout_vazio.png")
    assert "cart" in driver.current_url
