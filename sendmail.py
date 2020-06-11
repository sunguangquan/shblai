import zmail
import os
import chardet
from datetime import datetime
import re


def testServer(mail, passwd, smtp, port):
    if port == "25":
        server = zmail.server(mail, passwd, smtp, port, smtp_ssl=False)
    elif port == "465":
        server = zmail.server(mail, passwd, smtp, port, smtp_ssl=True)
    if server.smtp_able():
        return server
    else:
        return False


def GetCsv(f):
    if f != "":
        con = f.read()
        r = chardet.detect(con)
        con = con.decode(r.get('encoding'))
        con = con.split("\n")
        content = con[1:]
        print(content)
        return content
    else:
        return False


def SendMail(server, content, sub, html):
    for i in content:
        i = i.split(",")
        print("打印I的值：%s"%i)
        if len(i) >= 2:
            if len(i[2:]) < 1:
                mail = {
                    "subject": sub,
                    "content_html": html
                }
                server.send_mail(i[1], mail)
            else:
                cc = [c for c in i[2:] if re.match(r'\S', c)]
                mail = {
                    "subject": sub,
                    "content_html": html
                }
                server.send_mail(i[1],mail,cc = cc)
