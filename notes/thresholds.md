# Thresholding Notes

Thresholding is part of the model.

## Static Threshold

Works when the score distribution is stable. Fails under drift.

## Rolling Quantile

Useful for seasonal score distributions, but can absorb slow anomalies into the baseline.

## Validation-Calibrated Threshold

Requires a clean validation period. If validation includes anomalies, the threshold may become too permissive.

## Reporting

Always report:

- score definition
- threshold rule
- cooldown window
- event matching tolerance
- whether labels are point-level or interval-level

