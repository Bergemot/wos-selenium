from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# 设置路径
download_path = "C://Users/Fosquer/Downloads/cite_2018"
chrome_driver_path = 'C://Program Files/Google/Chrome/Application/chromedriver.exe'

# 创建 Chrome WebDriver 实例
options = webdriver.ChromeOptions()

# 设置下载路径
options.add_experimental_option("prefs", {
    "download.default_directory": "your_download_directory_path",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)

action = ActionBuilder(driver)
# 打开Web of Science的链接
url = 'https://www.webofscience.com/wos/woscc/summary/b9b649ed-aeef-4c61-b0e0-fd86b9bc422e-aee1d3df/date-ascending/1'
driver.get(url)

# 等待页面加载完成（可以根据需要增加等待时间）
time.sleep(5)

# 接受cookie
butt=driver.find_element(By.CSS_SELECTOR,"#onetrust-accept-btn-handler")
butt.click()

# 点击Export按钮
butt=driver.find_element(By.CSS_SELECTOR,"#snRecListTop > app-export-menu > div > button > span.mat-button-wrapper")

# 等待一段时间以确保下拉菜单完全加载
time.sleep(2)  # 根据需要调整等待时间

# 选择export
export=driver.find_element(By.CSS_SELECTOR,"#snRecListTop > app-export-menu > div > button")
export.click()
time.sleep(2)

# 选择Tab Delimited File
butt=driver.find_element(By.CSS_SELECTOR,"#exportToTabWinButton")
butt.click()
time.sleep(2)

# 找到单选按钮
radio_button = driver.find_element(By.CSS_SELECTOR,"#radio3 > label > span.mat-radio-container")
# 选择单选按钮
radio_button.click()
time.sleep(1)

# 找到输入框
input_element = driver.find_element(By.CSS_SELECTOR,'#mat-input-0')
input_element.clear()
# 输入文本 "1"
input_element.send_keys('1')
time.sleep(1)

# 找到输入框
input_element = driver.find_element(By.CSS_SELECTOR,'#mat-input-1')
input_element.clear()
# 输入文本 "1000"
input_element.send_keys('1000')
time.sleep(1)

# 叉掉弹窗
x=driver.find_element(By.CSS_SELECTOR,'#pendo-close-guide-5600f670')
x.click()

# 找到按钮元素
button_element = driver.find_element(By.CSS_SELECTOR,"body > app-wos > main > div > div > div.holder > div > div > div.held > app-input-route:nth-child(3) > app-export-overlay > div > div.window > div.window-content.ng-star-inserted > app-export-out-details > div > div.window-content.ng-star-inserted > form > div > div.ng-star-inserted > wos-select")
# 点击按钮
button_element.click()
time.sleep(2)

# 选择edit
edit=driver.find_element(By.CSS_SELECTOR,'#global-select > div > div > div.wrap-mode.ng-star-inserted.active > button')
edit.click()
time.sleep(6)
# edit1
edit1=driver.find_element(By.CSS_SELECTOR,'#mat-checkbox-23 > label > span.mat-checkbox-label')
edit1.click()
time.sleep(2)  # 根据需要调整等待时间
# edit2
edit2=driver.find_element(By.CSS_SELECTOR,'#mat-checkbox-24 > label > span.mat-checkbox-label')
edit2.click()
time.sleep(2)  # 根据需要调整等待时间
# edit3
edit2=driver.find_element(By.CSS_SELECTOR,'#mat-checkbox-25 > label > span.mat-checkbox-label')
edit2.click()
time.sleep(2)  # 根据需要调整等待时间
# edit4
edit2=driver.find_element(By.CSS_SELECTOR,'#mat-checkbox-26 > label > span.mat-checkbox-label')
edit2.click()
time.sleep(2)  # 根据需要调整等待时间
# 确定edit
edit=driver.find_element(By.CSS_SELECTOR,'#mat-dialog-0 > app-custom-field-selection-dialog > div > div.mat-dialog-actions > div > button.mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary > span.mat-button-wrapper')
edit.click()
time.sleep(2)  # 根据需要调整等待时间

# 点击export
export_element = driver.find_element(By.CSS_SELECTOR,'body > app-wos > main > div > div > div.holder > div > div > div.held > app-input-route:nth-child(3) > app-export-overlay > div > div.window > div.window-content.ng-star-inserted > app-export-out-details > div > div.window-content.ng-star-inserted > form > div > div.flex-align.margin-top-20 > button.mat-focus-indicator.mat-flat-button.mat-button-base.mat-primary > span.mat-button-wrapper > span')
export_element.click()

# 等待下载
time.sleep(60)  # 根据需要调整等待时间

i = 1
j = i + 1000

# while j <= 103312:
while j <= 10000:
    t = 1
    print(f"i = {i}, j = {j}")
    i += 1000
    j = i + 1000
    # 选择export
    export = driver.find_element(By.CSS_SELECTOR, "#snRecListTop > app-export-menu > div > button")
    export.click()
    time.sleep(2)

    # 选择Tab Delimited File
    butt = driver.find_element(By.CSS_SELECTOR, "#exportToTabWinButton")
    butt.click()
    time.sleep(2)

    # 找到单选按钮
    radio_button = driver.find_element(By.CSS_SELECTOR, "#radio3 > label > span.mat-radio-container")
    # 选择单选按钮
    radio_button.click()
    time.sleep(2)

    # 找到输入框
    t += 1
    input_string = "#mat-input-" + str(t)
    input_element = driver.find_element(By.CSS_SELECTOR, input_string)
    input_element.clear()
    # 输入文本 i
    input_element.send_keys(str(i))
    time.sleep(2)
    t += 1
    # 找到输入框
    input_string = "#mat-input-" + str(t)
    input_element = driver.find_element(By.CSS_SELECTOR, input_string)
    input_element.clear()
    # 输入文本 j
    input_element.send_keys(str(j-1))
    time.sleep(2)


    # 找到按钮元素
    button_element = driver.find_element(By.CSS_SELECTOR,"body > app-wos > main > div > div > div.holder > div > div > div.held > app-input-route:nth-child(3) > app-export-overlay > div > div.window > div.window-content.ng-star-inserted > app-export-out-details > div > div.window-content.ng-star-inserted > form > div > div.ng-star-inserted > wos-select > button")
    # 点击按钮
    button_element.click()
    time.sleep(2)

    # edit
    edit = driver.find_element(By.CSS_SELECTOR,'#global-select > div > div > div:nth-child(5) > span')
    edit.click()
    time.sleep(3)  # 根据需要调整等待时间

    # 点击export
    export_element = driver.find_element(By.CSS_SELECTOR,
                                         'body > app-wos > main > div > div > div.holder > div > div > div.held > app-input-route:nth-child(3) > app-export-overlay > div > div.window > div.window-content.ng-star-inserted > app-export-out-details > div > div.window-content.ng-star-inserted > form > div > div.flex-align.margin-top-20 > button.mat-focus-indicator.mat-flat-button.mat-button-base.mat-primary > span.mat-button-wrapper > span')
    export_element.click()

    # 等待下载
    time.sleep(60)  # 根据需要调整等待时间


# driver.quit()
