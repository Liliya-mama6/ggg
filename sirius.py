import urban
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global all_results
        all_results={}
    def setUp(self):
        global a, b, c
        a=urban.Runner('Усэйн', speed=10)
        b=urban.Runner('Андрей', speed=9)
        c=urban.Runner('Ник', speed=3)
    @classmethod
    def tearDownClass(cls):
        global all_results
        values=all_results.values()
        for v in values:
            print(str(v))
    def test_tournament1(self):
        global all_results
        turnir = urban.Tournament(90, a, b, c)
        all_result = turnir.start()
        self.assertTrue(all_result[max(all_result.keys())]=='Ник')
        for k in all_result.keys():#без этого цикла он мне не пойми ччто выводил
            all_result[k]=all_result[k].name
        all_results[1]=all_result
    def test_tournament2(self):
        global all_results
        turnir = urban.Tournament(90, a, c)
        all_result = turnir.start()
        self.assertTrue(all_result[max(all_result.keys())]=='Ник')
        for k in all_result.keys():
            all_result[k]=all_result[k].name
        all_results[2]=all_result
    def test_tournament3(self):
        global all_results
        turnir = urban.Tournament(90, b, c)
        all_result = turnir.start()
        self.assertTrue(all_result[max(all_result.keys())]=='Ник')
        for k in all_result.keys():
            all_result[k]=all_result[k].name
        all_results[3]=all_result
