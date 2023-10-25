import pandas as pd
import unittest
from random import randint

class BookLover():
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name must be a string')
        
        if isinstance(email, str):
            self.email = email
        else:
            raise TypeError('Email must be a string')
            
        if isinstance(fav_genre, str):
            self.fav_genre = fav_genre
        else:
            raise TypeError('Fav Genre must be a string')
        
        if isinstance(num_books, int):
            self.num_books = num_books
        else:
            raise TypeError('Num Books must be int')
        
        if isinstance(book_list, pd.DataFrame):
            self.book_list = book_list
        else:
            raise TypeError('Book list must be pandas dataframe')
            
    def add_book(self, book_name, rating):
        
        if isinstance(book_name, str):
            pass
        else:
            raise TypeError('Book Name must be a string')
        
        if isinstance(rating, int) and (rating >= 0 and rating <= 5):
            pass
        else:
            raise Exception('Rating must be an int and between 0 and 5')
        
        if book_name not in self.book_list['book_name'].tolist():
            new_book = pd.DataFrame({'book_name': [book_name], 
                                     'book_rating': [rating]
                                    })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            pass
    
    def has_read(self, book_name):
        if not isinstance(book_name, str):
            raise TypeError('Book Name must be string')
        
        return book_name in self.book_list.book_name.tolist()
    
    def num_books_read(self):
        return self.book_list.shape[0]
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]
    
class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        me.add_book(book_name='Naked Statistics', rating=4)
        self.assertTrue('Naked Statistics' in me.book_list['book_name'].tolist(), "Naked Statistics not in list")
        # add a book and test if it is in `book_list`.

    def test_2_add_book(self):
        me.add_book(book_name='Naked Statistics', rating=4)
        me.add_book(book_name='Naked Statistics', rating=4)
        self.assertTrue(len([i for i in me.book_list['book_name'].tolist() if i == 'Naked Statistics']) == 1, 'book in list more than twice')
         # add the same book twice. Test if it's in `book_list` only once.
                
    def test_3_has_read(self): 
        me.add_book(book_name='Naked Statistics', rating=4)
        self.assertTrue(me.has_read('Naked Statistics'), "Book has not been ready")
        # pass a book in the list and test if the answer is `True`.
        
    def test_4_has_read(self): 
        self.assertFalse(me.has_read(book_name='Naked Economics'), "book is in list")
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
    def test_5_num_books_read(self): 
        [me.add_book(book_name='HP {}'.format(i), rating=randint(0, 5)) for i in range(1, 8)]
        self.assertEqual(me.num_books_read(), 8, '{} books read, not 7'.format(me.num_books_read()))
        # add some books to the list, and test num_books matches expected.

    def test_6_fav_books(self):
        [me.add_book(book_name = 'HP {}'.format(i), rating= randint(0, 5)) for i in range(1, 8)]
        self.assertTrue(all(i > 3 for i in me.fav_books()['book_rating']), "not all books have a rating over 3")
        # Your test should check that the returned books have rating  > 3
            