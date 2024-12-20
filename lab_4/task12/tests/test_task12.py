import time
import unittest
import tracemalloc
from lab_4.task12.src.task12 import main


class TestFormation(unittest.TestCase):
    def test_should_formation_args1(self):
        # given
        args = (3, 3, ['left', 2, 1], ['right', 3, 1], ['name', 1])
        expected_result = ['2 3']
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        main(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_formation_args2(self):
        # given
        args = (3, 4, ['left', 2, 1], ['right', 3, 1], ['leave', 1], ['name', 2])
        expected_result = ['0 3']
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        main(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_should_formation_max_args(self):
        # given
        args = (75000, 75000)
        expected_result = ['3 0', '74998 74997']
        expected_time = 5
        expected_memory = 256
        for i in range(2, 75000):
            if i % 2 == 0:
                args += (['left', i, i - 1],)
            else:
                args += (['right', i, i - 1],)
        args += (['name', 1],)
        args += (['name', 74999],)

        # when
        start_time = time.perf_counter()
        result = main(*args)
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        main(*args)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
