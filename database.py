from result import Result;
import time

import sqlite3

class DogEntry:
    def __init__(self, result: Result, temp_link: str, data):
        self.result = result;
        self.temp_link = temp_link;
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
                zip_code INT,
                vet_name TEXT,
                email_address TEXT,
                temp_link TEXT,
                weight FLOAT(3),
                breed_group TEXT,
                sex INT,
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
    cur.execute('''CREATE TABLE IF NOT EXISTS contact ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, message TEXT )''');

def put_dog_entry(con, cur, dog_entry: DogEntry):
    cur.execute("INSERT INTO dogs(dog_name, owner_name, zip_code, vet_name, email_address, temp_link, weight, breed_group, sex, mat, anion_gap, sodium, potassium, chloride, bicarb, phosphorus, calcium, bun, creatine, glucose, protein, albumin, globulin, alt, ast, alp, ggt, cholesterol, bilirubin, urine_specific_gravity, hct, hgb, mcv, wbc, bands, neut, lymph, mono, eosin, plt) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dog_entry.data["dog name"], dog_entry.data["owner name"], dog_entry.data["zip code"], dog_entry.data["vet name"], dog_entry.data["email address"], dog_entry.temp_link, dog_entry.data["Weight"], dog_entry.data["Breed Group"], dog_entry.data["Sex"], dog_entry.data["MAT"], dog_entry.data["Anion Gap"], dog_entry.data["Sodium"], dog_entry.data["Potassium"], dog_entry.data["Chloride"], dog_entry.data["Bicarb"], dog_entry.data["Phosphorus"], dog_entry.data["Calcium"], dog_entry.data["BUN"], dog_entry.data["Creatinine"], dog_entry.data["Glucose"], dog_entry.data["Total Protein"], dog_entry.data["Albumin"], dog_entry.data["Globulin"], dog_entry.data["ALT"], dog_entry.data["AST"], dog_entry.data["ALP"], dog_entry.data["GGT"], dog_entry.data["Cholesterol"], dog_entry.data["Bilirubin"], dog_entry.data["Urine Specific Gravity"], dog_entry.data["Urine Protein"], dog_entry.data["Urine Glucose"], dog_entry.data["Hct"], dog_entry.data["Hgb"], dog_entry.data["MCV"], dog_entry.data["WBC"], dog_entry.data["Bands"], dog_entry.data["Neut"], dog_entry.data["Eosin"], dog_entry.data["Plt"]));
    con.commit();

def get_dog_by_names(con, cur, dog_name, owner_name):

    database_dog = cur.execute("SELECT * FROM dogs WHERE dog_name=?", (dog_name,)).fetchone();
    return DogEntry(Result.NEGATIVE, database_dog["temp_link"], database_dog);

def put_contact_message(con, cur, name: str, email: str, message: str):
    cur.execute("INSERT INTO contact(name, email, message) VALUES(?, ?, ?)", (name, email, message));
    con.commit();
