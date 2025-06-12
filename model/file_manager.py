import os
import pickle



def check_file(filename):
    return os.path.exists(filename)


def read_from_file(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"خطا در خواندن فایل: {e}")
        return []

def write_to_file(filename, data_list):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data_list, file)
        return True
    except Exception as e:
        print(f"خطا در نوشتن فایل: {e}")
        return False
