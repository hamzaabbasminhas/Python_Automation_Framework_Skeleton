import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import MainPackage.utilities.customLogger as cl
import os
from MainPackage.utilities.BaseClass import BaseClass


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose between local and import/export")


@pytest.yield_fixture(scope='class')
def setup(request):
    log = cl.customLogger()
    log.info("Remove all old Logs and Reports")
    removeFiles()
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://intake-portal.web.app/")
    driver.implicitly_wait(15)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


def removeFiles():
    filelist = [f for f in
                os.listdir(
                    BaseClass.ROOT_PATH+'/logs')
                if f.endswith(".log")]
    for f in filelist:
        os.remove(
            os.path.join(
                BaseClass.ROOT_PATH+'/logs',
                f))

    filelist = [f for f in
                os.listdir(
                    BaseClass.ROOT_PATH+'/reports')
                if f.endswith(".json")]
    for f in filelist:
        os.remove(
            os.path.join(
                BaseClass.ROOT_PATH+'/reports',
                f))

    filelist = [f for f in
                os.listdir(
                    BaseClass.ROOT_PATH+'/reports')
                if f.endswith(".txt")]
    for f in filelist:
        os.remove(
            os.path.join(
                BaseClass.ROOT_PATH+'/reports',
                f))

    filelist = [f for f in
                os.listdir(
                    BaseClass.ROOT_PATH+'/reports')
                if f.endswith(".png")]

    for f in filelist:
        os.remove(
            os.path.join(
                BaseClass.ROOT_PATH+'/reports',
                f))
