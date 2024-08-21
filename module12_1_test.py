import module12_1 as rn
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_1 = rn.Runner('Олег')
        for walk in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)



    def test_run(self):
        runner_2 = rn.Runner('Макс')
        for run_ in range(10):
            runner_2.run_()
        self.assertEqual(runner_2.distance, 100)



    def test_challenge(self):
        runner_3 = rn.Runner('Макар')
        runner_4 = rn.Runner('Вика')
        for run_ in range(10):
            runner_3.run_()
        for run_ in range(10):
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)



if __name__ == "__main__":
    unittest.main()