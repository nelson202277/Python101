# UV

一個套件/環境/Python 管理工具。  

---

* [uv 安裝](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)

1. 建立一個專案資料夾。  
2. 打開終端機，按照以下步驟執行：  

```bash
uv init test --app # 創建一個名為 test 的專案資料夾  
cd test # 進入 test 資料夾  
uv run main.py # 執行 main.py，並隱式建立 .venv 資料夾來存放環境數據  

uv python install 3.11.11 # 安裝 Python 版本 3.11.11  
python main.py # 正常執行 main.py  

uv run --with jupyter jupyter lab # 啟動 Jupyter Lab  

```

3. UV 的功能不僅限於上述操作，使用 `--help` 獲取更多資訊：  

```bash
uv --help
uv add --help
uv remove --help
uv python --help
uv run --help
uv tree --help
```

4. 例如：安裝套件  

```bash
uv add pandas
```

---

- `uv init` 會建立虛擬環境，並生成 `pyproject.toml` 作為專案的設定檔，而 `lock` 檔案則包含專案的套件詳細資訊。  
- 與 `pip install` 兼容，可使用 `uv pip` 來安裝套件。但請記住，在使用 `uv pip` 安裝後，需執行 `uv add` 來將相依性新增到專案中。  
- UV 可執行 **pip venv** 和 **conda** 的功能，甚至更多。下載套件的速度比這兩者更快。  
- 具備適度的相依性解析能力。  
