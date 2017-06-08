import unittest,sqlite3
from dbConnect import connect_to_DB

class dbConnectTest(unittest.TestCase):
    def setUp(self):
        self.db = connect_to_DB()

#test successful retrieve
    def test_sqliteRetrieveSuccess(self):
        print("\nRunning sqllite Data Retrieve Success test")
        self.conn = sqlite3.connect(":memory:")

        self.assertEqual(self.db.sqlite_retrieve('spanish').__getitem__('consumer_key'),'rcIlpeAhFKSXlzhjnWqfkS9x7')
        self.assertEqual(self.db.sqlite_retrieve('spanish').__getitem__('consumer_secret'),'J96cwUhHWX93TvSxO7nBpmnqz8LCGuJLNQVFWKehg1bFQRysQe')
        self.assertEqual(self.db.sqlite_retrieve('spanish').__getitem__('access_token'),'838080768408612868-sLc6Uo8iAbdHrJTeEd5C2pjskaitgq6')
        self.assertEqual(self.db.sqlite_retrieve('spanish').__getitem__('access_token_secret'),'r1lj2ZT20H0aACoxqZdIHNq6nfBoWtCNwZNFrvAB6JOMn')


    def test_sqliteRetrievFailure(self):
        print("\nRunning sqllite Data Retrieve Failure test")
        self.conn = sqlite3.connect(":memory:")
        self.assertRaisesRegexp(self.db.sqlite_retrieve('spanish'),'AttributeError: ''NoneType'' object has no attribute ''items''')
