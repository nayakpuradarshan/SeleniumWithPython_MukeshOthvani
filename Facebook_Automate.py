from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

# Open below url
driver.get("https://www.facebook.com")

# Created the explicit wait
wait = WebDriverWait(driver, 10)

# Click on the create New Account button
wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()= 'Create New Account']"))).click()

# sent username
wait.until(EC.presence_of_element_located((By.NAME, "firstname"))).send_keys("Darshan")

# sent lastname
wait.until(EC.presence_of_element_located((By.NAME, "lastname"))).send_keys("Patel")

# sent mobile number
wait.until(EC.presence_of_element_located((By.NAME, "reg_email__"))).send_keys("9913991399")

# sent new password
wait.until(EC.presence_of_element_located((By.ID, "password_step_input"))).send_keys("@GH4*76")

# select date drom dropdown
Date = wait.until(EC.presence_of_element_located((By.ID, "day")))
DateCount = Select(Date)
DateCount.select_by_visible_text("31")

# select Month from dropdown
Month = wait.until(EC.presence_of_element_located((By.ID, "month")))
MonthCount = Select(Month)
MonthCount.select_by_visible_text("Aug")

# Select Year from dropdown
Year = wait.until(EC.presence_of_element_located((By.ID, "year")))
YearCount = Select(Year)
YearCount.select_by_visible_text("1996")

# select gender
wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()= 'Male']"))).click()

time.sleep(5)

driver.close()

