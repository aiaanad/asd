import pathlib


def f_read(current_task):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'input.txt')
    args = ()
    f = open(path, 'r')
    for line in f:
        line = line.rstrip().split()
        if args == ():
            for elem in line:
                args += (int(elem),)
        else:
            args += ([int(elem) if elem.isdigit() else elem for elem in line],)
    f.close()
    print(args)
    return args


def f_write(current_task, answer):
    path = pathlib.Path(__file__).parent.parent.joinpath(current_task, 'txtf', 'output.txt')
    f = open(path, 'a')
    if type(answer) is not str:
        if len(answer) > 1:
            answer = '\n'.join(map(str, answer)) + '\n'
        else:
            answer = str(answer[0]) + '\n'
    f.write(answer)
    f.close()


def work(file, func, *dop):
    current_lab = file.parts[-4]
    current_task = file.stem
    input_data = f_read(current_task)
    if len(dop) != 0:
        arr = list(input_data) if type(input_data[1]) is not list else input_data[1]
        args = (arr, 0, len(arr) - 1)
    else:
        args = tuple(input_data)
    result = func(*args)
    f_write(current_task, result)
    print(
        f'''LAB NUMBER: {current_lab[4:]}
            TASK NUMBER: {current_task[4:]}
                    INPUT DATA: {args}
                    OUTPUT DATA: {result}

            ''')

