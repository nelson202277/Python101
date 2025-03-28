# 建立你的開發環境  

- Python 直譯器  
- 套件管理  
- 虛擬環境  
- Jupyter  

---  

## 什麼是程式碼？  

程式碼本質上就是一個純文字檔案，具有特定的副檔名（Python 使用 `.py`）。  

**理論上，你可以使用任何文字編輯器來撰寫程式碼。**  

現在，讓我們來看下面這段 Python 程式碼（很簡單，不用緊張）。  

```python
def hello_world():
    print('Hello world')
hello_world()
```  

在這段程式碼中，我們使用 `def` 定義了一個**函式**，名稱為 `hello_world`，這個函式的功能就是輸出 `Hello world` 這段文字。  

最後一行的 `hello_world()` 便是執行這個函式。  

你可以自己用一般的文字編輯器輸入這些字元。  
但如果使用程式碼編輯器，通常會有**自動補全**和**程式碼高亮**的功能，提升編輯速度和可讀性。  

- **自動補全（Completion Hint）：**
  |程式碼編輯軟體   |記事本   |
  |-----------------|---------|
  | ![vscode image](https://i.sstatic.net/RCO3y.png) | ![note image](https://github.com/user-attachments/assets/aebf8c95-78b4-42f4-a1d7-0ef525a38bd4)|

  - 輸入 `d` -> 提示 `def`  
  - 輸入 `p` -> 提示 `print`  

- **凸顯程式碼語法（Code Highlight）：**
  
  ![code hightlight](https://www.figma.com/community/resource/a76d3639-c5f0-49f2-992e-d6716f21f261/thumbnail)
  - `def hello_world()` -> `def`（綠色） `hello_world()`（白色）  

這讓程式撰寫更快、更直觀。  

---  

## 直譯器（Interpreter）  

當我們寫好 Python 程式後，還需要一個**直譯器**來執行程式碼。  

直譯器會**逐行**讀取你的程式碼，將其轉換為機器能夠理解的指令，並交給電腦執行。  

---  

## 套件（Packages）  

套件是一組預先編寫好的程式碼，針對特定需求而設計，例如：  

- 讀取 CSV 檔案  
- 讀取圖片檔案  
- 影像處理  
- 網路連線  

在開發時，我們通常遵循 **DRY（Don't Repeat Yourself）** 原則，避免重複造輪子。  
因此，我們會使用開源的套件，而不是自己從零開始開發。  

### 套件管理工具（Package Manager）  

套件與套件之間版本問題，相依性問題，而 **套件管理工具**可以幫助我們管理一個專案中的套件。\
它可以幫助安裝、移除套件，並自動解決相依性問題。  

---  

## 環境管理（Environment Manager）  

你可以把**環境（Environment）**想像成開發環境的設定狀態，這包含了：  

- 你的 Python 版本  
- 你安裝的套件  
- 其他相關的設定  

當你的專案數量增加，不同專案可能會需要不同的 Python 版本或不同的套件。  
我們通常希望**隔離**每個專案的環境，避免套件版本衝突，確保程式能夠在特定環境下穩定運行。  

當你需要部署程式時，擁有獨立的環境也能讓專案更容易打包與發佈。


[接下來就來進行安裝吧](./UV_zh.md)

有任何問題就發個[issue](https://github.com/nelson202277/Python101/issues)吧
