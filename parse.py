import os
from bs4 import BeautifulSoup
import time

chapters = [
    "Prologue", "Forsaken City", "Old Site", "Celestial Resort",
    "Golden Ridge", "Mirror Temple", "Reflection", "The Summit", "Epilogue",
    "Core", "Farewell"
]
modes = {"Normal": "A-Side", "BSide": "B-Side", "CSide": "C-Side"}
start_time = int(time.time())

save_file_path = os.path.join(os.environ["XDG_DATA_HOME"], "Celeste", "Saves",
                              "0.celeste")


def get_soup():
    with open(save_file_path, "r") as save_file:
        soup = BeautifulSoup(save_file, "xml")
    save_file.close()
    return soup


def get_chapter(soup):
    area_id = soup.find("LastArea").get("ID")
    return chapters[int(area_id)]

def get_mode(soup):
    mode = soup.find("LastArea").get("Mode")
    return modes[mode]

def get_time(soup):
    return start_time

def get_stats(soup):
    deaths = soup.find("TotalDeaths").get_text()
    strawberries = soup.find("TotalStrawberries").get_text()
    golden_strawberries = soup.find("TotalGoldenStrawberries").get_text()
    return deaths + " deaths and " + strawberries + " strawberries"

