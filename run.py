import os
import sys
import time
import shutil
import subprocess
import webbrowser
import pytest


# ========== 路径配置 ==========
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "reports")
ALLURE_RESULT_DIR = os.path.join(REPORT_DIR, "allure-results")
ALLURE_REPORT_DIR = os.path.join(REPORT_DIR, "allure-report")


def clean_dir(path):
    """删除目录，如果不存在则忽略"""
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"[清理] 已删除: {path}")


def is_allure_installed():
    """检查 allure 命令行是否可用"""
    try:
        subprocess.run(
            ["allure", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            shell=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def run_tests():
    """运行 pytest，生成 Allure 结果"""
    print("\n" + "=" * 60)
    print("[1/3] 开始运行测试...")
    print("=" * 60)

    exit_code = pytest.main([
        "-v",
        "-s",
        "testcases",
        f"--alluredir={ALLURE_RESULT_DIR}",
        "--clean-alluredir",
    ])
    return exit_code


def generate_allure_report():
    """使用 allure 命令行生成 HTML 报告"""
    print("\n" + "=" * 60)
    print("[2/3] 生成 Allure 报告...")
    print("=" * 60)

    if not is_allure_installed():
        print("[警告] 未检测到 allure 命令行工具，跳过报告生成。")
        print("安装方法（任选其一）：")
        print("  1) Scoop:  scoop install allure")
        print("  2) npm:    npm install -g allure-commandline")
        print("  3) 手动:   下载 https://github.com/allure-framework/allure2/releases")
        print("           解压后把 bin 目录加入 PATH")
        return False

    # 生成新的报告前先清掉旧报告
    clean_dir(ALLURE_REPORT_DIR)

    try:
        subprocess.run(
            [
                "allure", "generate",
                ALLURE_RESULT_DIR,
                "-o", ALLURE_REPORT_DIR,
                "--clean"
            ],
            check=True,
            shell=True
        )
        print(f"[完成] 报告已生成: {ALLURE_REPORT_DIR}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[错误] Allure 报告生成失败: {e}")
        return False


def open_report():
    """使用 allure open 启动本地服务并打开报告"""
    print("\n" + "=" * 60)
    print("[3/3] 启动 Allure 本地服务并打开报告...")
    print("=" * 60)

    if not is_allure_installed():
        print("[警告] 未检测到 allure 命令，无法使用 allure open。")
        print(f"请手动执行: allure open {ALLURE_REPORT_DIR}")
        return

    # 使用 Popen 避免阻塞主进程（Allure 服务会在后台持续运行）
    subprocess.Popen(["allure", "open", ALLURE_REPORT_DIR], shell=True)
    print(f"[完成] 正在浏览器中打开 Allure 服务，默认地址: http://localhost:4040")

def main():
    start = time.time()

    # 0. 准备目录
    os.makedirs(REPORT_DIR, exist_ok=True)
    clean_dir(ALLURE_RESULT_DIR)

    # 1. 运行测试
    exit_code = run_tests()

    # 2. 生成报告
    report_ok = generate_allure_report()

    # 3. 打开报告
    if report_ok:
        open_report()

    # 总结
    elapsed = time.time() - start
    print("\n" + "=" * 60)
    print(f"全部流程执行完毕，耗时: {elapsed:.2f} 秒")
    print(f"pytest 退出码: {exit_code}")
    print("=" * 60)

    # 把 pytest 的退出码透传给调用者，方便 CI 判断成功/失败
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

input("按回车键退出...")