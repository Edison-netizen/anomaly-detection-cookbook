from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Interval:
    start: int
    end: int

    def overlaps(self, other: "Interval") -> bool:
        return self.start <= other.end and other.start <= self.end


def event_recall(predicted: Iterable[Interval], truth: Iterable[Interval]) -> float:
    predictions = list(predicted)
    events = list(truth)
    if not events:
        return 0.0
    matched = sum(any(pred.overlaps(event) for pred in predictions) for event in events)
    return matched / len(events)


def event_precision(predicted: Iterable[Interval], truth: Iterable[Interval]) -> float:
    predictions = list(predicted)
    events = list(truth)
    if not predictions:
        return 0.0
    matched = sum(any(pred.overlaps(event) for event in events) for pred in predictions)
    return matched / len(predictions)

