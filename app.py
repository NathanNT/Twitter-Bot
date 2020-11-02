import tweepy
import time
import csv
import numpy as np
import gspread
import json
import ast
import pandas as pd
from colorama import init
from termcolor import colored

def launch_tweepy():
    print("main lancé... ")
    auth = tweepy.OAuthHandler("PRIVATE", "PRIVATE")
    auth.set_access_token("PRIVATE", "PRIVATE")
    api = tweepy.API(auth)

def launch_gsh():
    print("Google sheets lancé... ")
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_key('PRIVATE')
    ws = sh.sheet1
    rs = ws.col_values(1)
    speed1 = int(ws.get('B2')[0][0])
    speed2 = int(ws.get('C2')[0][0])


def add(write):
    with open('db.csv','a') as fd:
        fd.write("\n"+write + "\n")

def detec(read):
    with open('db.csv', 'rt') as f:
        true = 0
        reader = csv.reader(f, delimiter=',') # good point by @paco
        for row in reader:
            for field in row:
                if field == read:
                    true = 1
    return true


def give_original(id):
    return api.get_status(id).retweeted_status.id_str

def bot_content():
    print("main lancé... ")
    auth = tweepy.OAuthHandler("PRIVATE", "PRIVATE")
    auth.set_access_token("PRIVATE", "PRIVATE")
    api = tweepy.API(auth)
    print("Autentification avec succes...")
    while 1 != 0:
        print("Google sheets lancé... ")
        gc = gspread.service_account(filename='credentials.json')
        sh = gc.open_by_key('1LUq1dJFlGigosmw_-wTdg73oZ-eJTDcYwau5TO77N70')
        ws = sh.sheet1
        rs = ws.col_values(1)
        speed1 = int(ws.get('B2')[0][0])
        speed2 = int(ws.get('C2')[0][0])
        for index in range(1, len(rs)):
            aunt = api.search(q=rs[index] + " -filter:retweets",lang ='fr', count=10, result_type= 'recent')
            id = str(aunt[0].id)
            if detec(str(id)) == 1:
                print("Tweet d'id : " + str(aunt[0].id) + ", sujet : " + rs[index] +", aperçu : " + str(aunt[0].text)[0:12] + "..." +  colored('[Deja RT]', 'red'))
            else:
                print("Tweet d'id : " + str(aunt[0].id) + ", sujet : " + rs[index] +", aperçu : " + str(aunt[0].text)[0:12] + "..." + colored('[RT avec succes]', 'green') )
                api.retweet(id)
                add(id)
            time.sleep(speed1)
        print("Attente" + speed2 + "secondes...")
        time.sleep(speed2)



def main():
    auth = tweepy.OAuthHandler("PRIVATE", "PRIVATE")
    auth.set_access_token("PRIVATE", "PRIVATE")
    api = tweepy.API(auth)
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_key('PRIVATE-PRIVATE-PRIVATE')
    ws = sh.sheet1
    nigga = api.rate_limit_status()
    val = ast.literal_eval(nigga)
    val1 = json.loads(json.dumps(val))
    val2 = val1['tags'][0]['results'][0]['values']
    print pd.DataFrame(val2)


while True:
    try:
        main()
    except Exception as e:
        print(e)
        time.sleep(30)
        print('Restarting !!!')
        continue
    break
