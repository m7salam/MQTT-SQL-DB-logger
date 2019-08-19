from sqlalchemy import Column, Integer, String, Date, TIMESTAMP
from config import Base
import datetime


class TissueSensor(Base):

    __tablename__ = 'TissueSensor'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    initial_reading = Column(String, default="3")
    empty_reading = Column(String, default="8")
    level_tissuesensor = Column(String)
    date = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)

    
    def __repr__(self):
        return "<TissueSensor(title='{}', initial_reading='{}', empty_reading='{}', level_tissuesensor='{}', date='{}')>"\
                .format(self.title, self.initial_reading, self.empty_reading, self.level_tissuesensor, self.date)



class SmellSensor(Base):

    __tablename__ = 'SmellSensor'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    level_smellsensor = Column(String)
    date = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return "<SmelSensor(title='{}', level_smellsensor='{}', date='{}')>"\
                .format(self.title, self.level_smellsensor)


class SoupSensor(Base):

    __tablename__ = 'SoupSensor'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    initial_reading = Column(String, default="4")
    empty_reading = Column(String, default="12")
    level_soupsensor = Column(String)
    date = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return "<SoupSensor(title='{}', intial_reading='{}', empty_reading='{}', level_soupsensor='{}', date='{}')>"\
                .format(self.title, self.initial_reading, self.empty_reading, self.level_soupsensor, self.date)

