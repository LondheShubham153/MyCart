import unittest
from unittest.mock import patch

import myCart

class TestMyCartUser(unittest.TestCase):
    #TODO
    """
    - Users should be able to view the list of multiple categories.
    - Users should be able to view all the products under a particular category.
    - Users should be able to view product details.
    - Users should be able to add products to Cart.
    - Users should be able to buy multiple products from the Cart.
    - Users should be able to remove products from the Cart.
    - If the final billing amount is greater than Rs 10,000 then Rs 500 OFF should be given to the user.
    - If the final billing amount is less than Rs 10,000 then no discount should be given to the user.
    - Bill should be generated for multiple product purchases showing the actual amount, discounted
    amount, and the final amount.
    """

    
    def test_database_connection(self):
        con,cur = myCart.initDB()
        self.assertTrue(con.status)
        

    @patch('builtins.input', side_effect=['shubham'])
    def test_get_all_categories(self,mock_input):
        username = mock_input()
        con,cur = myCart.initDB()
        category = myCart.CartCategory(con,cur,username) 
        category.getAllCategories()

    @patch('builtins.input', side_effect=['shubham', 'Test','electronics'])
    def test_get_all_products(self,mock_input):
        username = mock_input()
        category = mock_input()
        con,cur = myCart.initDB()
        product = myCart.CartProduct(con,cur,username) 
        product.getAllProductsByCategory()

    @patch('builtins.input', side_effect=['shubham', 1,1])
    def test_add_product_to_cart(self,mock_input):
        username = mock_input()
        category = mock_input()
        con,cur = myCart.initDB()
        cart = myCart.Cart(con,cur,username) 
        cart.addProductToCart()
