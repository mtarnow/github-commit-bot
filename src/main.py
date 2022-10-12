import os
import random
import subprocess

# TODO: add recursive commit_string_name variables, f.ex. commit_string_name = 'commit_string',
#  commit_string_name_name = 'commit_string_name' etc.
commit_string = 'test.'
n_commits = 0


def execute_subcommand(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return_code = p.wait()
    if return_code != 0:
        raise ChildProcessError("Process didn't finish successfully.", cmd)


def git_commit():
    try:
        cmd = ['git', 'add', 'main.py']
        execute_subcommand(cmd)
        cmd = ['git', 'commit', '-m', f'"Very important change No. {n_commits+1}"']
        execute_subcommand(cmd)
        cmd = ['git', 'push']
        execute_subcommand(cmd)
    except ChildProcessError:
        raise


THIS_FILE_PATH = os.path.join(os.getcwd(), __file__)
print(THIS_FILE_PATH)
with open(THIS_FILE_PATH, 'r+') as f:
    # get two last lines consisting of the ending part of commit_string
    line1 = ''
    line2 = ''
    start = None
    for i, line in enumerate(f.readlines()):
        if line.split('=')[0].strip() == 'commit_string':
            start = i
            line2 = line
        elif start is not None:
            line = line.strip()
            if line != '' and line.strip()[0] == '+':
                line1 = line2
                line2 = line
            else:
                break
    # value of commit_string is assigned only in the first line 'commit_string = ...'
    if i == start + 1:
        last_lines = line2.split('=')[1].strip().strip('\'')
    # value of commit_string is assigned in the first line 'commit_string = ...' and the following line
    elif i == start + 2:
        last_lines = line1.split('=')[1].strip().strip('\'') + line2.split('+')[1].strip().strip('\'')
    # last two lines assigning value to commit_string  both are of format '+ ...'
    else:
        last_lines = line1.split('+')[1].strip().strip('\'') + line2.split('+')[1].strip().strip('\'')


# if 'commit_string_so_far' not in locals():  # we definitely need more constants for this
#     raise NameError("I (a program) am completely lost and have no idea what error message to give. "
#                     "You're on your own here.")
# 'Today I committed and committed again and committed again.'


ll = last_lines.split('.')
# if len(cs) > 1:
# split the last 2 lines into the part talking about the last day commits and the remainder of the previous days part
# (the last day commits fit into one full line - that's why we need at most 2)
main_part, last_day_part = ll[0], ll[1]
last_n_times = len(last_day_part.split('commit')) - 1  # how many commits in the last day

# change the last day commits from 'today' to 'the next day' format
main_part += ' and the next day'
if last_day_part.find("didn't") >= 0:
    main_part += " I didn't commit."
else:
    for n in range(last_n_times):
        if n == 0:
            main_part += ' I committed'
        else:
            phrasing = random.randint(0, 2)
            match phrasing:
                case 0:
                    main_part += ' and committed'
                case 1:
                    main_part += ' and then committed'
                case 2:
                    main_part += ' and committed again'
        main_part += '.'



# #cmd = ['git', 'add', 'main.py']
# cmd = ['ls']
# p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
# for line in p.stdout:
#     print('Cmd output:')
#     print(line)
# return_code = p.wait()
# if return_code != 0:
#     raise ChildProcessError("Process didn't finish successfully.", cmd)
# append today commits in 'today' format and commit each one
n_times = random.randint(0, 3)
if n_times == 0:
    main_part += " Today I didn't commit."
for n in range(n_times):
    if n == 0:
        main_part += ' Today I committed.'
        git_commit()
    else:
        phrasing = random.randint(0, 2)
        match phrasing:
            case 0:
                main_part = main_part[:-1] + ' and committed.'
                git_commit()
            case 1:
                main_part = main_part[:-1] + ' and then committed.'
                git_commit()
            case 2:
                main_part = main_part[:-1] + ' and committed again.'
                git_commit()

# append how many commits we're making today as 'the next day we commit and commit...', print the whole
# commit string, write it to this file and (figure out how) make n_times commits
