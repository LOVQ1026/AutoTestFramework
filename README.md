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

## 📦 快速开始

首先安装项目依赖：

```bash
pip install -r requirements.txt
```

然后运行测试，以下两种方式任选其一：

```bash
# 方式一：直接使用 pytest
pytest -v

# 方式二：一键运行（推荐，自动清理旧结果、执行测试、生成并打开报告）
python run.py
```

如果你想手动生成 Allure 报告（不使用 `run.py` 时）：

```bash
# 运行测试并生成结果数据
pytest --alluredir=reports/allure-results

# 生成 HTML 报告
allure generate reports/allure-results -o reports/allure-report --clean

# 启动本地服务并打开报告
allure open reports/allure-report
```

> **注意：** 不要直接双击 `index.html` 打开报告，否则浏览器会因跨域安全策略报 `500 Failed to fetch` 错误。必须通过 `allure open` 启动本地 HTTP 服务访问。

## 🔧 持续集成

项目已配置 GitHub Actions，在代码 push 或 pull request 时自动执行：

1. 拉取代码
2. 安装 Python
3. 安装依赖
4. 执行全部测试用例
5. 上传 pytest-html 报告和 Allure 结果

工作流文件：[.github/workflows/test.yml](.github/workflows/test.yml)

## 👤 作者

LOVQ1026

- GitHub: https://github.com/LOVQ1026
- 仓库: https://github.com/LOVQ1026/LovqTest

## 📄 许可

本项目仅用于学习与个人能力展示。