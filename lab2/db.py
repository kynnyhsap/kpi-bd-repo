import psycopg2


class DB:
    def __init__(self):
        self.conn = None
        self.cur = None

    def init(self):
        self.conn = psycopg2.connect(dbname='kpi_bd_labs', host='localhost')
        self.cur = self.conn.cursor()

        print('Connection opened.')

    def close(self):
        self.cur.close()
        self.conn.close()

        print('Connection closed.')

    def __enter__(self):
        self.init()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


db = DB()
db.init()

