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
    return sqlite3.connect("dogs.db", check_same_thread=False);

def init_database(cur):
    cur.execute('''
                CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                dog_name TEXT,
                owner_name TEXT,
                weight FLOAT(3),
                breed_group TEXT,
                mat FLOAT(3),
                anion_gap FLOAT(3),
                sodium FLOAT(3),
                potassium FLOAT(3),
                chloride FLOAT(3),
                bicarb FLOAT(3),
                phosphorus FLOAT(3),
                calcium FLOAT(3),
                bun FLOAT(3),
                creatine FLOAT(3),
                glucose INT,
                protein INT,
                albumin FLOAT(3),
                globulin FLOAT(3),
                alt FLOAT(3),
                ast FLOAT(3),
                alp FLOAT(3),
                ggt FLOAT(3),
                cholesterol FLOAT(3),
                bilirubin FLOAT(3),
                urine_specific_gravity FLOAT(5),
                hct FLOAT(3),
                hgb FLOAT(3),
                mcv FLOAT(3),
                wbc FLOAT(3),
                bands FLOAT(3),
                neut FLOAT(3),
                lymph FLOAT(3),
                mono FLOAT(3),
                eosin FLOAT(3),
                plt FLOAT(3)
                )''')

def put_dog_entry(con, cur, dog_entry: DogEntry):
    cur.execute("INSERT INTO dogs(dog_name, owner_name, weight) VALUES(?, ?, ?)", (dog_entry.data["dog name"], dog_entry.data["owner name"], dog_entry.data["Weight"]));
    con.commit();
