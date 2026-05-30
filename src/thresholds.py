from __future__ import annotations

from statistics import median
from typing import Sequence

from metrics import Interval


def robust_z_scores(values: Sequence[float]) -> list[float]:
    """Return median/MAD based robust z-scores for anomaly scoring."""
    if not values:
        raise ValueError("values must not be empty")

    center = median(values)
    deviations = [abs(value - center) for value in values]
    mad = median(deviations)
    if mad == 0:
        return [0.0 for _ in values]
    return [0.6745 * (value - center) / mad for value in values]


def intervals_from_scores(scores: Sequence[float], threshold: float, cooldown: int = 0) -> list[Interval]:
    """Convert point scores into event intervals with optional cooldown merging."""
    intervals: list[Interval] = []
    active_start: int | None = None
    last_hit: int | None = None

    for idx, score in enumerate(scores):
        hit = abs(score) >= threshold
        if hit and active_start is None:
            active_start = idx
        if hit:
            last_hit = idx
        if active_start is not None and last_hit is not None and idx - last_hit > cooldown:
            intervals.append(Interval(active_start, last_hit))
            active_start = None
            last_hit = None

    if active_start is not None and last_hit is not None:
        intervals.append(Interval(active_start, last_hit))
    return intervals

