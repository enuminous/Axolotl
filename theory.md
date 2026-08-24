# AXOLOTL Theory

## 1. Problem

Recovery does not always mean returning to the original state.

Biological, organizational, and computational systems can sometimes compensate for damage by reorganizing around it.

AXOLOTL distinguishes:
- restoration: return toward the old state,
- adaptation: improve after loss,
- transformation: reach function through a materially different state.

## 2. Reference and damaged states

Healthy reference:

`x_0`

Damaged state:

`x_d`

Adapted state after learning:

`x_a`

## 3. Loss severity

For pre-loss function `Q_0` and damaged function `Q_d`:

`L = max(0, (Q_0-Q_d)/(Q_0+eps))`

## 4. Functional recovery

`R = (Q_a-Q_d)/(Q_0-Q_d+eps)`

`R=1` means the lost function was recovered.

Values above 1 indicate improvement beyond the original functional level.

## 5. Transformation distance

`T = dist(x_a,x_0)`

A high-functioning adapted state with nontrivial `T` is evidence of compensatory reorganization rather than simple rollback.

## 6. Adaptation gain

`G = Q_a-Q_d`

## 7. Learning efficiency

For adaptation cost `C`:

`E = G/(C+eps)`

## 8. Invariant retention

Transformation is constrained by critical invariants.

`I = passed_invariants/total_invariants`

## 9. Adaptive resilience

Candidate normalized composite:

`A = w1*recovery + w2*invariant_retention + w3*learning_efficiency + w4*useful_transformation`

Transformation is useful only when function and invariants remain strong.

## 10. EFMW interpretation

The EFMW-inspired component is recursive evaluation of the path:

`loss -> altered relations -> learning -> transformed state -> renewed function`

## 11. Falsifiable prediction

AXOLOTL should add value where successful recovery can occur through a new configuration.

If endpoint performance and conventional adaptation metrics explain outcomes equally well, AXOLOTL adds no justified complexity.
