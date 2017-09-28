# Go to https://github.com/feykmeelyahoo/dockeransibletodobackend for virtual env installation

python3 -m venv MyDjangoEnv

. MyDjangoEnv/bin/activate
pip install --upgrade pip
pip install django
django-admin startproject first_project
python manage.py startapp first_app

python manage.py migrate
python manage.py makemigrations first_app
python manage.py migrate

# After creating models and admin.py
python manage.py createsuperuser

# Enter http://127.0.0.1:8000/admin
# Write populate.py to populate db
pip install faker
python populate.py

pip freeze > stable-req.txt
pip install -r stable-req.txt
