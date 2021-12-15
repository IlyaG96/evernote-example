# Evernote example
Cервис для работы с api evernote

## Установка
Вам понадобится установленный Python 3.9 и git

Склонируйте репозиторий
```bash
$ git clone git@github.com:IlyaG96/evernote-example.git
```

Создайте в этой папке виртуальное окружение
```bash
$ python3 -m venv [полный путь до папки evernote-example]
```

Активируйте виртуальное окружение и установите зависимости
```bash
$ cd evernote-example
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Получение токенов 

```bash
EVERNOTE_CONSUMER_KEY="username"
EVERNOTE_CONSUMER_SECRET="123usernamesecret123"
EVERNOTE_PERSONAL_TOKEN="bigstringA=username:anotherbigstring"

JOURNAL_TEMPLATE_NOTE_GUID="somedigitsandsymbols"
JOURNAL_NOTEBOOK_GUID="somedigitsandsymbols"
INBOX_NOTEBOOK_GUID="somedigitsandsymbols"
```
- EVERNOTE_CONSUMER_KEY - получить можно [Здесь](https://dev.evernote.com/doc/) 
- EVERNOTE_CONSUMER_SECRET - получить можно [Здесь](https://dev.evernote.com/doc/)
- EVERNOTE_PERSONAL_TOKEN - получить можно [Здесь](https://dev.evernote.com/get-token/)
- JOURNAL_NOTEBOOK_GUID - можно узнать так:
```bash
$ python list_notebooks.py
```
- JOURNAL_TEMPLATE_NOTE_GUID заметки-шаблона можно "вытащить из" ссылки на заметку, скопировав ее в интерфейсе evernote
```text
https://www.evernote.com/shard/.../guid_заметки_лежит_тут_?...
```
- INBOX_NOTEBOOK_GUID - GUID блокнота, который используется как ящик для входящих сообщений

## Использование

### add_note2journal.py

Создает заметки на основе заметки-шаблона JOURNAL_TEMPLATE_NOTE_GUID. 
Заметки будут создаваться в блокноте JOURNAL_NOTEBOOK_GUID.

Заголовок и содеержимое заметки остаются неизменными, 
но можно использовать следующие значения:

- `date` - заменяется на дату в формате ISO
- `dow` - заменяется на русскоязычное наименование дня недели
Если не указывать никакие аргументы, то время будет определяться системой. 
- Дату также можно задать вручную
```bash
$ bin/python add_note2journal.py 2021-11-11
```
Важно то, что дата должна быть задана в формате ГГГГ-ММ-ДД

Результатом работы скрипта будет выведенное название заметки.

### list_notebooks.py

Находясь в директории evernote-example выполните команду
```bash
$ python list_notebooks.py
```
Вы увидите список ваших записных книжек и их GUID

### dump_inbox.py

Выводит в консоль содержимое блокнота c INBOX_NOTEBOOK_GUID, это - ящик для входящих сообщений.
Их количество можно регулировать аргументом:
```bash
$ bin/python dump_inbox.py 3
```
В консоль будут выведено не более, чем 3 заметки.



