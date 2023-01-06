import os
import requests
from bs4 import BeautifulSoup
from json2excel import Json2Excel


def third_query():
    counter = 1
    flag = 0  # 1 -> name of game , 2 -> users amount
    URL = "https://steamcharts.com/top"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    myarr = []
    current_data = ""
    for game in soup.find_all('td'):
        # Obtain the text from the received
        # tags
        current_data = game.get_text().strip()
        if (counter % 2) == 0 and flag == 0:
            flag = 1
            myarr.append(current_data)
        if (counter % 3) == 0 and flag == 1:
            flag = 2
            myarr.append(current_data)
        counter = counter + 1
        if counter == 7:
            counter = 1
            flag = 0

    secCounter = 0
    res = []
    for index in range(25):
        title = myarr[secCounter]
        amount = myarr[secCounter + 1]
        next_game_for_res = {
             "Name": title,
             "Amount": amount,
        }
        res.append(next_game_for_res)
        secCounter = secCounter + 2

    json2excel = Json2Excel(head_name_cols=["Name","Amount"],export_dir='Output_Files')
    path = json2excel.run(res)
    os.rename(path, "Output_Files/ThirdQuery.xls")