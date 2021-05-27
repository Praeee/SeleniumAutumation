from selenium.webdriver import Chrome
import time

path = "C:\\Users\\paer_\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://the-internet.herokuapp.com/login")

# Maximum browser
driver.maximize_window()

def test(x, y):
    #   Text Username,Password
    driver.find_element_by_name("username").send_keys(x)
    driver.find_element_by_name("password").send_keys(y)
    #   Button Submit
    driver.find_element_by_xpath("//button[@type='submit']").click()


def logout():
    #   Button Logout
    driver.find_element_by_xpath('/html/body/div[2]/div/div/a').click()


# testcase : 1
test("tomsmith", "SuperSecretPassword!")
logout()
time.sleep(5)

test("tomsmith", "Password!")
time.sleep(5)

test("tomholland", "Password!")
time.sleep(5)

