import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def driver():
    ## Patrón AAA (Preparación - Arrange )
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    yield driver

    ## TEARDOWN
    driver.quit()