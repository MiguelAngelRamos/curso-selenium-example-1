from selenium.webdriver.common.by import By

class LoginPage:
    """
    Responsabilidades:
    - Localizar elementos en la página de login
    - Proveer acciones (ingresar usuario, ingresar contraseña, enviar)
    """
    # Localizadores
    USER_INPUT = (By.ID, 'user')
    PASS_INPUT = (By.ID, 'pass')
    LOGIN_BUTTON = (By.ID, 'login')
    FEEDBACK = (By.ID, 'feedback')

    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def enter_username(self, username: str):
        element_web = self.driver.find_element(*self.USER_INPUT) ## ('id', 'user')
        element_web.clear()
        element_web.send_keys(username)

    def enter_password(self, password: str):
        element_web = self.driver.find_element(*self.PASS_INPUT)
        element_web.clear()
        element_web.send_keys(password)

    def click_login(self):
        btn_login = self.driver.find_element(*self.LOGIN_BUTTON)
        btn_login.click()

    def get_feedback_test(self) -> str:
        return self.driver.find_element(*self.FEEDBACK).text