import sqlalchemy, random
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text



engine = create_engine('sqlite:///:memory:', echo=True)

def main():
  conn = engine.connect()
  metadata = MetaData()
  createTables(metadata, conn)
  statement = text("INSERT INTO users (name, fullname, age)"
  " values ('hal','Halsted Matthew Larsson', 37)")
  conn.execute(statement)

  statement = text("INSERT INTO users (name, fullname, age)"
  " values ('Kasey','Kasey Gabloff', 17)")
  conn.execute(statement)

  statement = text("INSERT INTO pets (name, age, userid)"
  " values ('Josie', 4, 1)")
  conn.execute(statement)

  statement = text("INSERT INTO pets (name, age, userid)"
  " values ('Fiona', 16, 1)")
  conn.execute(statement)

  statement = text("INSERT INTO pets (name, age, userid)"
  " values ('Andy', 12, 1)")
  conn.execute(statement)

  statement = text("INSERT INTO pets (name, age, userid)"
  " values ('Marigold', 6, 2)")
  conn.execute(statement)

  statement = text("INSERT INTO pets (name, age, userid)"
  " values ('Evie', 9, 2)")
  conn.execute(statement)

  query = text("Select pets.name, users.name from pets JOIN users ON pets.userID = users.ID ")
  result = conn.execute(query).fetchall()
  print(result)






def createTables(metadata, conn):
  users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer),
    Column('fullname', String))


  pets = Table('pets', metadata,
    Column('id', Integer, primary_key=True),
    Column('userId', Integer),
    Column('name', String),
    Column('age', Integer),
  )
  metadata.create_all(engine)

main()
