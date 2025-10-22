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