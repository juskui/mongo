# python -m pip install "pymongo[srv]"==3.11
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(
    override=True
)  # haetaan ensisijaisesti .env -tiedostosta, sitten vasta ympäristömuuttujista
user = os.getenv("USER")
pw = os.getenv("SS")


def connect():
    try:
        client = MongoClient(
            f"mongodb+srv://{user}:{pw}@cluster0.c2gyo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        )  ### LISÄÄ CONNECTION STRINGISI,
        ### HAE SALASANASI .env -TIEDOSTOSTA)
        print("connected to mongo")
        return client
    except:
        print("connection error")


def fetch_new_id(coll):
    ### FUNKTION TULEE PALAUTTAA UUSI id, JOTA KANNASSA EI VIELÄ OLE.
    ### MIKÄLI KANNASSA EI OLE YHTÄÄN DOKUMENTTIA, PALAUTETAAN 0.
    id_dict = coll.find_one(sort=[("id", -1)])  # -1 = desc, oletus asc
    max_id = int(id_dict["id"])
    if max_id is not None:
        new_id: int = int(max_id + 1)
        return int(new_id)
    else:
        return int(0)


def fetch_task_by_id(coll, task_id):
    ### FUNKTION TULEE HAKEA task_id -MUUTTUJAN PERUSTEELLA TIETOKANNASTA TASK, JONKA id ON task_id
    ### JA PALAUTTAA LÖYTYNYT TASK
    pass  # placeholder, (poista)


fetch_new_id(coll)
