import unittest
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from metrics import Interval
from thresholds import intervals_from_scores, robust_z_scores


class ThresholdTests(unittest.TestCase):
    def test_robust_z_scores_flags_outlier_shape(self):
        scores = robust_z_scores([1.0, 1.1, 0.9, 10.0, 1.0])
        self.assertGreater(scores[3], 3.5)

    def test_intervals_merge_with_cooldown(self):
        intervals = intervals_from_scores([0, 4, 0, 4, 0, 0], threshold=3, cooldown=1)
        self.assertEqual(intervals, [Interval(1, 3)])


if __name__ == "__main__":
    unittest.main()
