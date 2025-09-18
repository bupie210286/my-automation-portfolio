# my-automation-portfolio
使用 Python 和 Selenium 進行網頁自動化測試的專案集。

# Python 自動化測試作品集

這個專案集收錄了使用 **Python** 語言和 **Pytest** 測試框架所撰寫的自動化測試案例，並使用 **Selenium** 進行網頁使用者介面 (UI) 測試。

---

### 專案所用技術

- **程式語言**: Python
- **測試框架**: Pytest
- **網頁自動化工具**: Selenium
- **版本控制**: Git

---

### 環境設定與安裝

在執行測試之前，請確保你的環境已具備以下條件：

1.  **安裝 Python**: 
    - 如果尚未安裝，請從 [Python 官網](https://www.python.org/downloads/) 下載並安裝最新版本。

2.  **安裝必要的套件**:
    - 開啟你的命令提示字元或終端機，執行以下指令來安裝 Pytest 和 Selenium。
    ```bash
    pip install pytest selenium
    ```

3.  **下載瀏覽器驅動程式 (Chromedriver)**:
    - 你的電腦需要有對應的瀏覽器驅動程式，才能讓 Selenium 控制瀏覽器。
    - 前往 [Chromedriver 官方下載頁面](https://googlechromelabs.github.io/chrome-for-testing/)。
    - 找到與你 Chrome 瀏覽器版本相符的驅動程式，並將其下載後，解壓縮到此專案的根目錄下。

---

### 如何執行測試

完成上述設定後，你可以透過一個簡單的指令來執行所有的測試案例。

- 在此專案的根目錄下，執行以下指令：
```bash
pytest