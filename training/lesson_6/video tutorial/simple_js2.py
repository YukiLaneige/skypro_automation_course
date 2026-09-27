from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ru.wikipedia.org/wiki/")

driver.save_screenshot("screenshots/full_screen.png")

driver.quit()
