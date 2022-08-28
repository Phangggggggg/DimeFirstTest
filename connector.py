from typing import Type

import mysql.connector


class Connector:
    def __init__(self,host='localhost',user='root',password='phang789',port='3306',database='fmb'):
        super(Connector, self).__init__()
        self.connection = mysql.connector.connect(host=host,user=user,password=password,port=port,database=database)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        return self.connection.close()

    def store_historical(self, data):
        query = (
            "INSERT INTO historical_dividens(date,label,adjDividend,dividend,recordDate,paymentDate,declarationDate)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s)")
        for d in data:
            values = (d['date'],d['label'],d['adjDividend'],d['dividend'],d['recordDate'],d['paymentDate'],d['declarationDate'])
            self.cursor.execute(query,values)
            self.connection.commit()

