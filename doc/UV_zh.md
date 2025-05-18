# UV

UV是一個套件/環境/Python 管理工具。
不一定得用UV(還有其他的像是pip/conda等)，但我們選擇這個。

---

## 安裝
* [uv 安裝](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)，依照官方網站的指示下載。

1. 建立一個資料夾，這個資料夾就專們存放一個專案內的程式。  
2. 打開終端機[?](./Terminal.md)，按照以下步驟執行(每一行為一個命令，逐步執行，*#*以後的是註解，可以選擇不輸入)：  

```shell
uv init test --app # 創建一個名為 test 的專案資料夾  
cd test # 進入 test 資料夾  
uv run main.py # 執行 main.py，並隱式建立 .venv 資料夾來存放環境數據  

uv python install 3.11.11 # 安裝 Python 版本 3.11.11  
uv run python main.py # 正常執行 main.py  

uv run --with jupyter jupyter lab # 啟動 Jupyter Lab  

```
  執行完最後一步你可以找到http://localhost:XXXX 的網址，那就是jupyter的網址。
  請放心你很安全，除非你的電腦有做特別的區域網路設定，否則這個網址只有你這台機器連得上。\
![jupyter image](./img/jupyter.png)
  
如果你成功到這裡，恭喜你你已經完成了。下方就是一些常用的指令，你可以玩一下

## 常用功能

```shell
uv init # 創建新虛擬環境
uv add  <Package> # 安裝套件
uv remove <Package>  # 移除套件
uv python  # python 版本相關指令
uv run <py_script>  # 在虛擬環境下 執行python 代碼
uv run python  # 在虛擬環境下開啟Python REPL 互動介面
uv tree  # 印出環境內套件相依性
uv tree --package <Package> # 印出環境內套件<Package>所依賴的套件
uv tree --revert --package <Package> # 印出環境內所有依賴套件<Package>的套件
uv pip # 兼容所有 pip 指令，若有套件能以pip進行管理安裝等可將pip的用法以uv pip代替
uv pip show <Package> # 查詢是否安裝<Package>套件
uv python install # 安裝在專案範圍內的 python 版本相關指令
```


---

- `uv init` 會建立虛擬環境，並生成 `pyproject.toml` 作為專案的設定檔，而 `lock` 檔案則包含專案的套件詳細資訊。  
- 與 `pip install` 兼容，可使用 `uv pip` 來安裝套件。但請記住，在使用 `uv pip` 安裝後，需執行 `uv add` 來將相依性新增到專案中。  
- UV 可執行 **pip venv** 和 **conda** 的功能，甚至更多。下載套件的速度比這兩者更快。  
- 具備適度的相依性解析能力。  


##
