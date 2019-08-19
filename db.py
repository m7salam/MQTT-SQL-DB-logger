from config import Base, Session,engine
from models import *
import json
import psycopg2



def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

#old code until finishing
s = Session()

#recreate_database()




#function to check the last item in a list
def is_last(alist,choice):
	if choice == alist[-1]:
		print("Same Value as the one before!")
		return True
	else:
		print("New Value Detected :)")
		return False

#===============================================================
#Functions to push Sensor Data into Database

#Function to save ToiletRoll Reading to DB Table
def Toilet_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['title']
	Level = json_Dict['level_tissuesensor']
	List = []

	all_values = List.append(Level)

	#Push into DB Table
	data = TissueSensor(
		title= str(SensorID),
		level_tissuesensor = str(Level),
		)
	if is_last(List,Level) == False:
		s.add(data)
		s.commit()
		s.close()
		print "Inserted Data into TissueSensor into Database."
		print ""
	else:
		print "Not inserted into the database"	
		s.close()
	



# Function to save Smellreadings to DB Table
def Smell_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['title']
	Level = json_Dict['level_smellsensor']
	
	#Push into DB Table
	# dbObj = DatabaseManager()
	# dbObj.add_del_update_db_record("INSERT into SmellSensor (title, level_smellsensor) VALUES ('"+ SensorID + "','" + Level + "')")
	# del dbObj
	data = SmellSensor(
		title= str(SensorID),
		level_smellsensor = str(Level),
		)
	
	s.add(data)
	s.commit()
	s.close()
	print "Inserted Data into SmellSensor Table in stmdb Database."
	print ""


#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
	if Topic == "/sunway/level1/toilet1/tissuesensor":
		Toilet_Data_Handler(jsonData)
	elif Topic == "/sunway/level1/toilet1/smellsensor":
		Smell_Data_Handler(jsonData)	

#===============================================================