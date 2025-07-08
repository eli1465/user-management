import os
import pickle

def check_file (filename):
    return os.path.exists(filename)


def read_from_file(filename):
    if not check_file(filename):
        os.makedirs(os.path.dirname(filename),exist_ok= True)
        with open(filename,"wb")as f:
            pickle.dump([],f)
        return[]
    if os.stat(filename).st_size ==0:
        return[]
    with open(filename,"rb")as f:
        return pickle.load(f)



def write_to_file(filename, data_list):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename,"wb")as f:
        pickle.dump(data_list, f)

