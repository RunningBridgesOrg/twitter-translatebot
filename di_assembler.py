class Assembler(object):
    def __init__(self, DB_model):
        self._DB_model = DB_model;

    def get_cfg_fromDB(self):
            """Return user list and cfgs"""
    def get_userlist_fromDB(self):

class MySQLAssembler(Assembler):
    def __init__(self, DB_model, database):
        #define a path to DB.
        #for SQL later,
        #self.database = database;
        super(MySQLAssembler, self).__init__(DB_model)

    #implment method
    def get_cfg_fromDB(self):
        #add implementation for SQL (ex. (select token)query,)
        cfg = {};
        return cfg;

#this supposed to read from DB
    def get_userlist_fromDB(self):
        #add implementation for SQL (ex. (select userlist)query,)
        user_list = ['25073877','838107760721985536']
        return user_list;
#next week, write one more for xml
