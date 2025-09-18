from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_google_search():
    # 1. 開啟 Chrome 瀏覽器
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 2. 前往 Google 搜尋頁面
    driver.get("https://www.google.com")

    # 3. 找到搜尋框並輸入關鍵字
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python 自動化測試")

    # 4. 模擬按下 Enter 鍵
    search_box.send_keys(Keys.ENTER)

    # 5. (選擇性) 等待幾秒，讓你看到搜尋結果
    time.sleep(5)

    # 6. 關閉瀏覽器
    driver.quit()