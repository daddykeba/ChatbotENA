# This is a simple module to fetch data from MySQL db.
# python -m pip install mysql-connector //run this command if you face import error
# references: https://www.w3schools.com/python/python_mysql_getstarted.asp

# Before used this code  please make suure to install  this python package mysql-connector 
# Eg: python -m pip install mysql-connector

import mysql.connector
import traceback

def getData(query:str):
        """
         @query: sql query that needs to be executed.

         returns the data being executed in "List" format
        """

        try:

            # Setup the connection.
            # Pass your database details here
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='daddy6189',
                database='flask',
                auth_plugin='mysql_native_password'
                )

            # set up the cursor to execute the query
            cursor = mydb.cursor()
            cursor.execute(query)

            # fetch all rows from the last executed statement using `fetchall method`.
            results = cursor.fetchall()
            return results
        except:
            print("Error occured while connecting to database or fetching data from database. Error Trace: {}".format(traceback.format_exc()))
            return []

# test the file before integrating with the bot by uncommenting the below line.
# print(getData("SELECT * FROM test.customer;")
