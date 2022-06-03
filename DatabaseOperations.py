import sqlite3 as sl

class DatabaseOperations:
    def __init__(self):
        try:
            self.rebusDb = sl.connect("DATA/rebusDatabase.db")
        except self.rebusDb.Error as e:
            print(e)

    def createTable(self):
        try:
            cs = self.rebusDb.cursor()
            cs.execute("create table Images ('id' INTEGER, 'path' TEXT NOT NULL, 'text' TEXT NOT NULL, PRIMARY KEY('id' AUTOINCREMENT))")
            self.rebusDb.commit()
        except self.rebusDb.Error as e:
            print(e)

    def insert(self, path, text):
        try:
            cs = self.rebusDb.cursor()
            cs.execute("insert into Images(path, text) values (?, ?)",(path, text,))
            self.rebusDb.commit()
        except self.rebusDb.Error as e:
            print(e)


    def getAll(self):
        try:
            cs = self.rebusDb.cursor()
            cs.execute("select * from Images")
            dataSet = cs.fetchall()
            self.rebusDb.commit()
            for item in dataSet:
                print(item)
        except self.rebusDb.Error as e:
            print(e)

    def getImagePathByWord(self, word):
        try:
            cs = self.rebusDb.cursor()
            cs.execute("select * from Images where text = ?", (word,))
            dataSet = cs.fetchall()
            self.rebusDb.commit()
            if not dataSet:
                return None
            return dataSet[0][1]
        except self.rebusDb.Error as e:
            print(e)
