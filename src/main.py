import os
import random
import subprocess

commit_string = "I started to work here on 26.10.2022. On that day I had to clean up the development mess and the " \
                "next day I committed and then committed and the next day I didn't commit and the next day I didn't " \
                "commit and the next day I didn't commit and the next day I committed and then committed and then " \
                "committed and then committed and the next day I committed and committed after that and then " \
                "committed and committed again and then committed and the next day I committed and committed after " \
                "that and committed and then committed and the next day I committed and committed after that and " \
                "committed after that and committed after that and the next day I committed and committed again and " \
                "committed after that and then committed and the next day I committed and the next day I committed " \
                "and committed and committed again and committed after that and then committed and the next day I " \
                "didn't commit and the next day I committed and the next day I committed and the next day I " \
                "committed and committed again and committed and committed and committed again and the next day I " \
                "committed and committed again and committed and the next day I committed and committed again and " \
                "the next day I committed and committed after that and committed and committed and the next day I " \
                "committed and committed again and committed after that and committed again and the next day I " \
                "committed and then committed and the next day I committed and committed and committed after that " \
                "and committed after that and the next day I didn't commit and the next day I committed and the next " \
                "day I committed and the next day I committed and the next day I committed and committed again and " \
                "committed and the next day I didn't commit and the next day I committed and committed again and " \
                "committed and the next day I committed and committed after that and the next day I committed and " \
                "committed and then committed and then committed and then committed and the next day I committed and " \
                "committed after that and then committed and committed again and committed again and the next day I " \
                "committed and committed after that and then committed and the next day I committed and committed " \
                "again and then committed and committed after that and committed and the next day I committed and " \
                "the next day I didn't commit and the next day I didn't commit and the next day I committed and " \
                "committed after that and committed again and committed and the next day I committed and then " \
                "committed and then committed and the next day I committed and committed again and committed after " \
                "that and committed and the next day I didn't commit and the next day I didn't commit and the next " \
                "day I committed and then committed and committed again and committed again and committed after " \
                "that and the next day I committed and committed after that and then committed and committed after " \
                "that and committed after that and the next day I committed and committed and committed after that " \
                "and the next day I didn't commit and the next day I committed and committed again and then " \
                "committed and committed again and the next day I committed and then committed and committed and " \
                "committed after that and the next day I didn't commit and the next day I committed and the next day " \
                "I committed and then committed and the next day I committed and the next day I didn't commit and " \
                "the next day I committed and committed and then committed and committed again and the next day I " \
                "committed and committed and committed again and then committed and committed again and the next day " \
                "I didn't commit and the next day I didn't commit and the next day I committed and then committed " \
                "and the next day I committed and the next day I committed and then committed and committed and the " \
                "next day I committed and committed and committed after that and committed after that and then " \
                "committed and the next day I committed and committed and committed and the next day I committed and " \
                "committed again and then committed and the next day I committed and committed and the next day I " \
                "committed and committed again and then committed and committed again and the next day I committed " \
                "and then committed and committed after that and the next day I committed and the next day I didn't " \
                "commit and the next day I committed and committed again and the next day I committed and committed " \
                "and committed after that and then committed and then committed and the next day I committed and " \
                "committed again and the next day I committed and then committed and committed again and committed " \
                "again and the next day I committed and the next day I committed and committed and committed again " \
                "and the next day I committed and the next day I didn't commit and the next day I committed and then " \
                "committed and then committed and committed after that and the next day I committed and committed " \
                "again and committed after that and the next day I committed and then committed and committed after " \
                "that and the next day I committed and the next day I committed and the next day I didn't commit and " \
                "the next day I committed and then committed and committed after that and committed and the next day " \
                "I committed and committed and committed and then committed and the next day I committed and " \
                "committed after that and committed again and committed again and the next day I committed and the " \
                "next day I committed and then committed and committed after that and the next day I committed and " \
                "committed after that and committed again and committed again and the next day I didn't commit and " \
                "the next day I committed and committed and then committed and committed and the next day I " \
                "committed and the next day I committed and committed and the next day I committed and committed " \
                "after that and the next day I didn't commit and the next day I committed and the next day I didn't " \
                "commit and the next day I didn't commit and the next day I committed and committed and committed " \
                "after that and committed again and committed after that and the next day I committed and the next " \
                "day I didn't commit and the next day I committed and committed and then committed and committed " \
                "after that and committed after that and the next day I committed and committed after that and " \
                "committed again and the next day I committed and committed and committed again and then committed " \
                "and committed again and the next day I didn't commit and the next day I didn't commit and the next " \
                "day I committed and committed again and committed after that and committed after that and then " \
                "committed and the next day I committed and committed and committed again and then committed and " \
                "then committed and the next day I didn't commit and the next day I didn't commit and the next day I " \
                "didn't commit and the next day I committed and committed and committed again and then committed and " \
                "the next day I committed and then committed and the next day I committed and committed and " \
                "committed and the next day I committed and committed again and then committed and then committed " \
                "and then committed and the next day I committed and committed after that and committed again and " \
                "committed and committed again and the next day I didn't commit and the next day I didn't commit and " \
                "the next day I committed and committed and committed and the next day I didn't commit and the next " \
                "day I committed and committed again and the next day I committed and committed and committed and " \
                "committed again and the next day I didn't commit and the next day I committed and committed and " \
                "committed again and the next day I committed and committed after that and then committed and the " \
                "next day I committed and committed after that and committed again and the next day I committed and " \
                "then committed and committed again and committed after that and the next day I didn't commit and " \
                "the next day I committed and committed and committed again and the next day I committed and " \
                "committed after that and committed after that and committed again and committed again and the next " \
                "day I committed and committed after that and the next day I didn't commit and the next day I " \
                "committed and committed again and committed and committed after that and committed after that and " \
                "the next day I committed and then committed and committed after that and committed after that and " \
                "committed after that and the next day I committed and then committed and committed again and then " \
                "committed and the next day I committed and committed and committed after that and the next day I " \
                "committed and committed and committed after that and the next day I committed and committed and " \
                "committed again and committed and the next day I committed and the next day I didn't commit and the " \
                "next day I didn't commit and the next day I committed and committed again and committed. Today I " \
                "committed and committed again and committed after that and committed after that and committed after " \
                "that. and the next day I committed and the next day I committed and committed again and then " \
                "committed and committed after that and committed and the next day I committed and committed again " \
                "and committed and committed again and the next day I committed and committed and then committed and " \
                "committed after that and then committed and the next day I committed and committed again and " \
                "committed again and committed and the next day I committed and committed and committed and the next " \
                "day I committed and then committed and committed again and then committed and the next day I " \
                "committed and committed and the next day I committed and committed again and committed and the next " \
                "day I committed and committed after that and the next day I didn't commit and the next day I " \
                "committed and committed after that and committed after that and the next day I committed and the " \
                "next day I committed and committed again and committed again and committed again and the next day I " \
                "committed and committed again and the next day I committed and then committed and committed after " \
                "that and the next day I committed and the next day I didn't commit and the next day I committed and " \
                "committed after that and committed again and then committed and the next day I didn't commit and " \
                "the next day I committed and committed after that and then committed and then committed and then " \
                "committed and the next day I committed and then committed and then committed and then committed and " \
                "then committed and the next day I committed and committed after that and committed again and then " \
                "committed and the next day I committed and committed and committed after that and the next day I " \
                "committed and committed and committed and committed after that and the next day I committed and the " \
                "next day I committed and committed and committed again and the next day I committed and the next " \
                "day I committed and the next day I committed and committed and the next day I committed and " \
                "committed again and committed again and the next day I committed and committed again and the next " \
                "day I committed and committed again and committed after that and committed again and the next day I " \
                "committed and committed after that and the next day I committed and committed after that and the " \
                "next day I committed and committed after that and the next day I didn't commit and the next day I " \
                "committed and committed again and committed after that and the next day I didn't commit and the " \
                "next day I committed and committed after that and the next day I committed and committed and " \
                "committed and committed again and committed and the next day I didn't commit. Today I didn't  and " \
                "the next day I committed and committed and the next day I committed and committed and then " \
                "committed and committed after that and committed and the next day I committed and then committed " \
                "and committed after that and then committed and the next day I committed and committed after that " \
                "and the next day I committed and committed and committed again and then committed and committed " \
                "again and the next day I committed and the next day I committed and the next day I committed and " \
                "committed and committed and committed and the next day I committed and then committed and the next " \
                "day I committed and the next day I committed and then committed and the next day I committed and " \
                "committed and then committed and committed again and the next day I committed and committed after " \
                "that and committed again and committed after that and the next day I didn't commit and the next day " \
                "I committed and committed again and the next day I committed and the next day I committed and " \
                "committed and then committed and committed again and the next day I committed and committed again " \
                "and committed after that and committed after that and the next day I committed and committed and " \
                "the next day I committed and committed after that and committed again and the next day I committed " \
                "and committed after that and the next day I committed and committed and committed again and " \
                "committed again and committed again and the next day I committed and committed again and committed " \
                "after that and committed and the next day I committed and committed after that and then committed " \
                "and committed after that and the next day I committed and the next day I committed and committed " \
                "after that and committed after that and the next day I committed and committed and then committed " \
                "and then committed and committed after that and the next day I committed and the next day I " \
                "committed and the next day I committed and committed and committed and the next day I didn't commit " \
                "and the next day I committed and the next day I committed and committed after that and committed " \
                "and then committed and the next day I didn't commit and the next day I committed and committed " \
                "after that and committed and committed again and committed again and the next day I committed and " \
                "committed after that and committed again and then committed and the next day I committed and " \
                "committed after that and then committed and the next day I committed and committed again and the " \
                "next day I committed and the next day I didn't commit and the next day I committed and the next day " \
                "I committed and committed again and the next day I committed and the next day I committed and " \
                "committed again and the next day I committed and the next day I committed and committed again and " \
                "the next day I committed and committed again and committed again and committed after that and then " \
                "committed and the next day I committed and committed after that and committed and committed and the " \
                "next day I committed and committed and then committed and the next day I didn't commit and the next " \
                "day I committed and the next day I didn't commit and the next day I committed and then committed " \
                "and the next day I committed and then committed and committed again and committed after that and " \
                "the next day I committed and committed and the next day I didn't commit and the next day I didn't " \
                "commit and the next day I committed and committed after that and committed and the next day I " \
                "didn't commit and the next day I committed and committed again and then committed and committed " \
                "after that and committed and the next day I committed and committed after that and committed and " \
                "committed and the next day I committed and the next day I committed and committed after that and " \
                "committed and committed again and the next day I committed and committed and then committed and " \
                "committed after that and committed and the next day I committed and committed after that and " \
                "committed again and then committed and committed after that and the next day I committed and " \
                "committed again and committed after that and committed and committed again and the next day I " \
                "committed and then committed and then committed and committed and committed and the next day I " \
                "committed and committed after that and committed again and committed and committed again and the " \
                "next day I committed and committed after that and committed after that and committed again and " \
                "committed and the next day I committed and committed after that and committed after that and " \
                "committed again and committed and the next day I didn't commit and the next day I committed and " \
                "committed and then committed and committed after that and the next day I didn't commit and the next " \
                "day I committed and the next day I committed and committed and committed after that and the next " \
                "day I committed and the next day I committed and then committed and the next day I committed and " \
                "committed after that and then committed and the next day I committed and committed again and then " \
                "committed and committed and the next day I committed and committed and the next day I committed and " \
                "then committed and the next day I committed and the next day I committed and committed and " \
                "committed and the next day I committed and then committed and the next day I committed and " \
                "committed and the next day I committed and committed and the next day I committed and the next day " \
                "I committed and committed after that and committed after that and then committed and committed " \
                "after that and the next day I committed and then committed and committed after that and then " \
                "committed and the next day I committed and committed again. Today I committed and committed and " \
                "committed."
n_commits = 666
THIS_FILE_PATH = os.path.join(os.getcwd(), __file__)
LINE_LENGTH = 100


# for testing purposes only
def mock_function(fun):
    def inner():
        print(f'executing {fun.__name__}')
    return inner


def generate_file_lines(last_lines, includes_first_line):
    lines = []
    space_at = 0
    i = 0
    while i < len(last_lines):
        i += space_at
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
        i += LINE_LENGTH

    lines[-1] = lines[-1][:-3] + '\n'
    return lines


def change_last_day_phrasing(last_lines):
    ll = last_lines.rsplit('.', 2)
    # split the last 2 lines into the part talking about the last day commits and the remainder of the previous days part
    # (the last day commits fit into one full line - that's why we need at most 2 last lines)
    main_part, last_day_part = ll[0], ll[1]
    last_n_times = len(last_day_part.split('commit')) - 1  # how many commits in the last day
    if last_n_times == 0:
        return main_part + '.' + last_day_part + '.'
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
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return_code = p.wait()
    if return_code != 0:
        for i, line in enumerate(p.stdout):
            if i == 0:
                print('Cmd output:')
            print(line)
        print(f'Return code: {return_code}')
        raise ChildProcessError("Process didn't finish successfully.", cmd)


def git_commit():
    try:
        cmd = ['git', 'add', THIS_FILE_PATH]
        execute_subcommand(cmd)
        cmd = ['git', 'commit', '-m', f'Make a very important change No. {n_commits}']
        execute_subcommand(cmd)
    except ChildProcessError:
        raise


def git_push():
    try:
        cmd = ['git', 'push']
        execute_subcommand(cmd)
    except ChildProcessError:
        raise


def main():
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

    # helper functions to avoid duplicating the code fragments
    def insert_into_contents_and_write(text, strip_last=False):
        nonlocal last_lines, commit_string_ended
        if strip_last:
            last_lines = last_lines[:-1] + text
        else:
            last_lines = last_lines + text
        lines = generate_file_lines(last_lines, includes_first_line)
        contents[last_lines_start:commit_string_ended] = lines
        with open(THIS_FILE_PATH, 'w') as f:
            f.writelines(contents)
        # if line count got bigger due to the len of last line exceeding LINE_LENGTH, we need to update this info
        commit_string_ended += len(lines) - (commit_string_ended - last_lines_start)

    def commit():
        global n_commits
        nonlocal commit_string_ended
        n_commits += 1
        commit_count_line = f'n_commits = {n_commits}\n'
        contents[commit_string_ended:commit_string_ended+1] = [commit_count_line]
        with open(THIS_FILE_PATH, 'w') as f:
            f.writelines(contents)
        git_commit()

    # append today commits in 'Today I ... and ...' format to the commit_string and commit each change
    n_times = random.randint(0, 5)
    print(f"Today I'm gonna commit {n_times} times.")
    if n_times == 0:
        insert_into_contents_and_write(" Today I didn't commit.")
    else:
        for n in range(n_times):
            if n == 0:
                insert_into_contents_and_write(' Today I committed.')
            else:
                phrasing = random.randint(0, 3)
                match phrasing:
                    case 0:
                        insert_into_contents_and_write(' and committed.', strip_last=True)
                    case 1:
                        insert_into_contents_and_write(' and then committed.', strip_last=True)
                    case 2:
                        insert_into_contents_and_write(' and committed again.', strip_last=True)
                    case 3:
                        insert_into_contents_and_write(' and committed after that.', strip_last=True)
            print(f'Executing commit No. {n+1}...')
            commit()
        print(f'Pushing...')
        git_push()
        print('Done.')
    commit_string_lines = contents[commit_string_start:commit_string_ended]
    commit_string = ''
    for i, line in enumerate(commit_string_lines):
        if i == 0:
            commit_string += line.split('=')[1].strip().rstrip('\\').strip().strip('"')
        else:
            commit_string += line.strip().rstrip('\\').strip().strip('"')
    print('\n' + commit_string)
    print('\nPress Enter to exit...')
    input()


if __name__ == '__main__':
    main()
