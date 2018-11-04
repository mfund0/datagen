import boto3
from botocore.exceptions import ClientError
from multiprocessing.dummy import Pool as ThreadPool
import sys,random,time
import csv,json
import logging
from time import time

class datagen:

    def __init__(self):
        pass

    def generate_row(self,num_columns):
        row = ''.join(['{},'.format(random.randint(0,9)) 
                        for i in range(num_columns)])
        return row[:-1]+'\n'

    def generate_column(self,num_rows,num_columns):
        columns = ''.join([self.generate_row(num_columns) 
                        for i in range(num_rows)])
        return columns

    def rows_json(self,num_colums):
        result = {}
        for i in range(num_colums):
            result['_{}{}'.format(i,time.clock())]= str(random.randint(0,9))
        return result

    def columns_json(self,num_colums,num_rows):
        result = {}
        for i in range(num_rows):
            result["_"+str(i)]= rows_json(num_colums)
        print(json.dumps(result,indent=2))
        return result

if __name__ == "__main__":
    #from runner import runner
    #runner = runner()
    data = datagen()
    with open("data/{}.csv".format(str(random.randint(0,9)+time())), "a") as myfile:
        myfile.write(data.generate_column(int(sys.argv[1]),int(sys.argv[2])))
    
    #runner.run(sys.argv[1:len(sys.argv)],num_tasks=2,)