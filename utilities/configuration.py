import configparser

import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

connect_config = {
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database']
}

def getConnection():
    try:
        conn = mysql.connector.connect( **connect_config)
        if conn.is_connected():
            print("Connection successful")
            return conn
    except Error as e:
        print(e)

def getQuery(query):

    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

# authentication

def getPassword():
    return "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"

