import os
import tkinter as tk
import tkinter.messagebox as msg
from subprocess import run

class MainFace:
    def __init__(self):
        global TrueType
        self.frame = None
        self.create_widget()

    def create_widget(self):
        self.frame = tk.Frame(root)
        self.frame.pack()
        tk.Label(self.frame,text='欢迎使用pip-CH！',font=(TrueType,32)).pack(pady=10)

        self.update()

        frame = tk.Frame(self.frame)
        frame.pack(padx=20,pady=50)

        tk.Button(frame,text='安装库',command=self.install,font=(TrueType,32)).grid(row=3,column=0)
        tk.Button(frame,text='卸载库',command=self.uninstall,font=(TrueType,32)).grid(row=3,column=3)
        tk.Button(frame, text='退出', command=self.exit, font=(TrueType, 32)).grid(row=7,column=1,pady=30)

    @staticmethod
    def update():
        if os.name == 'nt':
            update = run('python -m pip install --upgrade pip', shell=True, capture_output=True, text=True)

        else:
            update = run('python3 -m pip install --upgrade pip', shell=True, capture_output=True, text=True)

        with open('../log\\update_log.log', 'w') as f:
            f.write(update.stdout+update.stderr)

        if 'Successfully installed' in update.stdout:
            msg.showinfo(title='pip-CH',message='更新完成！')

        elif 'Requirement already satisfied:' in update.stdout:
            msg.showinfo(title='pip-CH',message='已是最新版！')

        else:
            msg.showerror(title='pip-CH',message='更新错误！')

    def install(self):
        self.frame.destroy()
        StartInstall()

    def uninstall(self):
        self.frame.destroy()
        StartUNInstall()

    @staticmethod
    def exit():
        exit(114514)

class StartInstall: #背单词界面
    def __init__(self):
        global TrueType
        self.command = None
        self.is_China = None
        self.install_name = None
        self.frame = None
        self.is_china_var = tk.StringVar()
        self.entry=tk.StringVar()
        self.var_entry = tk.StringVar()
        self.create_widget()

        self.is_china_var.set('1')

    def create_widget(self):
        self.frame = tk.Frame(root)
        self.frame.pack()
        tk.Label(self.frame,text='配置',font=(TrueType,18)).pack()

        self.frame.update()
        install_name_frame = tk.Frame(self.frame)
        install_name_frame.pack()

        tk.Label(install_name_frame,text='要安装的包的名字：',font=(TrueType,13)).grid(row=0,column=0)
        tk.Entry(install_name_frame,textvariable=self.entry).grid(row=0,column=1)

        self.frame.update()
        is_china_frame = tk.Frame(self.frame)
        is_china_frame.pack()

        tk.Label(is_china_frame,text='是否使用国内源？',font=(TrueType,13)).grid(row=0,column=0)
        tk.Radiobutton(is_china_frame,text='是',variable=self.is_china_var,value=0).grid(row=1,column=0)
        tk.Radiobutton(is_china_frame,text='否',variable=self.is_china_var,value=1).grid(row=1,column=1)

        frame2 = tk.Frame(self.frame)
        frame2.pack(side='bottom')
        tk.Button(frame2, text="开始", command=self.get_information, font=(TrueType, 18), width=6).grid(row=4, column=0, padx=10,pady=10)
        tk.Button(frame2, text="返回", command=self.exit, font=(TrueType, 18), width=6).grid(row=4, column=1, padx=10,pady=10)

    def get_information(self):
        self.install_name=self.entry.get()

        if self.is_china_var.get()=='0':
            self.is_China=' -i https://pypi.tuna.tsinghua.edu.cn/simple'

        else:
            self.is_China=''

        if os.name == 'nt':
            self.start_for_windows()

        else:
            self.start_for_macos()

    def start_for_windows(self):
        self.command=run('pip install '+self.install_name+self.is_China,shell=True,capture_output=True,text=True)

        with open('../log\\install_log.log', 'w') as f:
            f.write(self.command.stdout+self.command.stderr)

        if 'Successfully installed ' in self.command.stdout:
            msg.showinfo(title='pip-CH',message='安装成功')

        elif 'Requirement already satisfied:' in self.command.stdout:
            msg.showinfo(title='pip-CH',message="该库已安装！")

        else:
            msg.showerror(title='pip-CH',message="安装失败！")

        self.exit()

    def start_for_macos(self):
        self.command=run('pip3 install '+self.install_name+self.is_China,shell=True,capture_output=True,text=True)

        with open('../log\\install_log.log', 'w') as f:
            f.write(self.command.stdout+self.command.stderr)

        if 'Successfully installed ' in self.command.stdout:
            msg.showinfo(title='pip-CH',message='安装成功')

        elif 'Requirement already satisfied:' in self.command.stdout:
            msg.showinfo(title='pip-CH',message="该库已安装！")

        else:
            msg.showerror(title='pip-CH',message="安装失败！")

        self.exit()

    def exit(self):
        self.frame.destroy()
        MainFace()

class StartUNInstall: #背单词界面
    def __init__(self):
        global TrueType
        self.command = None
        self.uninstall_name = None
        self.frame = None
        self.is_china_var = tk.StringVar()
        self.entry=tk.StringVar()
        self.var_entry = tk.StringVar()
        self.create_widget()

        self.is_china_var.set('1')

    def create_widget(self):
        self.frame = tk.Frame(root)
        self.frame.pack()
        tk.Label(self.frame,text='配置',font=(TrueType,18)).pack()

        self.frame.update()
        install_name_frame = tk.Frame(self.frame)
        install_name_frame.pack()

        tk.Label(install_name_frame,text='要卸载的包的名字：',font=(TrueType,13)).grid(row=0,column=0)
        tk.Entry(install_name_frame,textvariable=self.entry).grid(row=0,column=1)
        self.frame.update()

        frame2 = tk.Frame(self.frame)
        frame2.pack(side='bottom')
        tk.Button(frame2, text="开始", command=self.get_information, font=(TrueType, 18), width=6).grid(row=4, column=0, padx=10,pady=10)
        tk.Button(frame2, text="返回", command=self.exit, font=(TrueType, 18), width=6).grid(row=4, column=1, padx=10,pady=10)

    def get_information(self):
        self.uninstall_name=self.entry.get()

        if os.name == 'nt':
            self.start_for_windows()

        else:
            self.start_for_macos()

    def start_for_windows(self):
        print('由于pip限制，如果确认卸载，请在终端输入y，否则输入n！')
        self.command = run('pip uninstall ' + self.uninstall_name, shell=True, capture_output=True, text=True)

        with open('../log\\uninstall_log.log', 'w') as f:
            f.write(self.command.stdout+self.command.stderr)

        if 'Successfully uninstalled ' in self.command.stdout:
            msg.showinfo(title='pip-CH', message='卸载成功')

        if 'WARNING: Skipping' in self.command.stderr:
            msg.showinfo(message="该库已卸载或输入错误！")

        self.exit()

    def start_for_macos(self):
        print('由于pip限制，如果确认卸载，请在终端输入y，否则输入n！')
        self.command=run('pip3 uninstall '+self.uninstall_name,shell=True,capture_output=True,text=True)

        with open('../log\\uninstall_log.log', 'w') as f:
            f.write(self.command.stdout+self.command.stderr)

        if 'Successfully uninstalled ' in self.command.stdout:
            msg.showinfo(title='pip-CH',message='卸载成功')

        if 'WARNING: Skipping' in self.command.stderr:
            msg.showinfo(message="该库已卸载或输入错误！")

        self.exit()

    def exit(self):
        self.frame.destroy()
        MainFace()

if __name__ == '__main__':

    if os.name == 'nt':
        TrueType='SimSun'

    else:
        TrueType='Monaco'

    root=tk.Tk()
    root.title('pip-CH')
    root.geometry('600x350')
    MainFace()
    root.mainloop()