import json
import pandas as pd
from files import CSV_FILE_PATH, JSON_FILE_PATH 




with(JSON_FILE_PATH, "r") as f:
    user_dict = json.load(f)

#Парсим csv, убираем лишнюю колонку (drop) превращаем DataFrame в dict(records - формат словаря)
books_dict = pd.read_csv(CSV_FILE_PATH, header=0).drop(columns=["Publisher"]).to_dict("records")

#print(user_dict(list))  #!!!!!!!!!!!!!
#Создаём список (list) применяем ко всему списку(map)
user_dict = list(map(lambda el:
{
    "name": el["name"], "gender":["gender"],"address":["address"], "age":["age"],
    "books":[]
},
user_dict)
)

#создаём 2 счётчика i -для книг, j- для юзеров
i,j = 0,0
# бежим по всем юзерам и добавляем по одной книге пока они не закончатся   
# т.е целиком получается по 7 книг каждому пользователю и еще 15 книг добавляем с начала списка юзеров
while i < len(user_dict):
    user_dict[j]["books"]+= books_dict[i:i+1]
    j = j+1 if j < len(user_dict)-1 else 0
    i += 1
# Сохряняем результаты в  result.json и приводим к формату 4 (indent=4)
with open("result.json","w") as f:
    json.dump(user_dict, f,indent=4)
