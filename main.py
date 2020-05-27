from flask import (Flask,
    render_template,
    Config,
    redirect,
    _app_ctx_stack,
    url_for,
    session,
    request,)

import json
import sqlite3

DB_NAME = "Forum.db"


def create_database(con):
    for file in ["Uzytkownik.sql", "Kategoria.sql", "Watek.sql", "Post.sql"]:
        with open(f"Templates/sql/{file}") as f:
            print(file)
            database = f.read()
            con.execute(database)


def insert_init_values(con):
    inserts = [
        # "insert into Adres values(null, 1, 1, 'Dluga', 'Gdansk', 'Pomorskie')",
        # "insert into Adres values(null, 2, 2, 'Szeroka', 'Gdansk', 'Pomorskie')",
        # "insert into Adres values(null, 3, 3, 'Wojska Polskiego', 'Gdansk', 'Pomorskie')",
        # "insert into Osoba values(null, 'Andrzej', 'Kowalski', 1)",
        # "insert into Osoba values(null, 'Ania', 'Kowalska', 1)",
        # "insert into Osoba values(null, 'Grzegorz', 'Nowak', 2)",
        # "insert into Produkt values(null, 'Intel core i7-9700K', 1600, 0.23)",
        # "insert into Produkt values(null, 'Intel core i7-9900K', 2200, 0.23)",
        # "insert into Uzytkownik values (null, 'temp', 'temp123', 'Manager', 1)",
        # "insert into Uzytkownik values (null, 'Klient', 'temp123', 'Klient', 1)",
        # "insert into Uzytkownik values (null, 'S', 'temp123', 'Sprzedawca', 1)",
    ]
    for insert in inserts:
        con.execute(insert)
    con.commit()


def get_db():
    db = getattr(_app_ctx_stack, "_database", None)
    if db is None:
        db = _app_ctx_stack._database = sqlite3.connect(
            DB_NAME,check_same_thread=False
        )
    return db
app = Flask(__name__)
app.config.from_object(Config)
con = sqlite3.connect(DB_NAME, check_same_thread=False)
create_database(con)
# insert_init_values(con)

app.config.from_object(Config)
secret_key = "nencatokurwa"
app.config["SECRET_KEY"] = secret_key
app.secret_key = secret_key


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
