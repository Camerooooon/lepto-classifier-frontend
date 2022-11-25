from result import Result;
import time

import sqlite3

class DogEntry:
    def __init__(self, result: Result, data):
        self.result = result;
        self.data = data;
        self.timestamp = int(time.time());
        self.id = None;

def con_database():
    return sqlite3.connect("dogs.db");

def init_database(cur):
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS dogs (id INT PRIMARY_KEY NOT_NULL AUTO_INCREMENT, dog_name TEXT)")
    except sqlite3.OperationalError:
        print("Operational error when generating table 'dogs'");

def put_dog_entry(con, cur, dog_entry: DogEntry):
    cur.execute("INSERT INTO dogs VALUES(?, ?)", ("1", "2"));
    con.commit();
