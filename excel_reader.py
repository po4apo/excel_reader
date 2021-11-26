import configparser
import subprocess

def download_package(name):
    mod_inst = subprocess.Popen(f"pip3  install {name}", shell=True)
    mod_inst.wait()

try:
    import pandas
except ModuleNotFoundError as e:
    download_package(e.name)
    download_package('openpyxl')
    import pandas


try:
    import smtplib
except ModuleNotFoundError as e:
    download_package(e.name)
    import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PATH_SETTINGS = 'settings.ini'


c = configparser.ConfigParser()
c.read(PATH_SETTINGS)

PASSWORD = c.get('email', 'PASSWORD')
ADDRESS = c.get('email', 'ADDRESS')
TO_ADDRESS = c.get('email', 'TO_ADDRESS')
SERVER = c.get('email', 'SERVER')


def send_email(message):
    try:
        # create message object instance
        msg = MIMEMultipart()

        # setup the parameters of the message
        password = PASSWORD
        msg['From'] = ADDRESS
        msg['To'] = TO_ADDRESS
        msg['Subject'] = 'Ошибка в приложениии для чтения excel'

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # create server
        server = smtplib.SMTP(SERVER)

        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)

        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()

        print(f"сообщение отправлено успешно:{msg['To']}")
    except Exception as e:
        print(f"Сообщение на почту не отправленно")
        print(f'Описание ошибки:\n{e}')


def read(path):
    try:
        data = pandas.read_excel(path)
    except FileNotFoundError as e:
        print('Файл не найден')
        send_email(f'Файл не найден\n Подробнее об ошибке:{e}')
    except ValueError as e:
        print('Скрипт работает только с файлами имеющими расширение .xlsx')
        send_email(f'Скрипт работает только с форматом .xlsx\n Подробнее об ошибке:{e}')
    except Exception as e:
        print(f'Не известная ошибка\n{e}')
        send_email(f'Не известная ошибка\n Подробнее об ошибке:{e}')
    else:
        if list(data):
            if list(data[list(data)[0]]):
                return data
            else:
                print('Файл не содержит строк')
                return data
        else:
            print('Файл пустой')
            return None



if __name__ == '__main__':
    path = input('Введите путь до файла:\n')
    print(read(path))