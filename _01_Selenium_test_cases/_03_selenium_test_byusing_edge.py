from selenium import webdriver
driver = webdriver.edge("executable_path=G:\\My driver\\msedgedriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
print(driver.title)
driver.close()