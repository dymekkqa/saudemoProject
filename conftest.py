import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    def configure_browser(browser_type):
        if browser_type == "chrome":
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            return webdriver.Chrome(options=options)
        elif browser_type == "firefox":
            options = FirefoxOptions()
            # options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            return webdriver.Firefox(options=options)
        else:
            raise ValueError("Unsupported browser type. Use 'chrome' or 'firefox'.")

    browser_type = "chrome"  #  select browser
    driver = configure_browser(browser_type)
    request.cls.driver = driver
    yield driver
    driver.quit()
