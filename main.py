from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=900, 900')  # Last I checked this was necessary.

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
 

driver.get('http://127.0.0.1:5500/index.html')


# element = driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button")

# element.click()

time.sleep(10)


driver.save_screenshot(f'./images/{dt_string}.png')
 
driver.quit()