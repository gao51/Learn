# -*-coding:UTF-8-*-
# _author_= 'gao'


import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import threading

import xlrd

import readConfig as readConfig
from common.Common import gethtml
from common.Log import MyLog as Log
from common.Log import MyLog
import zipfile
import glob

localReadConfig = readConfig.ReadConfig()
def addimg(src, imgid):  # 文件路径、图片id
    fp = open(src, 'rb')  # 打开文件
    msgImage = MIMEImage(fp.read())  # 读入 msgImage 中
    fp.close()  # 关闭文件
    msgImage.add_header('Content-ID', imgid)
    return msgImage


def get_result_value(path):
    x = []
    ExcelFile = xlrd.open_workbook(path)
    sheet = ExcelFile.sheet_by_name('测试总况')
    x.append(str(int(sheet.cell_value(2, 4))))
    x.append(str(int(sheet.cell_value(3, 4))))
    x.append(str(int(sheet.cell_value(4, 4))))
    x.append(sheet.cell_value(5, 4))
    x.append(sheet.cell_value(3, 5))
    return x
class Email:
    def __init__(self):
        global host, user, password, port, sender, title, content,reportPath,logger
        log = Log.get_log()
        reportPath = log.get_report_path_excel()
        host = localReadConfig.get_email("mail_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_pass")
        port = localReadConfig.get_email("mail_port")
        sender = localReadConfig.get_email("sender")
        title = localReadConfig.get_email("subject")

        self.value = localReadConfig.get_email("receiver")
        self.receiver = []
        # get receiver list
        for n in str(self.value).split(","):
            self.receiver.append(n)
        # defined email subject

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = title + " " + date
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.msg = MIMEMultipart('mixed')

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        res = get_result_value(reportPath)
        content = gethtml().replace("_total",res[0])
        content = content.replace("_pass_t", res[1])
        content = content.replace("_fail_t", res[2])
        content = content.replace("_date", res[3])
        content = content.replace("_pass_rate", res[4])
        content_plain = MIMEText(content, 'html', 'utf-8')
        self.msg.attach(content_plain)
        self.msg.attach(addimg("G:\\code\\Tpython\\learn\\Logo.png", "logo"))

    def config_file(self):
        # if the file content is not null, then config the email file
        if self.check_file():

            reportpath = self.log.get_result_path()
            name = reportpath.split("\\")[-1]+".zip"
            #print(name)
            zippath = os.path.join(readConfig.proDir, "result", name)
            #print(zippath)
            # zip file
            files = glob.glob(reportpath + '\*')

            f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
            for file in files:
                f.write(file)
            f.close()

            reportfile = open(zippath, 'rb').read()
            filehtml = MIMEText(reportfile, 'base64', 'utf-8')
            filehtml['Content-Type'] = 'application/octet-stream'
            filehtml['Content-Disposition'] = 'attachment; filename='+name
            self.msg.attach(filehtml)

            reportfile1 = open(reportPath, 'rb').read()
            filehtml1 = MIMEText(reportfile1, 'base64', 'utf-8')
            filehtml1['Content-Type'] = 'application/octet-stream'
            filehtml1['Content-Disposition'] = 'attachment; filename=report.xlsx'
            self.msg.attach(filehtml1)

    def check_file(self):
        reportpath = self.log.get_report_path()
        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            return False

    def send_email(self):
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            # smtp = smtplib.SMTP()
            smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
            # smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
            self.logger.info("The test report has send to developer by email.")
            print("\nEmail has been send")
        except Exception as ex:
            print("Email send failed")
            self.logger.error(str(ex))


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == "__main__":
    Email = Email()
    Email.send_email()
    print(bool)
