import os
import argparse


def get_file(folder):
    os.chdir(folder)
    get_files = []
    for root, dirs, files in os.walk('.', topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            file_name = os.path.basename(file_path)
            file_extension = file_name.split('.')[-1]
            get_files.append((file_size, file_extension, file_path))
    return get_files


def check_same_size(all_file):
    same_size_file = {}
    for (file_size, file_extension, file_path) in all_file:
        try:
            same_size_file[file_size].append((file_extension, file_path))
        except KeyError:
            same_size_file[file_size] = [(file_extension, file_path)]
    same_size_file = {key: value for (key, value) in same_size_file.items() if len(value) > 1}
    return same_size_file


def display_user(user_extension, size_sort, all_file):
    if size_sort == '1':
        all_file = dict(sorted(all_file.items(), reverse=True))
    else:
        all_file = dict(sorted(all_file.items(), reverse=False))
    for size in all_file:
        print(f'{size} bytes')
        for (extension, path) in all_file[size]:
            if user_extension == '':
                print(path)
            else:
                if extension == user_extension:
                    print(path)


# ----------------------- Main ------------------------#
parser = argparse.ArgumentParser(description='')
parser.add_argument("root_folder", default=None, nargs='?')
args = parser.parse_args()
if args.root_folder is not None:
    file_extension = input('Enter file format:\n> ')
    while True:
        user_sort = input('Size sorting options:\n1. Descending\n2. Ascending\n> ')
        if user_sort == '1' or user_sort == '2':
            break
        else:
            print('Wrong option')
    file_list = get_file(args.root_folder)
    same_size_files = check_same_size(file_list)
    display_user(file_extension, user_sort, same_size_files)

else:
    print('Directory is not specified')
