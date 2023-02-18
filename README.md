# test

To execute on local machine :

```cmd
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
flask db migrate
flask db upgrade
flask run
```

To deploy on pythonanywhere :

- Login to pythonanywhere account
- Create Bach and clone the repo
- Then run the following commands :

```cmd
mv test mysite
mkvirtualenv myvirtualenv --python=/usr/bin/python3.10
workon myvirtualenv
cd mysite
pip install -r requirements.txt
```
