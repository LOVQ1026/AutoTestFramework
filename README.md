# LovqTest

![LovqTest CI](https://github.com/LOVQ1026/LovqTest/actions/workflows/ci.yml/badge.svg)

📊 **在线查看 Allure 测试报告：** [点击这里](https://lovq1026.github.io/LovqTest/)

基于 Selenium + pytest + Allure 的 Web / API 自动化测试实践项目。从 0 搭建，目前已跑通 18 个用例，并接入 GitHub Actions 持续集成。

## 🚀 主要功能

- 支持 UI 自动化与 API 测试
- 采用 POM（页面对象模型）设计，代码分层清晰
- 支持 YAML 数据驱动与 pytest 参数化
- 集成 Allure 报告，测试失败自动截图
- 一键运行脚本 `run.py`，自动清理、生成并打开报告
- 集成 GitHub Actions，支持无头模式自动化运行

## 🛠️ 技术栈

- Python 3.12+
- Selenium 4
- pytest 8
- Allure 2
- requests
- PyYAML
- GitHub Actions

## 📁 项目结构

```text
LovqTest/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions 配置
├── api/                        # API 接口封装
│   ├── api_client.py
│   └── user_api.py
├── common/                     # 公共模块
│   ├── allure_helper.py        # Allure 截图附件
│   ├── config.py               # 配置读取
│   ├── data_reader.py          # YAML 数据读取
│   ├── driver.py               # WebDriver 创建
│   ├── logger.py               # 日志封装
│   ├── request.py              # requests 封装
│   ├── screenshot.py           # 截图工具
│   └── wait.py                 # 显式等待
├── config/
│   └── config.yaml             # 配置文件
├── data/
│   ├── login_data.yaml         # 登录测试数据
│   └── users.py                # 用户参数化数据
├── pages/                      # 页面对象（POM）
│   ├── base_page.py            # 基类（含 JS 兜底点击）
│   └── login_page.py           # 登录页
├── testcases/                  # 测试用例
│   ├── test_api_demo.py
│   ├── test_api_user.py
│   ├── test_baidu.py
│   ├── test_config.py
│   ├── test_data.py
│   ├── test_data_reader.py
│   ├── test_fail.py            # 故意失败用例（xfail）
│   ├── test_fixture.py
│   ├── test_locator.py
│   ├── test_logger.py
│   ├── test_login.py
│   ├── test_login_data.py
│   └── test_parametrize.py
├── conftest.py                 # pytest fixture 和 hook
├── pytest.ini                  # pytest 配置
├── run.py                      # 一键运行入口
├── requirements.txt
└── README.md

📦 快速开始
1. 安装依赖
bash
pip install -r requirements.txt

2. 运行测试
bash
# 方式一：直接使用 pytest
pytest -v

# 方式二：一键运行（推荐）
python run.py

3. 手动生成 Allure 报告
bash
# 运行测试并生成结果数据
pytest --alluredir=reports/allure-results

# 生成 HTML 报告
allure generate reports/allure-results -o reports/allure-report --clean

# 启动本地服务并打开报告
allure open reports/allure-report

🔧 CI/CD
本项目已集成 GitHub Actions，每次 push 到 main 分支会自动触发：

安装 Python 3.12 和项目依赖

以无头模式（HEADLESS=true）运行 Selenium 测试

生成 Allure HTML 报告

将报告自动部署到 GitHub Pages

在线报告地址：https://lovq1026.github.io/LovqTest/

🏷️ 测试标记
标记	说明
smoke	冒烟测试
regression	回归测试
使用示例：

python
import pytest

@pytest.mark.smoke
def test_login(driver):
    ...
按标记运行：

bash
pytest -m smoke

## 作者

**LOVQ1026**

- GitHub：https://github.com/LOVQ1026
- 仓库：https://github.com/LOVQ1026/LovqTest

---

## License

本项目仅用于学习与个人能力展示。