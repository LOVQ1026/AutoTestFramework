# LovqTest

![LovqTest CI](https://github.com/LOVQ1026/LovqTest/actions/workflows/ci.yml/badge.svg)

📊 **在线查看 Allure 测试报告：** [点击这里](https://lovq1026.github.io/LovqTest/)

基于 Selenium + pytest + Allure 的 Web / API 自动化测试实践项目。从 0 搭建，目前已跑通 18 个用例，并接入 GitHub Actions 持续集成。

## 🚀 主要功能
- 支持 UI 自动化与 API 测试
- 采用 POM（页面对象模型）设计
- YAML 数据驱动，支持参数化
- 集成 Allure，支持失败自动截图
- 一键运行脚本 `run.py`
- GitHub Actions 无头模式自动执行

## 📦 快速开始
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行测试
python run.py