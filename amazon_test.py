from selenium.webdriver import Chrome 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = Chrome()  

driver.get("https://www.amazon.com/")

login = driver.find_element(By.ID,"nav-link-accountList")
login.click()

input_email=driver.find_element(By.NAME,"email")
input_email.send_keys('pera_peric@gmail.com')

button=driver.find_element(By.ID,"continue")
button.click()

wait = WebDriverWait(driver,5)
wait.until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))

errorMessage = driver.find_element(By.CLASS_NAME,"a-alert-heading")
assert errorMessage.text == "There was a problem"
