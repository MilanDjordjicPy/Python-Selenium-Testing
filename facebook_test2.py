from selenium.webdriver import Chrome  

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.by import By
#iza izdvajanje


from selenium.webdriver.common.keys import Keys  
#za entera



driver = Chrome()

driver.get("https://google.com/")  

search=driver.find_element(By.NAME,"q")




search.send_keys("facebook")
search.send_keys(Keys.RETURN) #Pritiskanje entera


login = driver.find_element(By.PARTIAL_LINK_TEXT,"Фејсбук – пријавите се или се региструјте")
login.click()

input_email=driver.find_element(By.NAME,"email")
input_email.send_keys('pera_peric@gmail.com')

zaboravljena_sifra=driver.find_element(By.PARTIAL_LINK_TEXT,"Заборавили сте лозинку?")
zaboravljena_sifra.click()

driver.quit()
