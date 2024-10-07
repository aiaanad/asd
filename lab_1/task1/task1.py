import time
def insertion_sort():
    with open('input.txt', 'r') as file:
        n = -1
        for line in file:
            if n == -1:
                n = int(line)
                if not 1 <= n <= 1000:
                    with open('output.txt', 'w') as ans:  # проверка на корректность
                        ans.write('---Incorrect data---')

        else:
            input_list = [int(elem) for elem in line.split() if abs(int(elem)) <= 10e9]  # проверка на корректность
            for j in range(1, len(input_list)):
                key = input_list[j]
                i = j - 1
                while i >= 0 and input_list[i] > key:  # направление знака меняется
                    input_list[i + 1] = input_list[i]
                    i = i - 1
                input_list[i + 1] = key
            with open('output.txt', 'w') as ans:
                ans.write(' '.join(map(str, input_list)))


t_start = time.perf_counter()
print("Время работы %s:", (time.perf_counter() - t_start))
insertion_sort()
