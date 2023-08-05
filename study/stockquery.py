from sqlalchemy import select,insert
import mysql.connector
import pymysql
from sqlalchemy import create_engine,text

import os.path
import json

from fastapi import FastAPI

from stock import result as R

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME=get_secret("Mysql_Hostname")
PORT=get_secret("Mysql_Port")
USERNAME=get_secret("Mysql_Username")
PASSWORD=get_secret("Mysql_Password")
DBNAME=get_secret("Mysql_DBname")

engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}')

#api
app=FastAPI()

def Selectfs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from stock"))
        resultDict = []
        for row in result:
            resultDict.append({"Code" : row.Code, "Name":row.Name, "MarketId" : row.MarketId, "Dept" : row.Dept, "Close": row.Close})
        print(resultDict)
    return resultDict

@app.get('/selectall')
async def selectall():
    result = Selectfs()
    return result

