# write your code here
import os
import argparse
import hashlib
from pprint import pprint


# --------------------------- Handle input ---------------------------#
def check_duplicates():
    """
    If user wants to check duplicates
    :return: True for checking; False for not checking
    """
    while True:
        print('\n============================================')
        answer = input('Check for duplicates? (yes or no)\n>>> ')
        if answer.lower() == 'yes':
            return True
        elif answer.lower() == 'no':
            return False
        else:
            print('Wrong option')


def check_delete():
    """
    If users wants to delete duplicates files
    :return: True for deleting; False for not deleting
    """
    while True:
        print('\n============================================')
        answer = input('Delete files? (yes or no)\n>>> ')
        if answer.lower() == 'yes':
            return True
        elif answer.lower() == 'no':
            return False
        else:
            print('Wrong option')


# --------------------------- Get File Hash ---------------------------#
def get_hash(full_path):
    m = hashlib.md5()
    with open(full_path, "rb") as f:
        data = f.read()
        m.update(data)
        return m.hexdigest()


# --------------------- Get, Display and Delete files --------------------#
def get_file(folder, extension):
    ''' 
    Return a dict with file size as keys.
    :param folder: folder to search
    :param extension: file format to search, '' for all file
    :return dict = {
        size1: [file path1, file path2, ...],
        size2: [file path1, ...],
        ...,
    }
    '''
    got_files = {}
    for root, dirs, files in os.walk(folder, topdown=True):
        for name in files:
            if extension == '' or name.split('.')[-1] == extension:
                file_path = os.path.join(root, name)
                file_size = os.path.getsize(file_path)

                if file_size not in got_files:
                    got_files[file_size] = [file_path]
                else:
                    got_files[file_size].append(file_path)
    
    return got_files


def check_size(files):
    ''' 
    Return a dict just cotains files with same size.
    :param files: all files
    :return dict = {
        size1: [file1, file2, ...],
        size2: [file1, file2, ...],
        ...
    }
    '''
    same_size_file = {key: value for (key, value) in files.items() if len(value) > 1}
    return same_size_file


def check_hash(files):
    ''' 
    Return a nested dict with file size as keys for outter dict and hash value as keys for inner dict.
    :param files: files with same size
    :return dict = {
        size1: {
            hash1: [file1, file2, ...]
            hash2: [file1, ...]
        },
        size2: {
            ...
        },
        ...
    }
    '''
    file_with_hash = {}
    for size in files:
        hash_dict = {}
        for path in files[size]:
            file_hash = get_hash(path)
            try:
                hash_dict[file_hash].append(path)
            except KeyError:
                hash_dict[file_hash] = [path]
        file_with_hash[size] = hash_dict

    return file_with_hash


def display_same_size(size_sort, files):
    '''
    Print files have same size.
    :param size_sort: user's sorting option
    :param files: files with same size
    '''
    if size_sort == '1':
        files = dict(sorted(files.items(), reverse=True))
    else:
        files = dict(sorted(files.items(), reverse=False))

    for size in files:
        print(f'\n{size} bytes')
        for path in files[size]:
            print(path)


def display_same_hash(size_sort, files):
    '''
    Print files have same hash.
    Create a list of files to delete with tuple(file_path, file_size)
    :param size_sort: user's sorting option
    :param files: files with same hash
    :return list = [(file_path1, file_size1), ...]
    ]
    '''
    if size_sort == '1':
        files = dict(sorted(files.items(), reverse=True))
    else:
        files = dict(sorted(files.items(), reverse=False))

    file_for_delete = []
    count = 1
    for size, value in files.items():
        print(f'\n{size} bytes')
        for h, paths in files[size].items():
            if len(paths) > 1:
                print("Hash:", h)
                for path in paths:
                    print(f"{count}. {path}")
                    count += 1
                    file_for_delete.append((path, size))
    return file_for_delete


def check_delete_input(list, files):
    '''
    Return the file number that user want to delete.
    :param list: user input list
    :param files: list of files to delete
    :return: a list of (index+1) user want to delete.
    '''
    delete_nums = []
    try:
        for item in list:
            delete_nums.append(int(item))
    except ValueError:
        raise ValueError('Wrong input format')
    
    for num in delete_nums:
        if num > len(files):
            raise ValueError('Wrong input format')
    
    return delete_nums


def delete_file(nums, files):
    '''
    Delete files by index and print how much spaces are freed.
    :param nums: list of (index+1) user want to delete
    :param files: list of files to delete
    '''
    deleted_bytes = 0
    for index in nums:
        file = files[index - 1]
        deleted_bytes += file[1]
        os.remove(file[0])

    print(f'\nTotal freed up space: {deleted_bytes} bytes')


# -------------------------------- Main --------------------------------#
parser = argparse.ArgumentParser(description='')
parser.add_argument("root_folder", default=None, nargs='?')
args = parser.parse_args()
if args.root_folder is not None:
    
    file_extension = input('Enter file format:\n>>> ')
    while True:
        user_sort = input('\nSize sorting options:\n1. Descending\n2. Ascending\n\nEnter a sorting option:\n>>> ')
        if user_sort == '1' or user_sort == '2':
            break
        else:
            print('Wrong option')

    file_list = get_file(args.root_folder, file_extension)
    same_size_files = check_size(file_list)
    display_same_size(user_sort, same_size_files)

    if check_duplicates():
        files_with_hash = check_hash(same_size_files)
        file_to_delete = display_same_hash(user_sort, files_with_hash)
    
        if check_delete():
            while True:
                delete_input = input('\nEnter file numbers to delete:\n>>> ').split(' ')
                try:
                    delete_num = check_delete_input(delete_input, file_to_delete)
                except ValueError:
                    print('\nWrong format')
                else:
                    break

            delete_file(delete_num, file_to_delete)

else:
    print('Directory is not specified')
