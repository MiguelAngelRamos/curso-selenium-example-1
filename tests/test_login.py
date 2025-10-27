import csv
import os
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def read_users_csv(path):
    # (username, password)
    with open(path, newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            yield row['username'], row['password']


@pytest.mark.ui
@pytest.mark.parametrize('username,password', list(read_users_csv(os.path.join(os.path.dirname(__file__), '..', 'usuarios.csv'))))
def test_login_with_csv(driver, username, password):
    
    ## Preparación
    login_url = 'https://login-selenium.netlify.app'
    page = LoginPage(driver)
    page.open(login_url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'user')));

    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    

