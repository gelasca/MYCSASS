import  sqlite3

conn = sqlite3.connect('contas.db')

cursor = conn.cursor()

def create_table(name, cnpj):
  cursor.execute(""""
                CREATE TABLE IF NOT EXISTS ENTERPRISE (
                NAME TEXT NOT NULL,
                CNPJ TEXT NOT NULL
                )
  """)


def insert():
  cursor.execute(""""
                INSERT INTO IF NOT EXISTS contas (
                
                )
  """)
  conn.commit()


