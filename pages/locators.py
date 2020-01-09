from selenium.webdriver.common.by import By


class MainPageLocators():
    BODY = (By.XPATH, "//body[1]")
    LOGO = (By.XPATH, "//img[@class='img-container']")
    HIDE_LEFT_MENU_BUTTON = (By.XPATH, "//zps-platform-button[@zpsiconclass='editor-format-indent-decrease']")  # скрыть левое меню
    SWITCH_LOCALIZATION_BUTTON = (By.XPATH, "//zps-platform-button[@elementclass='app-icon'][2]")  # Сменить локализацию
    SWITCH_THEME_BUTTON = (By.XPATH, "//zps-platform-button[@elementclass='app-icon'][1]")  # Сменить тему
    USER_ICON_BUTTON = (By.XPATH, "//zps-platform-button[@zpsiconclass='account-circle']")  # Иконка юзера

    LEFT_MENU = (By.TAG_NAME, "zps-applications-panel")  # левое меню
    Z_QA_LINK = (By.XPATH, "//h4[text()='Quality Assurance']")  # ЛИМС


class ZQAPageLocators():
    pass
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

