import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.sql import text



engine = create_engine('sqlite:///:memory:', echo=True)

def main():
  conn = engine.connect()
  metadata = MetaData()
  createTables(metadata, conn)
  s = text("SELECT users.fullname AS title FROM users")
  statement = text("INSERT INTO users (name, fullname) values ('hal', 'Halsted Matthew Larsson')")
  conn.execute(statement)

  query = text("Select * from users")
  result = conn.execute(query).fetchall()
  print(result)






def createTables(metadata, conn):
  users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String))

  metadata.create_all(engine)

main()
