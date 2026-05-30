from metrics import Interval, event_precision, event_recall


def test_event_metrics_match_overlapping_intervals():
    truth = [Interval(10, 20), Interval(50, 60)]
    predicted = [Interval(12, 13), Interval(70, 80)]

    assert event_recall(predicted, truth) == 0.5
    assert event_precision(predicted, truth) == 0.5

