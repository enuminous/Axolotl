import unittest
from axolotl import AxolotlEvaluator, AdaptationEpisode

class TestAxolotl(unittest.TestCase):
    def test_full_function_recovery(self):
        ep=AdaptationEpisode({"a":1},{"a":0},{"a":1},1,0,1,1)
        out=AxolotlEvaluator().evaluate(ep)
        self.assertAlmostEqual(out["functional_recovery"],1.0,places=6)

    def test_transformation_detected(self):
        ep=AdaptationEpisode({"a":1,"b":0},{"a":0,"b":0},{"a":0,"b":1},1,0,1,1)
        out=AxolotlEvaluator().evaluate(ep)
        self.assertGreater(out["transformation_distance"],0)

    def test_adaptation_beats_failure(self):
        ev=AxolotlEvaluator()
        fail=AdaptationEpisode({"a":1},{"a":0},{"a":0.1},1,0.2,0.3,1)
        adapt=AdaptationEpisode({"a":1},{"a":0},{"a":0.9},1,0.2,0.95,1)
        self.assertGreater(ev.evaluate(adapt)["adaptive_resilience"],ev.evaluate(fail)["adaptive_resilience"])

if __name__=="__main__":
    unittest.main()
