from selenium import webdriver
driver = webdriver.firefox(executable_path="G:\\My driver\\geckodriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
print(driver.title)
driver.close()