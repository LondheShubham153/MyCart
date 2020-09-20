# Importing required libraries

import psycopg2
import os
import sys
from schema import config
import time

# Importing classes designed for SRP

from cart.cartUser import CartUser
from cart.cartCategory import CartCategory
from cart.cartProduct import CartProduct
from cart.cart import Cart

def initDB():
    """
        This is the database initialization which returns a connection and cursor object
    """
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



def displayCartMenu():
    """
    This is the menu for MyCart Cli application 
    """
    print('------- MENU -------')
    print('  0. Register Admin')
    print('  1. Register User')
    print('  2. All Users')
    print('  3. Add Category')
    print('  4. Get Categories')
    print('  5. Add Product')
    print('  6. Get Product By Category')
    print('  7. Add Product To Cart')
    print('  8. Get Bill By username')
    print('  9. Exit')
    print('--------------------')

def run():

    print("Checking connection to MyCart\n")
    time.sleep(2)
    
    connection, cursor = initDB()
    print("Connection successful, Welcome to MyCart\n")
    
    user = CartUser(connection, cursor) 
    username = user.getUser(input("Enter your registered email : "))
    
    if not username:
        user.registerUser()

    category = CartCategory(connection, cursor,username)
    product = CartProduct(connection, cursor,username)
    cart = Cart(connection, cursor,username)

    while True:
        displayCartMenu()
    
        n = int(input("Enter option : "))
        if n == 0:
            user.registerUser(isAdmin=True)
        elif n == 1:
            os.system('clear')  
            user.registerUser()
        elif n == 2:
            os.system('clear')
            user.getAllUsers()
        elif n == 3:
            os.system('clear')
            category.addCategory()
        elif n == 4:
            os.system('clear')
            category.getAllCategories()
        elif n == 5:
            os.system('clear')
            product.addProduct()
        elif n == 6:
            os.system('clear')
            product.getAllProductsByCategory()
        elif n == 7:
            os.system('clear')
            cart.addProductToCart()
        elif n == 8:
            os.system('clear')
            cart.getBillForUser()
        elif n == 9:
            os.system('clear')
            connection.close()
            print('----- Thank You For shopping with us-----')
            break
        else:
            os.system('clear')
            run()
    
if __name__ == '__main__':
    run()
           
            
    
    
