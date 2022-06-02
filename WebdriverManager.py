import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.goibibo.com")

wait = WebDriverWait(driver, 10)
from_location = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[1]/div[1]/div/div/p")))
from_location.click()

from_location.send_keys(By.XPATH, "//span[text()= 'Bhopal, India']")

time.sleep(5)

driver.close()

