# Anomaly Detection Cookbook

Practical recipes for time-series anomaly detection.

This repository focuses on the parts that usually decide whether anomaly detection works outside a demo: thresholding, temporal aggregation, delayed labels, noisy ground truth, and evaluation that does not reward alert spam.

## Topics

- Point anomaly vs contextual anomaly
- Reconstruction error baselines
- Forecasting residual baselines
- Threshold calibration
- Event-level metrics
- Alert deduplication and cooldown windows

## Recipes

```text
src/metrics.py       event-aware precision and recall helpers
notes/thresholds.md  thresholding patterns and failure cases
```

## Principle

Anomaly detection is less about a clever score and more about a defensible decision rule.

