import os
import random
import subprocess

# TODO:
#   1. Fix splitting lines on spaces - cuts some letters at the start of new line on line break.
#       - generate_file_lines range nie updatuje i, który raz już sobie wziął - trzeba to rozbić na while
#   2. Fix calling change_last_day_phrasing on a string without any 'commit' substrings.

commit_string = "The first day I laid in bed."
n_commits = 0
THIS_FILE_PATH = os.path.join(os.getcwd(), __file__)
LINE_LENGTH = 100


def mock_function(fun):
    def inner():
        print(f'executing {fun.__name__}')
    return inner


def generate_file_lines(last_lines, includes_first_line):
    lines = []
    space_at = 0
    print(f'len: {len(last_lines)}')
    for i in range(0, len(last_lines), LINE_LENGTH):
        i += space_at
        print(f"i: {i}")
        # find the last space and break the line there
        if i + LINE_LENGTH - 1 < len(last_lines):
            j = i + LINE_LENGTH - 1
            space_at = 0
            while last_lines[j] != ' ':
                j -= 1
                space_at -= 1
        # last line
        else:
            j = len(last_lines) - 1

        if i == 0 and includes_first_line:
            line = 'commit_string = "' + last_lines[i:j+1] + '" \\\n'
        else:
            line = ' '*16 + '"' + last_lines[i:j+1] + '" \\\n'
        lines.append(line)
    # remove the line continuation sign from the last line
    lines[-1] = lines[-1][:-3] + '\n'
    return lines


def change_last_day_phrasing(last_lines):
    ll = last_lines.split('.')
    # split the last 2 lines into the part talking about the last day commits and the remainder of the previous days part
    # (the last day commits fit into one full line - that's why we need at most 2 last lines)
    main_part, last_day_part = ll[0], ll[1]
    last_n_times = len(last_day_part.split('commit')) - 1  # how many commits in the last day

    # change the last day commits from 'today' to 'the next day' format
    main_part += ' and the next day'
    if last_day_part.find("didn't") != -1:
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
    return main_part


def execute_subcommand(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return_code = p.wait()
    if return_code != 0:
        for line in p.stdout:
            print('Cmd output:')
            print(line)
        print(return_code)
        raise ChildProcessError("Process didn't finish successfully.", cmd)


@mock_function
def git_commit():
    try:
        cmd = ['git', 'add', 'main.py']
        execute_subcommand(cmd)
        cmd = ['git', 'commit', '-m', f'"Very important change No. {n_commits+1}"']
        execute_subcommand(cmd)
    except ChildProcessError:
        raise


@mock_function
def git_push():
    try:
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
                if line != '' and line.strip()[0] == '"':
                    line1 = line2
                    line2 = line
                else:
                    break
    commit_string_ended = i
    last_lines_start = max(i - 2, commit_string_start)
    # if True, the entire commit_string is 1 or 2 lines long
    includes_first_line = (last_lines_start == commit_string_start)
    # commit_string has only one line of format: 'commit_string = "..."'
    if commit_string_ended == commit_string_start + 1:
        last_lines = line2.split('=')[1].strip().strip('"')
    # last two lines of commit_string are of format: 1) 'commit_string = "..." \' 2) '"..."'
    elif commit_string_ended == commit_string_start + 2:
        last_lines = (line1.split('=')[1].strip().rstrip('\\').strip().strip('"') +
                      line2.strip().strip('"'))
    # last two lines of commit_string are of format: 1) '"..." \' 2) '"..."'
    else:
        last_lines = line1.strip().rstrip('\\').strip().strip('"') + line2.strip().strip('"')

    last_lines = change_last_day_phrasing(last_lines)

    # a helper function to avoid duplicating this code fragment
    def insert_into_contents_and_write(text, strip_last=False):
        nonlocal last_lines, commit_string_ended
        print(f'before: {last_lines}')
        if strip_last:
            last_lines = last_lines[:-1] + text
        else:
            last_lines = last_lines + text
        print(f'after: {last_lines}')
        lines = generate_file_lines(last_lines, includes_first_line)

        print_contents = [s.lstrip(' ') for s in contents]
        print(f'contents:\n{print_contents}')
        contents[last_lines_start:commit_string_ended] = lines
        with open(THIS_FILE_PATH, 'w') as f:
            f.writelines(contents)
        # if line count got bigger due to the last line exceeding LINE_LENGTH chars, we need to update this info
        commit_string_ended += len(lines) - (commit_string_ended - last_lines_start)

    # append today commits in 'today' format and commit each one
    n_times = random.randint(0, 5)
    n_times = 4
    print(n_times)
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
        git_push()


if __name__ == '__main__':
    main()
