#Information from
#https://github.com/ets-labs/python-dependency-injector/blob/master/examples/miniapps/movie_lister/movies/finders.py
import Assembler from di_assembler

class TwitterListener:
    def __init__(self,Assembler):
        #creating an object from di injector
        self._obj_assembler = Assembler
        self._user_list = _obj_assembler.get_userlist_fromDB()
        self.cfg = _obj_assembler.get_cfg_fromDB()
