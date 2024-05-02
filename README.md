# flask-restful-project-starter-code
My starter code for creating a new project

Console commands!

For setup
- `pipenv install && pipenv shell`


In the server folder if you want to use 'flask run':
- `export FLASK_APP=app.py`
- `export FLASK_RUN_PORT=3000`
- `export FLASK_DEBUG=1`

Or you can just run app.py to start the server! ^_^

To create your database after working on your models
- `flask db init` ( to create initial db setup )

- `flask db revision --autogenerate -m 'message here!'` ( creates a db migration )
- `flask db upgrade head`

