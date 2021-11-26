# Тестовые задания для сбербанка

## Задание 1. Чтение из excel файла

Разработан скрипт `excel_reader.py` для чтение информации из excel файла.
Ошибки в результате работы скрипта отправляются на почту.

Для работы скрипта нужен сам скрипт и файл `settings.ini`.

`settings.ini` нужно заполнить следующим образом:

* PASSWORD ='пароль электронной почты отправителя'
* ADDRESS = 'адрес электронной почты отправителя'
* TO_ADDRESS = 'адрес элетронной почты получателя'
* SERVER = smtp.gmail.com:587

Почта отправителя должна быть gmail.
Для корректной работы почты необходимо выставить разрешение на сайте:

```
https://support.google.com/accounts/answer/6010255
```

После чего нужно просто запустить скрипт.

## Задание 2. SQL-запросы