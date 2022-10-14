import os
import random
import subprocess

commit_string = 'test.'
n_commits = 0
THIS_FILE_PATH = os.path.join(os.getcwd(), __file__)
LINE_LENGTH = 100


def execute_subcommand(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return_code = p.wait()
    if return_code != 0:
        for line in p.stdout:
            print('Cmd output:')
            print(line)
        print(return_code)
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


def main():
    print(THIS_FILE_PATH)
    with open(THIS_FILE_PATH, 'r') as f:
        contents = f.readlines()
        # get two last lines consisting of the ending part of commit_string
        line1 = ''
        line2 = ''
        commit_string_start = None
        for i, line in enumerate(contents):
            if line.split('=')[0].strip() == 'commit_string':
                commit_string_start = i
                line2 = line
            elif commit_string_start is not None:
                line = line.strip()
                if line != '' and line.strip()[0] == '+':
                    line1 = line2
                    line2 = line
                else:
                    break
    commit_string_ended = i
    # value of commit_string is assigned only in the first line 'commit_string = ...'
    if commit_string_ended == commit_string_start + 1:
        last_lines = line2.split('=')[1].strip().strip('\'')
    # value of commit_string is assigned in the first line 'commit_string = ...' and the following line
    elif commit_string_ended == commit_string_start + 2:
        last_lines = line1.split('=')[1].strip().strip('\'') + line2.split('+')[1].strip().strip('\'')
    # last two lines assigning value to commit_string  both are of format '+ ...'
    else:
        last_lines = line1.split('+')[1].strip().strip('\'') + line2.split('+')[1].strip().strip('\'')

    ll = last_lines.split('.')
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
                phrasing = random.randint(0, 3)
                match phrasing:
                    case 0:
                        main_part += ' and committed'
                    case 1:
                        main_part += ' and then committed'
                    case 2:
                        main_part += ' and committed again'
                    case 3:
                        main_part += ' and committed after that'
            main_part += '.'

    # a helper function to avoid duplicating this code fragment
    def insert_into_contents_and_write(text, strip_last=False):
        nonlocal main_part, commit_string_ended
        if strip_last:
            main_part[:-1] += text
        else:
            main_part += text
        lines = [main_part[i:i+LINE_LENGTH] for i in range(0, len(main_part), LINE_LENGTH)]
        contents[commit_string_start:commit_string_ended] = lines
        f.writelines(contents)
        # if line count got bigger due to the last line exceeding LINE_LENGTH chars, we need to update this info
        commit_string_ended += len(last_lines) - (commit_string_ended - commit_string_start)

    # append today commits in 'today' format and commit each one
    with open(THIS_FILE_PATH, 'w') as f:
        n_times = random.randint(0, 5)
        if n_times == 0:
            insert_into_contents_and_write(" Today I didn't commit.")
        for n in range(n_times):
            if n == 0:
                insert_into_contents_and_write(' Today I committed.')
                git_commit()
            else:
                phrasing = random.randint(0, 3)
                match phrasing:
                    case 0:
                        insert_into_contents_and_write(' and committed.', strip_last=True)
                        git_commit()
                    case 1:
                        insert_into_contents_and_write(' and then committed.', strip_last=True)
                        git_commit()
                    case 2:
                        insert_into_contents_and_write(' and committed again.', strip_last=True)
                        git_commit()
                    case 3:
                        insert_into_contents_and_write(' and committed after that.', strip_last=True)
                        git_commit()


if __name__ == '__main__':
    main()
