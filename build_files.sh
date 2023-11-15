pip install virtualenv
virtualenv venv
source venv/bin/activate
sudo apt-get install sqlite3
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver