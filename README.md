# AutoTestFramework

基于 Selenium + pytest + Allure 的 Web 自动化测试框架。

## 环境要求
- Python 3.10+
- Chrome 浏览器

## 安装依赖
```bash
pip install -r requirements.txt

## 运行测试
```bash
pytest -v -s
##生成 Allure 报告
pytest --alluredir=reports/allure-results
allure serve reports/allure-results