import os
import pickle

def read_from_file(filename):
    try:
        file = open(filename,"rb")
        data_list = pickle.load(file)
        file.close()
        return data_list
    except Exception as e:
        print(e)
        return []



def write_to_file(filename, data_list):
    file = open(filename, "wb")
    pickle.dump(data_list, file)
    file.close()

