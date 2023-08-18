import pytest
from appium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    capabilities = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'RZCR301GKCM',
        "appPackage": 'com.android.chrome',
        "appActivity": 'com.google.android.apps.chrome.Main'
        # "appPackage": 'com.sec.android.app.sbrowser',
        # "appActivity": 'com.sec.android.app.sbrowser.SBrowserMainActivity'
    }

    driver = webdriver.Remote("http://localhost:4723", capabilities)

    request.cls.driver = driver
    yield
    driver.quit()
