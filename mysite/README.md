Run in Bash:


!!! За наявності VENV з інстальованими бібліотеками Django налаштування починати з п.5.

1.
python -m venv fccenv

2.
source fccenv/Scripts/activate  

3.
pip install Django

4.
python manage.py makemigrations faculty



!!! За наявності VENV з інстальованими бібліотеками Django налаштування починати з п.5.
5.
python manage.py migrate

6.
python manage.py createsuperuser

7
python manage.py runserver


Site: http://127.0.0.1:8000/
Admin board: http://127.0.0.1:8000/admin/
(enter with login&password from step 6)
