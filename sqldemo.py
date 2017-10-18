import sqlalchemy, random
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text



engine = create_engine('sqlite:///:memory:', echo=True)

def main():
  conn = engine.connect()
  metadata = MetaData()
  createTables(metadata, conn)
  statement = text("INSERT INTO users (id, name, fullname, age)"
  " values (1, 'hal','Halsted Matthew Larsson', 37)")
  conn.execute(statement)

  statement = text("INSERT INTO users (id, name, fullname, age)"
  " values (2, 'Emma','Emma Doovid Judith Harringtowne', " + str(random.randint(10,16)) + ")")
  conn.execute(statement)

  statement = text("INSERT INTO pets (name, age, userid)"
  " values ('Josie', 4, 1)")
  conn.execute(statement)

  statement = text("INSERT INTO pets (name, age, userid)"
  " values ('Bobbi', 24, 2)")
  conn.execute(statement)

  statement = text("INSERT INTO pets (name, age, userid)"
  " values ('Bubbles', 14, 2)")
  conn.execute(statement)

  query = text("SELECT users.name, pets.name from pets JOIN users ON pets.userid = users.id")
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
