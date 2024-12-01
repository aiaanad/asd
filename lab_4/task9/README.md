# Задание №9 по выбору:  Поликлиника

Студент(ка) ИТМО, Данилова Айаана Васильевна

## Вариант 6

## Задание 
Очередь в поликлинике работает по сложным правилам. Обычные пациенты
при посещении должны вставать в конец очереди. Пациенты, которым "только
справку забрать встают ровно в ее середину, причем при нечетной длине очереди
они встают сразу за центром. Напишите программу, которая отслеживает порядок
пациентов в очереди.

• Формат входного файла (input.txt). 

В первой строке записано одно целое
число n ( 1 ≤ n ≤ 10^5) - число запросов к вашей программе. В следующих
n строках заданы описания запросов в следующем формате:

– «+ i» – к очереди присоединяется пациент i (1 ≤ i ≤ N) и встает в ее
конец;

– «* i» – пациент i встает в середину очереди ( 1 ≤ i ≤ N);

– «-» – первый пациент в очереди заходит к врачу. Гарантируется, что на
момент каждого такого запроса очередь будет не пуста.


• Формат выходного файла (output.txt). 

Для каждого запроса третьего типа в отдельной строке выведите номер пациента, который должен зайти к
шаманам.

Для каждого запроса max выведите
(в отдельной строке) максимальное значение стека.
## Input / Output 

| Input                                                               | Output                    |
|---------------------------------------------------------------------|---------------------------|
| 7<br/>+1<br/>+2<br/>-<br/>+3<br/>+4<br/>-<br/>-                     | 1<br/>2<br/>3             | 
| 10<br/>+1<br/>+2<br/>*3<br/>-<br/>+4<br/>*5<br/>-<br/>-<br/>-<br/>- | 1<br/>3<br/>2<br/>5<br/>4 |               

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
   python -m lab_4.task9.src.task9
   ```

4. Запуск тестов:
   ```bash
   python -m unittest lab_4.task9.tests.test_task9
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    python -m unittest lab_4.task9.tests.test_task9
```