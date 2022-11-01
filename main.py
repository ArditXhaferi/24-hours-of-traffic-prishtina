from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1600, 900')  # Last I checked this was necessary.

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M")

def delete(path):
    element = driver.find_element(By.XPATH, path)

    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)

    time.sleep(.1)


driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 

driver.get('https://www.google.com/maps/@42.6584911,21.1631733,15z/data=!5m1!1e1')

time.sleep(1)

# element = driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button")

# element.click()

# time.sleep(4)

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