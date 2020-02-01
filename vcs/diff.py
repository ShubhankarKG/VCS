from collections import namedtuple
import sys
from init import check_init

Keep = namedtuple('Keep', ['line'])
Insert = namedtuple('Insert', ['line'])
Delete = namedtuple('Delete', ['line'])

Frontier = namedtuple('Frontier', ['x', 'history'])


def myers_diff(a_lines, b_lines):
    frontier = {1: Frontier(0, [])}

    def one(idx):
        return idx - 1

    a_max = len(a_lines)
    b_max = len(b_lines)
    for d in range(0, a_max+b_max+1):
        for k in range(-d, d+1, 2):
            go_down = (k == -d or (k != d and frontier[k-1].x < frontier[k+1].x))
            if go_down:
                old_x, history = frontier[k+1]
                x = old_x
            else:
                old_x, history = frontier[k-1]
                x = old_x + 1

            history = history[:]
            y = x - k
            if 1 <= y <= b_max and go_down:
                history.append(Insert(b_lines[one(y)]))
            elif 1 <= x <= a_max:
                history.append(Delete(a_lines[one(x)]))
            while x < a_max and y < b_max and a_lines[one(x + 1)] == b_lines[one(y + 1)]:
                x += 1
                y += 1
                history.append(Keep(a_lines[one(x)]))

            if x >= a_max and y >= b_max:
                # If we're here, then we've traversed through the bottom-left corner,
                # and are done.
                return history
            else:
                frontier[k] = Frontier(x, history)

        assert False, 'Could not find edit script'


def diff():
    if check_init():
        try:
            _, a_file, b_file = sys.argv
        except ValueError:
            print(sys.argv[0], '<FILE 1>', '<FILE 2>')
            return 1
        with open(a_file) as a_handle:
            a_lines = [line.rstrip() for line in a_handle]
        with open(b_file) as b_handle:
            b_lines = [line.rstrip() for line in b_handle]
        diff_var = myers_diff(a_lines, b_lines)
        for each_element in diff_var:
            if isinstance(each_element, Keep):
                print(' ' + each_element.line)
            elif isinstance(each_element, Insert):
                print('++ ' + each_element.line)
            else:
                print('-- ' + each_element.line)
    else:
        print("Please initialize repo with \"vcs init\" first!")
