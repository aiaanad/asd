# Задание №3 по выбору: Сортировка вставкой по убыванию
Студент(ка) ИТМО, Данилова Айаана Васильевна

## Вариант 6

## Задание
**Перепишите процедуру Insertion-sort для сортировки в невозрастающем порядке вместо неубывающего с использованием процедуры Swap.
Формат входного и выходного файла и ограничения - как в задаче 1.
Подумайте, можно ли переписать алгоритм сортировки вставкой с использованием рекурсии?**

• Формат входного файла (input.txt). 

В первой строке входного файла содержится число n (1 ≤ n ≤ 10^3) — число элементов в массиве. Во второй
строке находятся n различных целых чисел, по модулю не превосходящих
10^9

• Формат выходного файла (output.txt).

Одна строка выходного файла с
отсортированным массивом. Между любыми двумя числами должен стоять
ровно один пробел.


## Input / Output 

| Input             | Output            |
|-------------------|-------------------|
| 31 41 59 26 41 58 | 59 58 41 41 32 26 |
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
   cd asd/lab_1
   ```
3. Запустите программу:
   ```bash
   for f in task*/src/*.py; do python "$f"; done 
   ```

4. Запуск тестов:
   ```bash
   python -m unittest task3.tests.test_task3
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    python -m unittest task3.tests.test_task3
```
