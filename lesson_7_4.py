import os
import some_data
from collections import defaultdict


def dir_info():
    root_dir = some_data.__path__[0]
    some_files = defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            some_files[size] += 1

        for size, nums in sorted(some_files.items()):
            print(f'{size}: {nums}')


dir_info()
