# write your code here
import os
import argparse
import hashlib


# --------------------------- Handle input ---------------------------#
def check_duplicates():
    while True:
        print('============================================')
        answer = input('Check for duplicates? (yes or no)\n>>> ')
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print('Wrong option')


def check_delete():
    while True:
        print('============================================')
        answer = input('Delete files? (yes or no)\n>>> ')
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print('Wrong option')


# --------------------------- Operate files ---------------------------#
def get_file(folder, extension):
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
    same_size_file = {key: value for (key, value) in files.items() if len(value) > 1}
    return same_size_file


def get_hash(full_path):
    m = hashlib.md5()
    with open(full_path, "rb") as f:
        data = f.read()
        m.update(data)
        return m.hexdigest()


def check_hash(files):
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
    if size_sort == '1':
        files = dict(sorted(files.items(), reverse=True))
    else:
        files = dict(sorted(files.items(), reverse=False))

    for size in files:
        print(f'\n{size} bytes')
        for path in files[size]:
            print(path)


def display_same_hash(size_sort, files):
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


def delete_file(nums, files):
    deleted_bytes = 0
    for index in nums:
        if index > len(files):
            print(f'\nWarning: {index} file does not exist, confirm again')
            continue
        else:
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
        user_sort = input('\nSize sorting options:\n1. Descending\n2. Ascending\nEnter a sorting option:\n>>> ')
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
            delete_input = input('Enter file numbers to delete:\n>>> ').split(' ')
            delete_num = []
            try:
                for num in delete_input:
                    delete_num.append(int(num))
            except ValueError:
                print('Wrong format')
            else:
                break

        delete_file(delete_num, file_to_delete)

else:
    print('Directory is not specified')
