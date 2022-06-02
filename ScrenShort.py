from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.python.org")
driver.get_screenshot_as_file("python_URL.png")

driver.quit()