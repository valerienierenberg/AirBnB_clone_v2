#!/usr/bin/python3

""" notes from here and will flesh out """

""" __engine set to none
__session set to none

__init__(self):
create (self.__engine)
engine must be linked to MySQL DB and user created before (hbnb_dev and hbnb_dev_db)
retrieve values via env variables
HBNB_MYSQL_USER
HBNB_MYSQUL_PWD
HBNB_MYSQL_DB

REMEMBER pool_pre_ping=True when calling create_engine
drop all tables if env variable HBNB_ENV == test all(self, cls=None)
query on current db session (self.__session) all obj depending on class name (arg cls)
if cls=None, query all types of obj (User, State, City, Amenity, Place and Review)
Returns a dictionary key = <class-name>.<object-id>
value = obj

new(self,obj) add obj to current db session
save(self) comment all changes of current db session
delete(self, obj=None)
reload(self) create all tables in db, create current db session

