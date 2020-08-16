#csv file parser to data structure

# data_url = 'http://bit.ly/2cLzoxH'
# gapminder = pd.read_csv(data_url)
# print(gapminder.head(3))

# with open(request, newline='') as csv_file:
#     csv_text = csv.reader(csv_file)
#     #for row in csv_text:
#     print(csv_text)

# import csv
# import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="testuser", password="1234")

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
# request = input("File requested: ")

# data = pd.read_csv(request)
# print(data)
