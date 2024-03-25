import pyodbc

class DBUtil:
    @staticmethod
    def get_db_conn():
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=DESKTOP-NQM93MA\\SQLEXPRESS;'
                                  'Database=BANK;'
                                  'Trusted_Connection=yes;')
            print("Connected Successfully")
            return conn
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return None