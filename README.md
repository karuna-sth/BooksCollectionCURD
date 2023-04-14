# BooksCollectionCURD
CURD operation using Django and Postgresql

## Installation
1. Clone the Repository <br>
```bash
https://github.com/karuna-sth/BooksCollectionCURD.git 
```
2. Navigate the directory
```bash
cd bookcollection
```
3. Create virtual environment and activate
```bash
py -m venv env
env/scripts/activate
```
4. Install requirements
```bash
pip install -r requirements.txt
```
5. Change Database infor in setting.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Books',
        'USER': 'YourUsername',
        'PASSWORD': 'YourPassword',
        'HOST': 'localhost',
    }
}
```
6. Make migration in database
```bash
python manage.py migrate
```
## Usage 
1. Start server
```bash
python manage.py runserver
```
2. open web browser and navigate to ``` http://127.0.0.1:8000/ ```

## Endpoints
- ``` / ``` : Show List of books from retrieved from database
- ``` /addbook ``` : Add new book to list
- ``` /deletebook/<id> ``` Delete an book by id and redirect to home page
- ``` /editbook/<id> ``` Update book details by id

## Screenshots

![home](https://user-images.githubusercontent.com/47665883/231962537-d016c7b2-3eb5-4ddb-af6d-6b2d13cefa9e.png)
![addbook](https://user-images.githubusercontent.com/47665883/231962550-98f046d4-97e6-4c32-9030-e57340f69093.png)
![editbook](https://user-images.githubusercontent.com/47665883/231962559-86b13572-9160-4539-96b0-d8c58ac97e75.png)




