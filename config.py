# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import psycopg2


#local Pi database

#alternative connection way

#DATABASE_URI= psycopg2.connect(database="dbname", user="username", password="dbpassword", host="ipaddress", port="5432")


DATABASE_URI = "postgres+psycopg2://postgres:Global1234@192.168.0.170:5432/stmdb" #just an example also you might consider using environment variables here for security
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)
