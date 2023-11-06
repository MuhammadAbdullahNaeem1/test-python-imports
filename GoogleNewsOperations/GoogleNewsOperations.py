# from PgOperationsMain.PgOperationsMain import PgOperationsMain
# class GoogleNewsOperations:
#     def __init__(self):
#         pgOperationsMain = PgOperationsMain()
#         print("GoogleNewsOperations init")
#         pass


import sys
import os


pg_operations_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'PgOperationsMain')
sys.path.append(pg_operations_path)

from PgOperationsMain import PgOperationsMain

class GoogleNewsOperations:
    def __init__(self):
        pass
