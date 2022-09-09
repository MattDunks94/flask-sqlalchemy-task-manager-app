# pip3 install Flask-SQLAlchemy
# pip3 install psycopg2
# set_pg
# psql
# CREATE DATABASE taskmanager;

import os
from taskmanager import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )