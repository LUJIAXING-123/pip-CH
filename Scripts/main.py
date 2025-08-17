from subprocess import run
from time import sleep as wait
import os

class MainForWindows:
    def __init__(self):
        self.main()

    @staticmethod
    def next_page():
        for i in range(100):
            print()

    def install(self):
        self.next_page()

        install_name=input("输入你安装的库名：")
        is_china=input("是否使用国内源下载？(是输入y，否输入n)")

        while True:
            if is_china=='y':
                url='-i https://pypi.tuna.tsinghua.edu.cn/simple'
                break
            elif is_china=='n':
                url=''
                break
            else:
                print("无效的输入。。。")
                wait(3)

        print('请稍等...')
        output_install=run("pip install %s %s"%(install_name,url),shell=True,capture_output=True,text=True)

        if 'Successfully installed ' in output_install.stdout:
            print("安装成功！")
            wait(3)

        elif 'Requirement already satisfied:' in output_install.stdout:
            print("该库已安装！")
            wait(3)

        else:
            print("安装失败！")
            wait(3)

        print('是否显示终端输出？(是输入y，否输入n)')
        set=input()

        if set=='y':
            print(output_install.stdout+'\n'+output_install.stderr)
            wait(5)

        self.main()

    def uninstall(self):
        self.next_page()

        uninstall_name=input("输入你卸载的库名：")
        print("真的要卸载吗？(是输入y，否输入n)")
        output_uninstall=run("pip uninstall %s"%uninstall_name,shell=True,capture_output=True,text=True)

        if 'WARNING: Skipping' in output_uninstall.stderr:
            print("该库已卸载或输入错误！")
            wait(3)

        if 'Successfully uninstalled' in output_uninstall.stdout:
            print("卸载成功！")
            wait(3)

        print('是否显示终端输出？(是输入y，否输入n)')
        set = input()

        if set=='y':
            print(output_uninstall.stdout+'\n'+output_uninstall.stderr)
            wait(5)

        self.main()

    def main(self):
        self.next_page()

        update=run('python -m pip install --upgrade pip',shell=True,capture_output=True,text=True)

        if 'Successfully installed' in update.stdout:
            print('更新完成！')
            wait(3)

        elif 'Requirement already satisfied:' in update.stdout:
            print('已是最新版！')
            wait(3)

        else:
            print('更新错误！')
            wait(3)

        print('欢迎使用PIP-Python By JIAXING汉化版！')
        print()
        print('#####################################################')
        print()
        print('输入  ins  以安装库')
        print('输入  uni  以卸载库')
        print('输入  q  以退出')
        print()
        print('注：此工具无法为 .venv 环境运行PIP工具！')
        print()

        cmd = input('输入你的操作：')
        if cmd == 'ins':
            self.install()

        if cmd == 'uni':
            self.uninstall()

        if cmd == 'q':
            quit(114514)

        else:
            print('无效的输入。。。')
            wait(3)
            self.main()

class MainForMacOS:
    def __init__(self):
        self.main()

    @staticmethod
    def next_page():
        for i in range(100):
            print()

    def install(self):
        self.next_page()

        install_name=input("输入你安装的库名：")
        is_china=input("是否使用国内源下载？(是输入y，否输入n)")

        while True:
            if is_china=='y':
                url='-i https://pypi.tuna.tsinghua.edu.cn/simple'
                break
            elif is_china=='n':
                url=''
                break
            else:
                print("无效的输入。。。")
                wait(3)

        print('请稍等...')
        output_install=run("pip3 install %s %s"%(install_name,url),shell=True,capture_output=True,text=True)

        if 'Successfully installed ' in output_install.stdout:
            print("安装成功！")
            wait(3)

        elif 'Requirement already satisfied:' in output_install.stdout:
            print("该库已安装！")
            wait(3)

        else:
            print("安装失败！")
            wait(3)

        print('是否显示终端输出？(是输入y，否输入n)')
        set=input()

        if set=='y':
            print(output_install.stdout+'\n'+output_install.stderr)
            wait(5)

        self.main()

    def uninstall(self):
        self.next_page()

        uninstall_name=input("输入你卸载的库名：")
        print("真的要卸载吗？(是输入y，否输入n)")
        output_uninstall=run("pip3 uninstall %s"%uninstall_name,shell=True,capture_output=True,text=True)

        if 'WARNING: Skipping' in output_uninstall.stderr:
            print("该库已卸载或输入错误！")
            wait(3)

        if 'Successfully uninstalled' in output_uninstall.stdout:
            print("卸载成功！")
            wait(3)

        print('是否显示终端输出？(是输入y，否输入n)')
        set = input()

        if set=='y':
            print(output_uninstall.stdout+'\n'+output_uninstall.stderr)
            wait(5)

        self.main()

    def main(self):
        self.next_page()

        update=run('python3 -m pip install --upgrade pip',shell=True,capture_output=True,text=True)

        if 'Successfully installed' in update.stdout:
            print('更新完成！')
            wait(3)

        elif 'Requirement already satisfied:' in update.stdout:
            print('已是最新版！')
            wait(3)

        else:
            print('更新错误！')
            wait(3)

        print('欢迎使用PIP-Python By JIAXING汉化版！')
        print()
        print('#####################################################')
        print()
        print('输入  ins  以安装库')
        print('输入  uni  以卸载库')
        print('输入  q  以退出')
        print()
        print('注：此工具无法为 .venv 环境运行PIP工具！')
        print()

        cmd = input('输入你的操作：')
        if cmd == 'ins':
            self.install()

        if cmd == 'uni':
            self.uninstall()

        if cmd == 'q':
            quit(114514)

        else:
            print('无效的输入。。。')
            wait(3)
            self.main()

if __name__ == '__main__'and os.name == 'nt':
    MainForWindows()

else:
    MainForMacOS()