from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M")

def delete(path):
    element = driver.find_element(By.XPATH, path)

    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)

    time.sleep(.1)


driver = webdriver.Chrome(ChromeDriverManager().install())
 

driver.get('https://www.google.com/maps/@42.6539778,21.1589676,15z/data=!5m1!1e1')

time.sleep(1)

element = driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button")

element.click()

time.sleep(4)

delete("/html/body/div[3]/div/div[26]")
delete("/html/body/div[3]/div[9]/div[23]/div[1]/div[2]")
delete("/html/body/div[3]/div[9]/div[23]/div[5]")
delete("/html/body/div[3]/div[9]/div[23]/div[5]")
delete("/html/body/div[3]/div[9]/div[3]")
delete("/html/body/div[3]/div[9]/div[4]")
delete("/html/body/div[3]/div[9]/div[21]")
delete("/html/body/div[3]/div[9]/div[8]")

driver.save_screenshot(f'{dt_string}.png')
 
driver.quit()