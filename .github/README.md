# 建立你的開發環境  

- Python 直譯器  
- 套件管理  
- 虛擬環境  
- Jupyter  

---  
## 在開始寫Python程式之前...


### 終端機 Terminal

![Terminal](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/DEC_VT100_terminal_transparent.png/250px-DEC_VT100_terminal_transparent.png)

在很久很久以前當圖形介面操作仍未開發出，連滑鼠也不知為何物的時代，終端機便是人與電腦互動的媒介。它是純粹的文字顯示媒介，相較於現今五光十色的圖形介面以純文字的方式顯示程式運行的結果是最有效率，也由於當時沒有程式會需要顯示圖片。但也不是沒有辦法。

<img src="https://blog.filestack.com/wp-content/uploads/2017/01/Screen-Shot-2017-01-27-at-3.10.33-PM.png" width="45%" height="20%"><img src="https://velvetyne.fr/site/assets/files/2889/image-1.png" width="45%" height="45%">


這樣如何?這可都是文字與符號呢!總之，那是最原始的互動模式，上面那台像是印象管電視的大傢伙只是為了顯示文字而存在的，可沒有甚麼鼠標會在你的螢幕上。圖形化介面的誕生，讓人機互動的方式更多樣化並且仰賴滑鼠操作，但文字的交互模式仍然無法被替代，終端機也變成終端模擬器(Terminal emulator)給取代，模仿終端機功能的應用程式。

用終端機你可以以指令的方式操作電腦，例如切換目錄、列出路徑下所有檔案、複製檔案、移動檔案、開啟任何應用程式，~~並且讓其他人覺得你像駭客一樣酷~~。[學一下吧，很簡單的](https://www.youtube.com/watch?v=meI1f_N5ArI)[給windows用戶，只需看到11:50](https://www.youtube.com/watch?v=-fzO7iWCSWY)，[chatgpt](https://chatgpt.com/)也能幫得上忙。你至少需要知道如何切換目錄。有些令只有在特定路徑底下才會成功。

# 注意如果你一開始學習使用終端機在使用`rm`指令的時候要格外小心，
## 這是刪除檔案的指令，一不小心你會把整台電腦的檔案給刪掉。如果你沒有信心，用你熟悉的滑鼠做這個任務。告訴你一個事實，曾有一個工程師在曾經用這個指令意外刪除大半個伺服器資料。我也曾經把一天寫好的程式碼資料夾給全部刪除。`rm`雖然可怕，我建議你熟習其他操作後再慢慢嘗試這個。

### --help

在使用命令時，若對於命令有不了解的地方 可以利用 --help 參數印出該命令相關的使用方法

```shell
ls --help
cd --help
```

### 直譯 vs 編譯 -> transpile vs compile

執行python程式大部分都是利用Python直譯器將python的代碼文件在執行時邊翻譯成機器可讀的指令傳送給機器CPU執行。 直譯器就是個將python代碼翻譯成最底層的機器指令的媒介；與其他*編譯*語言不同，像是C語言，*編譯*語言需要將代碼文件在執行前將所有的代碼翻譯成執行檔(我們熟知的.exe檔案)後再運行該執行檔，只要代碼有任何修改，都必須再次編譯。雖然在執行效率上直譯語言較差，但是你不需要等待編譯的時間，有時編譯一個大的檔案會需要很久呢。

![compile meme](https://www.incredibuild.com/wp-content/uploads/2021/07/meme-1_fencing.jpg)

到此你知道要運行Python文件需要Python直譯器。那麼如果你已經安裝好Python直譯器你可以在終端機且在你放代碼的路徑底下輸入`python test.py` 運行test.py(只要你寫的代碼不需要額外的*參數*)，所謂*參數*是指，有時候為了泛用性我們會將代碼設計需要額外*參數*來運行，它看器來會像這樣`python test.py --arg1 abc --arg2 123 -arg3 456` 這表示執行test.py這隻程式我還給予了三個參數分別是arg1，arg2，arg3；三者的值分別是abc，123，456(先不考慮傳入的值在程式中會是甚麼型態)。一個參數都是由一個或兩個\*-\*組成，並且後面立即跟隨對應的數值，雖然有些參數並不需要給予數值，我們稱這種是*flag*，通常表示有了這個*flag*之下某個設定是開啟或關閉的，不給予*flag*代表某個設定是關閉或開啟的。一個常見的例子是設定傳入與輸出的路徑參數:`python test.py --input test.txt --output test_output.txt`。

### 寫第一支程式 Hello_world.py

創建一個文字檔**Hello_world.py**，並以任意的文字編輯軟體打開輸入以下內容後儲存。

```python
def hello_world():
    print('Hello world')
hello_world()
```  
開啟終端機且切換路徑到該文件底下輸入`python Hellow_world.py` 你應該就會看到**Hello world**的訊息被打印在你的終端機上。這樣的過程就是寫python程式的縮影，編輯代碼文字->執行代碼檢查結果是否正確->再次編輯代碼...


### 套件管理工具

所謂套件如同寫文章時會引用其他人的文句，寫程式也會直接使用他人寫的程式。例如文章的引用可能像是這樣

- 關傑才（1990）。《英譯廣東口語詞典》。香港：商務印書館。

而在python中像是這樣

```python
import openai
from random import sample
import pandas as pd
from itertools import chain
```
* `import openai`就像是說我要引用`openai`這個套件
* `from random import sample`就像是說我要從`random`套件引用`sample`
* `import pandas as pd`就像是說我要引用`pandas`套件，但以下我將稱呼它為`pd`
* `from itertools import chain as ch`就像是說我要從`itertools`套件引用 `chain` ，但以下我將稱呼它為`ch`

將套件下載後python有一套搜尋套件路徑的方式，只要這些套件被存在那些能被搜索到的路徑底下，python直譯器在執行階段就能正確的引入那些套件，有了引用你可以直接使用這些套件裡面的函數了。但這些和套件管理工具有甚麼關係呢? 在寫程式的時候，不同的問題解決專案，會放在不同的資料夾，確保兩者不互相干擾以及方便管理。同樣的分隔管理的概念在python套件上也會出現。

1. 首先，你如果不使用套件管理工具，你就需要手動下載並且管理這些檔案。在運行python之前需要改變一些python直譯器在運行時的設定等等。有了管理工具，它會幫你把這些事情做好，把套件存到該放的地方。
2. 再來，你必須知道套件事有不同版本的，當你寫A專案的程式需要的套件A只支援到10.0.1版但專案B同樣需要套件A但它需要至少11.0版。此時你就需要一個管理這些套件
3. 最後，你需要為不同的專案建立不同的 *虛擬環境* 也就是改變python搜尋套件的設定與套件下載路徑，讓python只搜尋在專案底下的的第三方套件

### 甚麼是程式碼編輯器/整合開發環境（integrated development environment)，IDE?

你能只用記事本來完成所有程式碼的撰寫，但IDE能幫你，調量程式碼、自動補全建議、以及一些其他有助於生產力的工具或插件讓你比較容易編輯程式碼，像是AI工具集成的程式碼編輯器可以讓你把程式碼給AI看讓它基於你的要求給出具體建議。

- **自動補全（Completion Hint）：**
    |程式碼編輯軟體   |記事本   |
    |-----------------|---------|
    | ![vscode image](https://i.sstatic.net/RCO3y.png) | ![note image](https://github.com/user-attachments/assets/aebf8c95-78b4-42f4-a1d7-0ef525a38bd4)|

    - 輸入 `d` -> 提示 `def`  
    - 輸入 `p` -> 提示 `print`  

    - **凸顯程式碼語法（Code Highlight）：**

        ![code hightlight](https://www.figma.com/community/resource/a76d3639-c5f0-49f2-992e-d6716f21f261/thumbnail)
        - `def hello_world()` -> `def`（綠色） `hello_world()`（白色）  

常見的程式碼編輯環境有*Vs code/Pycharm/IntelliJ/Jupyter/Colab*。

### 我為你選了

1. Jupyter 最陽春的編輯方式
2. uv 套件/環境管理工具，並用UV安裝python直譯器


### GitHub

GitHub 是一個程式碼倉庫分享的平台讓各個程式碼倉庫擁有自己的討論區，讓不同人一起協作。要和作者群回報問題或詢問程式細節都會到Issue進行發問，[這是這個代碼庫的討論區](https://github.com/nelson202277/Python101/issues)，只要有人在上面留言作者就會收到Email通知



## Install UV

[接下來就來進行安裝吧](../doc/UV_zh.md)


## 語法介紹

[語法介紹](../syntax/Python101.ipynb)
[Boot.dev](https://www.boot.dev/)

## 簡單openai範例程式

[example](../example/)

--
以下方步驟啟動假的server
```shell
cd example && uv run fastapi dev fake_server.py
```
