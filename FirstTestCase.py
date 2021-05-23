from selenium.webdriver import Chrome

path="C:\\Users\\paer_\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://the-internet.herokuapp.com/login")

# Maximum browser
driver.maximize_window()

#Enter Data to textbox
driver.find_element_by_name("username").send_keys("tomsmith")
driver.find_element_by_name("password").send_keys("SuperSecretPassword!")

#Work on Button
driver.find_element_by_xpath("//button[@type='submit']").click()

driver.find_element_by_xpath('/html/body/div[2]/div/div/a').click()
