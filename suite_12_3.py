import unittest
import test12_3

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test12_3.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)