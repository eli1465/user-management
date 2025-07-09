import os
import pickle

def check_file (filename):
    return os.path.exists(filename)


def read_from_file(filename):
    if check_file(filename):
        with open(filename,"rb")as file:
            try:
                return pickle.load(file)
            except EOFError:
                return[]
    else:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as file:
            pickle.dump([],file)
        return[]


def write_to_file(filename, data_list):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename,"wb")as file:
        pickle.dump(data_list, file