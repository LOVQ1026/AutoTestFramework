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