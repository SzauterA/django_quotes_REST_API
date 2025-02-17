It's a Django REST API app to provide random historical quotes for the user. It has a JS frontend to display dynamically, the quotes are stored in
a PostgreSQL db.

Setup:
1 - clone the repository
2 - create and activate virtual enviroment: python -m venv venv
3 - install dependencies: pip install -r requirments.txt
4 - create a .env file in the root directory:
    DB_HOST=your_db_host
    DB_NAME=your_db_name
    DB_USER=your_db_username
    DB_PASSWORD=your_password

    example for local use:
    DB_HOST=localhost
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASSWORD=your_password
5 - set up the database:
    python manage.py makemigrations
    python manage.py migrate
6 - import quotes into the db:
    python manage.py import quotes
7 - create teh superuser:
    python manage.py createsuperuser
8 - run the server:
    python manage.py runserver

API available at: http://127.0.0.1:8000/api/quote/

Frontend available: click the 'index.html' file in the 'frontend/' folder (it's static, must be opened manually)

Make sure PostgreSQL is installed and working locally.
API is CORS-enabled for frontend acces.










