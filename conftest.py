import json
import os
import pytest
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def config():
    with open("config.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]

@pytest.fixture
def driver(config, request):
    browser = config.get("browser", "chrome")
    headless = config.get("headless", False)

    if browser == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        service = Service(ChromeDriverManager().install())
        _driver = webdriver.Chrome(service=service, options=options)
    else:
        raise Exception("Only Chrome configured for now")

    _driver.implicitly_wait(5)

    yield _driver

    _driver.quit()

# -------- Screenshot on failure --------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Screenshot capture if a test fails.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            # screenshot folder
            screenshots_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            destination = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(destination)
            # if pytest-html is used
            if "html" in item.config.option.__dict__:
                extra = getattr(item.config, "_html", None)
