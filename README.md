# test

To execute on local machine, first run the following commands :

```cmd
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
flask db migrate
flask db upgrade
```

Then create user roles on flask shell :

```cmd
flask shell
```

```py
from app.models import *
role = Role(name="admin")
db.session.add(role)
db.session.commit()
role = Role(name="client")
db.session.add(role)
db.session.commit()
exit()
```

Then run the app : ```flask run``` or ```py main.py```
