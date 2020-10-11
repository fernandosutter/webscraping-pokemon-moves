#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup

url = 'https://pokemondb.net/move/all'

req = requests.get(url)

if req.status_code == 200:
    print('Requisição feita com sucesso!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')

table = soup.find(name='table', attrs={'id':'moves'})

data = table.find(name='tbody')

moves = data.find_all('tr')

list = []

for move in moves:
    
    row = move.find_all('td')
    
    move_name = row[0].get_text()
    type = row[1].get_text()
    if row[2].get_text() != '—':
        category = row[2].span["title"]
    else:
        category = row[2].get_text()
    power = row[3].get_text()
    accuracy = row[4].get_text()
    pp = row[5].get_text()
    tm = row[6].get_text()
    effect = row[7].get_text()
    prob = row[8].get_text()
    list.append({'move_name': move_name,'type':type, 'category':category, 'power':power,'accuracy':accuracy, 'pp':pp, 'tm':tm, 'effect':effect,'prob':prob})

with open('pokemon_moves.json', 'w') as json_file:
    json.dump(list, json_file, indent=2, ensure_ascii=False)