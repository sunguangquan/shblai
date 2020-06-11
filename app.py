from flask import Flask , render_template, request
from sendmail import testServer,GetCsv,SendMail
import json
import chardet
import re
app = Flask(__name__)


servers = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send",methods = ['GET','POST'])
def send():
    username = []
    with open("mailserver",'r') as mailserver:
        js = json.loads(mailserver.read())
        print(js)
        return js
        

    if request.method == "POST":
        content = GetCsv(request.files.get("file"))
        if content:
            return render_template("send.html",username=username,content=content)

@app.route("/testsv",methods = ['GET','POST'])
def testsv():
    if request.method == "POST":
        servers["mail"] = request.form.get("mail")
        servers["passwd"] = request.form.get("passwd")
        servers["host"] = request.form.get("host")
        servers["port"] = request.form.get("port")
        server = testServer(servers.get("mail"),servers.get("passwd"),servers.get("host"),servers.get("port")) 
        if server:
            with open("mailserver",'a') as mails:
                js = json.dumps(servers)
                mails.write(js)
                mails.write("\n")
            return "服务器测试成功"
        else:
            return "服务器测试失败,请重新填写"                
    else:
        print("没有Post")





if __name__ == "__main__":
    app.run(debug=True)
