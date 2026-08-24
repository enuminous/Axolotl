# AXOLOTL Architecture

## Pipeline

1. Healthy-State Snapshotter
2. Loss Injector / Incident Recorder
3. Damage Quantifier
4. Adaptation Episode Recorder
5. Functional Recovery Analyzer
6. Transformation-Distance Engine
7. Invariant Validator
8. Learning-Efficiency Analyzer
9. Adaptive-Resilience Scorer
10. Audit Reporter

## Inputs

- healthy state
- damaged state
- adapted state
- functional scores
- learning/adaptation cost
- critical invariants

## Outputs

```json
{
  "loss_severity": 0.65,
  "adaptation_gain": 0.57,
  "functional_recovery": 0.88,
  "transformation_distance": 0.31,
  "invariant_retention": 1.0,
  "learning_efficiency": 0.71,
  "adaptive_resilience": 0.86
}
```

## Design principle

AXOLOTL does not penalize a recovered system merely because it no longer resembles its original configuration.

The question is whether transformation restores useful, bounded function.

## Integration

PHOENIX evaluates restoration toward a known healthy state.

AXOLOTL handles the complementary case where recovery requires becoming different.

RHINO supplies severe perturbations.

HEDGEHOG can test whether the learned adaptation generalizes out of sample.
