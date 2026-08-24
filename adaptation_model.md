# Adaptation Model

## Episode

An adaptation episode contains:
- reference state
- damaged state
- adapted state
- reference function
- damaged function
- adapted function
- adaptation cost
- invariant tests

## Key distinction

A system may have:

`high functional recovery`

and simultaneously:

`high transformation distance`

This is not automatically failure. It may represent successful compensatory adaptation.

## Evaluation classes

- FAILED
- PARTIAL_RECOVERY
- RESTORED
- TRANSFORMED_RECOVERY
- IMPROVED_AFTER_TRANSFORMATION

## Experimental requirement

Adaptation should be tested on held-out disturbances to distinguish genuine learning from memorized repair.
