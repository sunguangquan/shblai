import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
from tkinter.filedialog import askdirectory
from tkinter import filedialog
import zmail
import os







 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('发送邮件')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1024x700')  # 这里的乘是小x

var_usr_name = tk.StringVar()
var_usr_pwd = tk.StringVar()
var_usr_smtp = tk.StringVar()
var_usr_port = tk.StringVar()
var_usr_sub = tk.StringVar()
path = tk.StringVar()
filename = tk.StringVar()
text_usr_con = tk.Text(window, height = 10, font=('Arial', 14))

 
# 第5步，用户信息
tk.Label(window, text='邮箱:', font=('Arial', 14)).place(x=10, y=80)
tk.Label(window, text='密码:', font=('Arial', 14)).place(x=10, y=120)
tk.Label(window, text='Smtp服务器:', font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text='主题:', font=('Arial', 14)).place(x=10, y=220)
tk.Label(window, text='正文:', font=('Arial', 14)).place(x=10, y=270)
tk.Label(window, text='端口:', font=('Arial', 14)).place(x=400, y=170)
 
#变量


var_usr_name.set('info@shblai.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120,y=85)
# 用户密码

entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14))
entry_usr_pwd.place(x=120,y=125)


var_usr_smtp.set("smtp.qiye.163.com")
entry_usr_smtp = tk.Entry(window, textvariable=var_usr_smtp, font=('Arial', 14))
entry_usr_smtp.place(x=120,y=175)

var_usr_port.set(25)
entry_usr_smtp = tk.Entry(window, textvariable=var_usr_port, font=('Arial', 14))
entry_usr_smtp.place(x=520,y=175)


var_usr_sub.set("主题")
entry_usr_sub = tk.Entry(window, textvariable=var_usr_sub, font=('Arial', 14))
entry_usr_sub.place(x=120,y=225)




text_usr_con.place(x=120,y=275)

def select():
    paths = askdirectory()
    path.set(paths)





def SelectFile():
    files = filedialog.askopenfilename()
    filename.set(files)


# 第7步，login and sign up 按钮
btn_open = tk.Button(window, text='打开文件', command=SelectFile)
btn_open.place(x=20, y=30)
btn_select = tk.Button(window, text='选择附件', command=select)
btn_select.place(x=100, y=30)

def run():
    global text_usr_con
    global path
    data = [var_usr_name.get(),var_usr_pwd.get(),var_usr_smtp.get(),var_usr_port.get()]
    print(data)
    server = zmail.server(data[0],data[1],smtp_host=data[2],smtp_port=data[3],smtp_ssl=False)
    with open(filename.get(),'r',encoding="UTF8") as f:
        con = f.read()
        for i in con.split("\n")[1:]:
            i = i.split(",")
            os.chdir(os.path.join(path.get(),i[0]))
            print(len(i))
            mail = {
            "subject":var_usr_sub.get(),
            "content":text_usr_con.get('0.0',"end"),
            'attachments': os.listdir(os.path.join(path.get(),i[0]))
            }

            server.send_mail(i[1],cc=i[2:],mail=mail)


btn_run = tk.Button(window, text='启动', command=run)
btn_run.place(x=180, y=30)




# 第10步，主窗口循环显示
window.mainloop()