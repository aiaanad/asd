# Задание №6 по варианту: Наибольшая возрастающая подпоследовательность

Студент(ка) ИТМО, Данилова Айаана Васильевна

## Вариант 6

## Задание 
Дана последовательность, требуется найти ее наибольшую возрастающаю подпоследовательность.

• Формат ввода / входного файла (input.txt). 

В первой строке входных
данных задано целое число n – длина последовательности (1 ≤ n ≤ 300000).
Во второй строке задается сама последовательность. Числа разделяются
пробелом.
Элементы последовательности – целые числа, не превосходящие по модулю
10^9.

– Подзадача 1 (полегче). n ≤ 5000.

– Общая подзадача. n ≤ 300000.

• Формат вывода / выходного файла (output.txt). 

В первой строке выведите длину наибольшей возрастающей подпоследовательности, а во второй
строке выведите через пробел саму наибольшую возрастающую подпоследовательность данной последовательности. Если ответов несколько - выведите
любой.

## Input / Output 

| Input                 | Output         |
|-----------------------|----------------|
| 6 <br/> 3 29 5 5 28 6 | 3 <br/> 3 5 28 |

## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/aiaanad/asd.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd folder/where/cloned/asd
   ```
3. Запустите программу:
   ```bash
   python -m lab_7.task6.src.task6
   ```

4. Запуск тестов:
   ```bash
   python -m unittest lab_7.task6.tests.test_task6
   ```