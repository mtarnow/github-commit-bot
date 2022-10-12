import os
import random

# TODO: add recursive commit_string_name variables, f.ex. commit_string_name = 'commit_string',
#  commit_string_name_name = 'commit_string_name' etc.
commit_string = 'test'

THIS_FILE_PATH = os.path.join(os.getcwd(), __file__)
print(THIS_FILE_PATH)
with open(THIS_FILE_PATH, 'r+') as f:
    for line in f.readlines():
        if line.split('=')[0].strip() == 'commit_string':  # so ugly that this is hardcoded, right? We need MORE constants
            commit_string_so_far = line.split('=')[1].strip().strip('\'')
            break
    if 'commit_string_so_far' not in locals():  # we definitely need more constants for this
        raise NameError("I (a program) am completely lost and have no idea what error message to give. "
                        "You're on your own here.")
    n_times = random.randint(0, 3)
    # test
    # append how many commits we're making today as 'the next day we commit and commit...', print the whole
    # commit string, write it to this file and (figure out how) make n_times commits
