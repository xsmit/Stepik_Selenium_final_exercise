import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose site language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nstart browser for test..")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Общий вариант запуска
    browser = webdriver.Chrome(options=options)

    # Запуск для моего компа
    # chrome_service_executable_path = "C:\\Users\\yury.ageev\\AppData\\Local\\Programs\\ChromeDriver\\chromedriver.exe"
    # chrome_service = Service(executable_path=chrome_service_executable_path)
    # browser = webdriver.Chrome(options=options, service=chrome_service)

    yield browser
    print("\nquit browser..")
    browser.quit()
