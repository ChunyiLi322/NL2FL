# NL2FL web

## About

This is a demo project for natural language to logical language. The project is in /nl2flweb.

It was made using  **Anaconda3**  + **Python** + **Django** and database is **SQLite**.
**Bootstrap** was used for styling.

Install dependencies:
```bash
$ pip install -r requirements.txt
```
or
```bash
conda create -n NL2LTL python==3.8
conda activate NL2LTL
pip install -r requirements.txt
pip install pytz==2022.6
pip install django-bootstrap3
pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install urllib3==1.25.11
pip install -U django-cloudflare
pip install matplotlib
```

## How to run

### Default

You can run the application from the command line with manage.py.
Go to the root folder of the application.

First, run migrations:
```bash
$ python manage.py migrate
```
Then, run server on port 8000:
```bash
$ python manage.py runserver 8000
```

## Post Installation

Go to the web browser and visit `http://localhost:8000/hello`

### Others
Unzip the **node_modules.zip** file to the current file. This file is a third-party library, which has many files that are difficult to upload.
```
/nl2flweb/mysite/blog/static/blog/js/node_modules.zip  
```



