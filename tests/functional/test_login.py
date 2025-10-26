from selenium.webdriver.common.by import By
import time
from .conftest import take_screenshot

def login(driver, base_url, username, password):
    driver.get(base_url)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

def test_login_sucesso(driver, base_url):
    login(driver, base_url, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    take_screenshot(driver, "login_sucesso.png")

def test_login_bloqueado(driver, base_url):
    login(driver, base_url, "locked_out_user", "secret_sauce")
    erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "locked out" in erro.lower()
    take_screenshot(driver, "login_bloqueado.png")

def test_login_invalido(driver, base_url):
    login(driver, base_url, "usuario_fake", "senha_errada")
    erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "do not match" in erro.lower()
    take_screenshot(driver, "login_invalido.png")
