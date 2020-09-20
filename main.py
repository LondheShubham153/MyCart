import psycopg2
import sys
import os
import config
import time

from cartUser import CartUser
from cartCategory import CartCategory
from cartProduct import CartProduct

def initDB():
    try:
        connection = psycopg2.connect(user=config.PG_USERNAME,
                                      password=config.PG_PASSWORD,
                                      host=config.PG_HOST,
                                      port=config.PG_PORT,
                                      database=config.PG_DATABASE)
        cursor = connection.cursor()
        return connection, cursor

    except (Exception, psycopg2.Error, psycopg2.OperationalError) as error:
        error_response_obj["Issue.severity"] = 'error'
        error_response_obj["Issue.code"] = 'exception'
        error_response_obj["Issue.diagnostics"] = 'There was a failure in connecting or retrieving data from the postgres'

        return 'POSTGRES_CONNECTION_ERROR', None



def displayMainMenu():
    print('------- MENU -------')
    print('  0. Register Admin')
    print('  1. Register User')
    print('  2. All Users')
    print('  3. Add Category')
    print('  4. Get Categories')
    print('  5. Add Product')
    print('  6. Get Product By Category')
    print('--------------------')

def exit():
    n = int(input(" Press 5 to exit : "))

    if n == 5:
        os.system('cls')  # For Windows
        run()
    else:
        print(" Invalid Option")
        exit()

def run():

    print("Checking connection to MyCart")
    time.sleep(2)
    connection, cursor = initDB()
    print("Connection successful, Welcome to MyCart")
    displayMainMenu()
    user = CartUser() 
    category = CartCategory()
    product = CartProduct()

    n = int(input("Enter option : "))
    if n == 0:
        user.registerUser(connection, cursor,isAdmin=True)
    elif n == 1:
        os.system('clear')  
        user.registerUser(connection, cursor)
    elif n == 2:
        os.system('clear')
        user.getAllUsers(connection, cursor)
    elif n == 3:
        os.system('clear')
        category.addCategory(connection, cursor)
    elif n == 4:
        os.system('clear')
        category.getAllCategories(connection, cursor)
    elif n == 5:
        os.system('clear')
        product.addProduct(connection, cursor)
    elif n == 6:
        os.system('clear')
        product.getAllProductsByCategory(connection, cursor)
        print('----- Thank You -----')
    else:
        os.system('cls')
        run()
        
    
if __name__ == '__main__':
    run()
           
            
    
    
