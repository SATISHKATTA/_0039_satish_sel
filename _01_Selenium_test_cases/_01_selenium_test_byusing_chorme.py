from selenium import webdriver
driver = webdriver.Chrome(executable_path="G:\\My driver\\chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
print(driver.title)
driver.close()