# Лабораторная работа №4: Стек, очередь, связанный список


**Студентка ИТМО,  Данилова Айаана Васильевна  465714**  
## Вариант 6
### Навигация

- [ ] [Задача 2 - Очередь](task2)
- [ ] [Задача 3 - Скобочная последовательность. Версия 1](task3)
- [ ] [Задача 5 - Стек с максимумом](task5)
- [ ] [Задача 12 - Строй новобранцев](task12)
- [ ] [Задача 13 - Реализация стека, очереди и связанных списков](task13)


## Описание
В этой лабораторной работе студенты ознакомятся с алгоритмом быстрой сортировки и сортировками за линейное время. 
Основные задачи включают изучение более эффективных относительно изученных ранее сортировок, их реализация и практика в применении для решения варианта, и при желании 3 дополнительных заданий по выбору, написание тестов к ним, создание директории лабораторной согласно требуемой структуре, написание документации к каждой задаче, а также одной единой для всей лабораторной. 


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/aiaanad/asd.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd folder/where/cloned/asd
   ```
3. **Запуск всех задач**
    ```bash
        for f in lab_4/task*/src/task*; do f=${f%.py}; python -m ${f////.}; done

4. **Запуск всех тестов задач**
    ```bash
        for f in lab_4/task*/tests/test_task*; do f=${f%.py}; python -m unittest ${f////.}; done

## Тестирование
Для запуска тестов выполните:
```bash
      for f in lab_4/task*/tests/test_task*; do f=${f%.py}; python -m unittest ${f////.}; done
```