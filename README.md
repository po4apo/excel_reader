# Тестовые задания для сбербанка

Задача 1. Чтение из excel файла

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

## Задача 2. SQL-запросы

### Задание:

Есть две таблицы:

* students – список студентов, поля: name (имя студента), group (группа), passed (признак успешного прохождения экзаменов).
* exams – результаты экзамена, поля: name (имя студента), exam (предмет), score (оценка), year (год), period (период).

Напишите SQL-запрос:

a) Который выставляет passed = 1 всем студентам 2-ой и 3-ей группы, у которых сумма баллов по всем экзаменам больше 36.

b) Который выводит количество отличников и хорошистов в каждой группе по каждому предмету за 2-ой период 2021 года.

c) Который выводит список итоговых оценок студентов по предметам (итоговая оценка – последняя оценка по предмету).


В процессе решения задания я принял решение заменить поле exams.name на exams.student_id. Так как в простивном случае имена у всех студентов должны были бы быть уникальными.

Созданные мной запросы находятся в файле `task2.txt`
