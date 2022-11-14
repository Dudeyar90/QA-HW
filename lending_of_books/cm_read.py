from files import CSV_FILE_PATH

with open(CSV_FILE_PATH, "r") as file:
    print(file.read())