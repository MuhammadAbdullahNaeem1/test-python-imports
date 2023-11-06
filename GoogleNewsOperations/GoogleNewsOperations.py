
import sys
import os

pg_operations_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(pg_operations_path)

from PgOperationsMain.PgOperationsMain import PgOperationsMain

class GoogleNewsOperations:
    def __init__(self):
        self.pg_operations = PgOperationsMain()
        print("GoogleNewsOperations init")

if __name__ == '__main__':
    gno = GoogleNewsOperations()
