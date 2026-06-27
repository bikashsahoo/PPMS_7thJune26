# VIDEO 1 1:07:18
import pytest  #Used for fixtures, test execution, command-line options, etc
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )

# above function means "Pytest, create a command-line option called --browser"
# below Read the value stored in --browser and return it
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# "request" is a built-in pytest fixture object.,"request" contains lots of information about the current pytest run
# Inside request there is a property called config, "request.config"=>This stores pytest configuration information., in cmd line we write "pytest test_login.py --browser firefox" => here browser = firefox =>Pytest saves: inside its configuration.
# "getoption()"=>"Go to pytest configuration and get the value of --browser"
# ====> getoption() belongs to pytest's configuration object.
# ====> To access that configuration object, pytest gives us request.
# ====> Through request, we access config.
# ====> Through config, we access getoption().
# ====> Gets the value supplied from command line., example : pytest --browser firefox, return firefox
# --------------Conclusion--------------
#1. Command: pytest test_login.py --browser firefox
#2. Then: request.config.getoption("--browser")
#3. returns:  "firefox"

# So the request object is simply the bridge that allows your fixture to access pytest's runtime information, including command-line options like --browser.

@pytest.fixture()
# browser = browser() it means this what ever value return that store in variable browser
def setup(browser):

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    yield driver
    driver.quit()

# ==> (i)yield driver and (ii)return driver
#  They both give the driver object to the test, but they behave differently after the test finishes

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver
#
#     driver.quit()   # NEVER executes
#
# conclusion :
# will never run because execution stops at return.
# driver.quit()
#
# --------------------------------------------------------
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#
#     yield driver
#
#     driver.quit()   # Executes after test
#
# conclusion :
# This line does execute after the test ends.
