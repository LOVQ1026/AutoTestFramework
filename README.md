# AutoTestFramework

![AutoTest CI](https://github.com/LOVQ1026/AutoTestFramework/actions/workflows/ci.yml/badge.svg)

📊 **在线查看 Allure 测试报告：** [https://LOVQ1026.github.io/AutoTestFramework/](https://LOVQ1026.github.io/AutoTestFramework/)

基于 **Selenium + pytest + Allure** 的 Web / API 自动化测试框架，已集成 GitHub Actions 持续集成。

## 🚀 功能特性
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

## 📦 快速开始
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行测试（本地）
python run.py