import unittest
from unittest.mock import patch

import myCart

class TestMyCartAdmin(unittest.TestCase):
    """
    - Admin should be able to add categories and products.
    - Admin should be able to see details of the products added to the cart by the user.
    - Admin should be able to see all the bills generated by all the users.
    """
    
    def test_database_connection(self):
        con,cur = myCart.initDB()
        self.assertTrue(con.status)
        

    @patch('builtins.input', side_effect=['admin', 'Sports', 'Fashion'])
    def test_add_category(self,mock_input):
        username = mock_input()
        category = mock_input()
        con,cur = myCart.initDB()
        category = myCart.CartCategory(con,cur,username) 
        category.addCategory()
        con.close()
    
    @patch('builtins.input', side_effect=['admin', 'Sports', 'football',2500])
    def test_add_product(self,mock_input):
        username = mock_input()
        category = mock_input()
        con,cur = myCart.initDB()
        product = myCart.CartProduct(con,cur,username) 
        product.addProduct()


    @patch('builtins.input', side_effect=['Sports', 'test'])
    def test_get_all_products(self,mock_input):
        username = mock_input()
        category = mock_input()
        con,cur = myCart.initDB()
        product = myCart.CartProduct(con,cur,username) 
        product.getAllProductsByCategory()

    @patch('builtins.input', return_value='shubham')
    def test_get_bill_by_username(self,mock_input):
        username = mock_input()
        con,cur = myCart.initDB()
        cart = myCart.Cart(con,cur,username) 
        cart.getBillForUser()

if __name__ == '__main__':
    unittest.main()