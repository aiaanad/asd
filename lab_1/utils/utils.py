import pathlib


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def convert_one_elem(string):
    if is_number(string):
        if '.' in string:
            return float(string)
        return int(string)

    return string.rstrip()


def convert_list(string):
    list_ = []
    for elem in string.rstrip().split():
        list_.append(convert_one_elem(elem))
    return list_


def is_first_numbers(string):
    if len(string.split()) <= 2:
        l_ = string.split()
        if is_number(l_[0]) and is_number(l_[1]):
            return True
    return False


def convert_first_numbers(string):
    nums = convert_list(string)
    res = ()
    for elem in nums:
        res += (elem,)
    return res


def convert_line(string):
    if len(string.split()) == 1:
        return (convert_one_elem(string),)

    return (convert_list(string),)


def f_read(current_task):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'input.txt')
    args = ()
    f = open(path, 'r')
    for line in f:
        args += convert_line(line)
    f.close()
    return args


def f_write(current_task, answer):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'output.txt')
    f = open(path, 'w')
    if type(answer) is list:
        answer = ' '.join(map(str, answer)) + '\n'
    elif type(answer) is int:
        answer = str(answer) + '\n'
    elif type(answer) is tuple:
        answer = ' '.join(map(str, answer))
    f.write(answer)
    f.close()


def f_print(cur_lab, cur_task, args, res):
    print(
        f'''LAB NUMBER: {cur_lab[4:]}
            TASK NUMBER: {cur_task[4:]}
                    INPUT DATA: {args}
                    OUTPUT DATA: {res}

            ''')


def work(current_lab, current_task, func, dop=None):
    input_data = f_read(current_task)
    args = ()
    if dop is not None:
        if dop == 0:
            args = (input_data[1],) + (0,) + (len(input_data[1]) - 1,)
        if dop == 1:
            input_data[0][0] = [input_data[0][0] // 10 ** i % 10 for i in range(len(str(input_data[0][0])) - 1, -1, -1)]
            input_data[0][1] = [input_data[0][1] // 10 ** i % 10 for i in range(len(str(input_data[0][1])) - 1, -1, -1)]
            args = input_data[0][0], input_data[0][1]
    else:
        args = input_data

    result = func(*args)
    f_write(current_task, result)
    f_print(current_lab, current_task, args, result)



