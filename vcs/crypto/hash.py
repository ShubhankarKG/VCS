import hashlib
from os import getcwd, listdir
from os.path import join, normpath, basename
BLOCK_SIZE = 65536


def get_files_list():
    current_path = normpath(getcwd())
    return [join(current_path, f) for f in listdir(current_path)]


def hash_of_repo():
    files = get_files_list()
    list_of_hashes = []
    for each_file in files:
        get_hash = hash_of_file(each_file)
        list_of_hashes.append('Filename: {}\tHash: {}\n'.format(basename(each_file), get_hash))
    return list_of_hashes


def hash_of_file(file):
    try:
        global BLOCK_SIZE
        sha1 = hashlib.sha1()
        with open(file, 'rb') as file:
            file_buffer = file.read(BLOCK_SIZE)
            while len(file_buffer) > 0:
                sha1.update(file_buffer)
                file_buffer = file.read(BLOCK_SIZE)
        return sha1.hexdigest()
    except FileNotFoundError:
        print("Requested file not found")
