import sys,random,time,os
import csv,json
import logging
from time import gmtime, strftime

class datagen:

    def __init__(self):
        pass

    def generate_row(self,num_columns):
        return ('{},'.format(random.randint(0,9)) for i in range(num_columns))

    def generate_column(self,num_rows,num_columns):
        return (self.generate_row(num_columns) for i in range(num_rows))

if __name__ == "__main__":

    data = datagen()
    os.makedirs("data", exist_ok=True)
    with open("data/{}.csv".format(strftime("%Y-%m-%d-%H-%M-%S", gmtime())), "a") as _:
        column_generator = data.generate_column(int(sys.argv[1]),int(sys.argv[2]))
        for line in column_generator:
            _.write(''.join(line))