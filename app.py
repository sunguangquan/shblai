from flask import Flask , render_template, request
from sendmail import testServer,GetCsv,SendMail
import json
import chardet
import re
import zmail
app = Flask(__name__)
'''
调试真是要人命，下次一定要一个模块一个模块的测试它们。真是无语的很
'''


servers = {"mail":"sunmanlyh@126.com","passwd":"Sandisk611027","host":"smtp.126.com","port":465}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send",methods = ['GET','POST'])
def send():
    if request.method == "GET":
        username = servers.get("mail")
        return render_template("send.html",username=username)
    if request.method == "POST":
        content = GetCsv(request.files.get("file"))
        sub = request.form.get("sub")
        html = request.form.get("editor1")
        server = zmail.server(servers.get("mail"),servers.get("passwd"),servers.get("host"),servers.get("port"))
        SendMail(server,content,sub,html)
        return "发送成功！"

        

@app.route("/testsv",methods = ['GET','POST'])
def testsv():
    if request.method == "POST":
        servers["mail"] = request.form.get("mail")
        servers["passwd"] = request.form.get("passwd")
        servers["host"] = request.form.get("host")
        servers["port"] = request.form.get("port")
        server = testServer(servers.get("mail"),servers.get("passwd"),servers.get("host"),servers.get("port")) 
        if server:
            return "服务器测试成功"
        else:
            return "服务器测试失败,请重新填写"                
    else:
        print("没有Post")





if __name__ == "__main__":
    app.run(debug=True)
