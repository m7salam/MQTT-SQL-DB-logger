# DataBase Logger for MQTT - PostgresQL 

* This code uses SQLAlchemy and MQTT to read topics sent by the publisher in json dictionary format, parse it and save it into SQL database in our case its PostgresQL. using alembic for database migrations but its not totally configured yet. but the  rest is working perfectly.


## understanding the structure

These instructions explanation should give you an understanding of which file do what.


```
config.py >>> it has the database configurations
db.py  >>>> its used for the CURD operations inside the database 
models.py >>> where you create the tables using SQLAlchemy
MQTT.py >>>> the subscriber main code in python - MQTT
setup.sh >>> bash file for rasberrypi to install python 3.7

```

### Prerequisites

What things you need to install the software and how to install them
you will also need to be familiar with MQTT and have a publisher working , and broker in the middle in our case we used RasberryPi as broker , this is just the subscriber code setup to log readings into PostgresQL

```
virtualenv
Python2.7.15
SQLAlchemy
MQTT - Publisher device publishing messages
you can install all " pip install -r requirments.txt "
```

### Installing

A step by step series of examples that tell you how to get a development env running


```
virtualenv  venv
source venv/bin/activate
pip install -r requirements.txt
```

## Authors

* **Mo Salam** - [m7salam](https://github.com/m7salam)
