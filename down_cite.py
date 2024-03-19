from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

# 设置路径
download_path = "C://Users/Fosquer/Downloads/"
chrome_driver_path = 'C://Program Files/Google/Chrome/Application/chromedriver.exe'

i = 1
j = i + 1000
t = 1

while i <= 77000:
    # 创建 Chrome WebDriver 实例
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # 隐藏浏览器页面

    # 设置下载路径
    options.add_experimental_option("prefs", {
        "download.default_directory": "your_download_directory_path",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(options=options)

    # 打开Web of Science的链接
    url = 'https://webofscience.clarivate.cn/wos/woscc/summary/7a33147b-b150-4d54-a84c-db4b8c538757-c347c09b/relevance/1'
    driver.get(url)
    driver.maximize_window()
    #time.sleep(2)
    #driver.minimize_window() # 最小化窗口
    # driver.set_window_size(400, 300)
    # 等待页面加载完成
    time.sleep(5)

    # 接受所有小饼干
    butt = driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
    butt.click()
    print("已接受cookie")
    time.sleep(1)

    # 叉掉弹窗
    #bitch = driver.find_element(By.CSS_SELECTOR, "#pendo-close-guide-5600f670")
    #bitch.click()
    #print("已关掉弹窗")
    #time.sleep(3)

    # 选择export
    export = driver.find_element(By.CSS_SELECTOR, "#snRecListTop > app-export-menu > div > button")
    export.click()
    print("已点击export")
    time.sleep(1)

    # 选择Tab Delimited File
    butt = driver.find_element(By.CSS_SELECTOR, "#exportToTabWinButton")
    butt.click()
    time.sleep(1)
    print("已选择Tab")

    # 找到单选按钮
    radio_button = driver.find_element(By.CSS_SELECTOR, "#radio3 > label > span.mat-radio-container")
    # 选择单选按钮
    radio_button.click()
    time.sleep(1)
    print("已选择range")

    # 找到输入框
    input_element = driver.find_element(By.CSS_SELECTOR, '#mat-input-0')
    input_element.clear()
    # 输入文本 "1"
    input_element.send_keys(str(i))
    time.sleep(1)

    # 找到输入框
    input_element = driver.find_element(By.CSS_SELECTOR, '#mat-input-1')
    input_element.clear()
    # 输入文本 "1000"
    input_element.send_keys(str(j-1))
    time.sleep(1)
    print("此次下载",i,'到',j-1)

    # 找到按钮元素
    button_element = driver.find_element(By.CSS_SELECTOR,
                                         "body > app-wos > main > div > div > div.holder > div > div > div.held > app-input-route:nth-child(3) > app-export-overlay > div > div.window > div.window-content.ng-star-inserted > app-export-out-details > div > div.window-content.ng-star-inserted > form > div > div.ng-star-inserted > wos-select")
    # 点击按钮
    button_element.click()
    time.sleep(1)
    # 选择edit
    edit = driver.find_element(By.CSS_SELECTOR,
                               '#global-select > div > div > div:nth-child(5) > button > span.mat-button-wrapper')

    edit.click()
    time.sleep(3)
    print("已点击edit")

    # edit1
    edit1 = driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-20 > label > span.mat-checkbox-label')
    edit1.click()
    time.sleep(1)  # 根据需要调整等待时间
    print("已点击edit1")
    # edit2
    edit2 = driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-30 > label > span.mat-checkbox-label')
    edit2.click()
    time.sleep(1)  # 根据需要调整等待时间
    print("已点击edit2")
    # edit3
    edit2 = driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-39 > label > span.mat-checkbox-label')
    edit2.click()
    time.sleep(1)  # 根据需要调整等待时间
    print("已点击edit3")
    # edit4
    edit2 = driver.find_element(By.CSS_SELECTOR, '#mat-checkbox-45 > label > span.mat-checkbox-label')
    edit2.click()
    time.sleep(1)  # 根据需要调整等待时间
    print("已点击edit4")

    # 确定edit
    edit = driver.find_element(By.CSS_SELECTOR,
                               '#mat-dialog-0 > app-custom-field-selection-dialog > div > div.mat-dialog-actions > div > button.mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary > span.mat-button-wrapper')
    edit.click()
    time.sleep(2)  # 根据需要调整等待时间
    print("已完成所有edit")

    check = driver.find_element(By.CSS_SELECTOR, 'body > app-wos > main > div > div > div.holder > div > div > div.held > app-input-route:nth-child(3) > app-export-overlay > div > div.window > div.window-content.ng-star-inserted > app-export-out-details > div > div.window-content.ng-star-inserted > form > div > div.ng-star-inserted > wos-select > button')
    aria_label = check.get_attribute("aria-label")

    # 检查导出项个数
    if aria_label != " Custom selection (29)":
        print("error")
        driver.quit()
        continue
    else:
        print("edit选项为：Custom selection (29)")

    # 点击export
    export_element = driver.find_element(By.CSS_SELECTOR,
                                         'body > app-wos > main > div > div > div.holder > div > div > div.held > app-input-route:nth-child(3) > app-export-overlay > div > div.window > div.window-content.ng-star-inserted > app-export-out-details > div > div.window-content.ng-star-inserted > form > div > div.flex-align.margin-top-20 > button.mat-focus-indicator.mat-flat-button.mat-button-base.mat-primary > span.mat-button-wrapper > span')
    export_element.click()
    time.sleep(2)

    t += 1
    # 等待下载
    downloaded_file = download_path + 'savedrecs (' + str(t) + ').txt'
    while not os.path.exists(downloaded_file):
        time.sleep(1)
    print(t,"download：", i,"——", j-1)
    i += 1000
    j = i + 1000
    driver.quit()
