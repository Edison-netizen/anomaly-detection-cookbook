from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from thresholds import intervals_from_scores, robust_z_scores


def main() -> None:
    values = [1.0, 1.1, 0.9, 1.2, 1.0, 5.8, 6.1, 1.1, 1.0, 0.8]
    scores = robust_z_scores(values)
    intervals = intervals_from_scores(scores, threshold=3.5, cooldown=1)
    print("scores:", [round(score, 2) for score in scores])
    print("intervals:", intervals)


if __name__ == "__main__":
    main()

