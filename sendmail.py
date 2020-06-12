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
        return content
    else:
        return False


def SendMail(server, content, sub, html,att):
    for i in content:
        i = i.split(",")
        paths = os.path.abspath(os.path.join("c:\\upload\\att",i[0]).lower())
        satt = att.get(paths,[])
        print(satt)
        if len(i) >= 2:
            if len(i[2:]) < 1 and len(satt) == 0:
                mail = {
                    "subject": sub,
                    "content_html": html
                }
                server.send_mail(i[1], mail)
            elif len(i[2:]) < 1 and len(satt) > 0:
                mail = {
                    "subject": sub,
                    "content_html": html,
                    'attachments': satt
                }
                server.send_mail(i[1], mail)
            elif len(i[2:]) > 1 and len(satt) == 0:
                cc = [c for c in i[2:] if re.match(r'\S', c)]
                mail = {
                    "subject": sub,
                    "content_html": html
                }
                server.send_mail(i[1],mail,cc = cc)
            else:
                cc = [c for c in i[2:] if re.match(r'\S', c)]
                print(satt)
                mail = {
                    "subject": sub,
                    "content_html": html,
                    'attachments': satt
                }
                server.send_mail(i[1],mail,cc = cc)
