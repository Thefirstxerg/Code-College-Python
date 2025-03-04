from pathlib import Path
import json

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

path = Path("numbers.json")
with open(path, "w") as file: # w = write
    json.dump(number, file) # Dump is used to write the data to the file

with open(path, "r") as file: # r = read
    numbers = json.load(file) # Load is used to read the data from the file