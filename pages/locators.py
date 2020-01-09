from selenium.webdriver.common.by import By


class BasePageLocators():
    # скрыть левое меню
    # Сменить локализацию
    # Сменить тему
    USER_ICON = (By.XPATH, "//zps-platform-button[@zpsiconclass='account-circle']")  # Иконка юзера

    LEFT_MENU = (By.TAG_NAME, "zps-applications-panel")  # левое меню
    Z_QA_LINK = (By.XPATH, "//h4[text()='Quality Assurance']")  # ЛИМС

    # Задания
    # НСИ
    # Шаблоны обоазцов

    # Ввод результатов анализов
    # Журналы образцов

    # Метдики и методы
    # График аналитического контроля


class LoginPageLocators():
    LOGIN_TITLE = (By.TAG_NAME, "h3")  # Заголовок
    LOGIN_USERNAME_INPUT = (By.ID, "username")  # Имя
    LOGIN_PASSWORD_INPUT = (By.ID, "password")  # Пароль
    LOGIN_BUTTON = (By.ID, "kc-login")  # Кнопка

