from pickle import UNICODE
import sys
import psycopg2
from psycopg2 import connect
from psycopg2.extras import DictConnection
from configparser import ConfigParser


class dbConnection:
    # wczytanie danych
    def __init__(self, filename="database.ini", section="postgresql"):
        self.parser = ConfigParser()
        self.parser.read(filename)
        self.db = {}
        
        if self.parser.has_section(section):
            self.params = self.parser.items(section)
            for param in self.params:
                self.db[param[0]] = param[1]
        else:
            raise Exception(f"Section {section} not found in file {filename}")

    # ustanowienie połączenia
    def connect(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(host = self.db['host'],
                                         database=self.db['database'],
                                         user=self.db['user'],
                                         password=self.db['password']
                                         )
            print("połączono...")
        except (Exception, psycopg2.DatabaseError) as err:
            print(f"Database connection error: {err}")
     
   
    # zamykanie połączenia
    def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()
        self.conn = None
        
    # zatwierdzenie zmian
    def commit(self):
        self.conn.commit()
        
    
    # cofanie zmian
    def rollback(self):
        self.conn.rollback()
        
    
    # wykonanie zapytania
    def execute(self, query, args=None):
        if self.conn is None or self.conn.closed:
            self.connect()
        curs = self.conn.cursor()
        try:
            curs.execute(query, args)
        except Exception as ex:
            self.conn.rollback()
            curs.close()
            raise ex
        return curs   
        
    # rekord
    def fetchone(self, query, args=None):
        curs = self.execute(query, args)
        row = curs.fetchone()
        curs.close()
        return row
    
     # rekordy
    def fetchall(self, query, args=None):
        curs = self.execute(query, args)
        rows = curs.fetchall()
        curs.close()
        return rows
    
    
    
    
        
    
    
        
        