import unittest
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from metrics import Interval, event_precision, event_recall


class EventMetricTests(unittest.TestCase):
    def test_event_metrics_match_overlapping_intervals(self):
        truth = [Interval(10, 20), Interval(50, 60)]
        predicted = [Interval(12, 13), Interval(70, 80)]

        self.assertEqual(event_recall(predicted, truth), 0.5)
        self.assertEqual(event_precision(predicted, truth), 0.5)


if __name__ == "__main__":
    unittest.main()
