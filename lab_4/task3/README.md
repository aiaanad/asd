# Задание №3 по варианту:  Скобочная последовательность. Версия 1

Студент(ка) ИТМО, Данилова Айаана Васильевна

## Вариант 6

## Задание 
Последовательность A, состоящую из символов из множества «(», «)», «[» и
«]», назовем правильной скобочной последовательностью, если выполняется
одно из следующих утверждений:

• A – пустая последовательность;

• первый символ последовательности A – это «(», и в этой последовательности
существует такой символ «)», что последовательность можно представить
как A = (B)C, где B и C – правильные скобочные последовательности;

• первый символ последовательности A – это «[», и в этой последовательности
существует такой символ «]», что последовательность можно представить
как A = (B)C, где B и C – правильные скобочные последовательности.

Так, например, последовательности «(())» и «()[]» являются правильными скобочными последовательностями, а последовательности «[)» и «((» таковыми не
являются.
Входной файл содержит несколько строк, каждая из которых содержит последовательность символов «(», «)», «[» и «]». Для каждой из этих строк выясните,
является ли она правильной скобочной последовательностью.

• Формат входного файла (input.txt). 

Первая строка входного файла содержит число N (1 ≤ N ≤ 500) – число скобочных последовательностей,
которые необходимо проверить. Каждая из следующих N строк содержит
скобочную последовательность длиной от 1 до 104
включительно. В каждой из последовательностей присутствуют только скобки указанных выше
видов.
3

• Формат выходного файла (output.txt). 

Для каждой строки входного файла
(кроме первой, в которой записано число таких строк) выведите в выходной
файл «YES», если соответствующая последовательность является правильной скобочной последовательностью, или «NO», если не является.

## Input / Output 

| Input                                             | Output                                      |
|---------------------------------------------------|---------------------------------------------|
| 5</br>()() </br> ([]) </br>([)] </br>((]] </br>)( | YES</br> YES </br> NO </br> NO</br> NO</br> | |        |

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
   python -m lab_4.task3.src.task3
   ```

4. Запуск тестов:
   ```bash
   python -m unittest lab_4.task3.tests.test_task3
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    python -m unittest lab_4.task3.tests.test_task3
```