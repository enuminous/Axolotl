# AXOLOTL: Adaptive eXperimental Observation of Loss, Optimization, Transformation and Learning

## Abstract

AXOLOTL is an experimental framework for evaluating adaptive recovery after capability loss. Unlike restoration-centered recovery models, AXOLOTL explicitly permits successful post-loss states to differ materially from the original configuration. It measures loss severity, adaptation gain, functional recovery, transformation distance, invariant retention, learning efficiency, and adaptive resilience.

## 1. Motivation

A system may recover by rebuilding what was lost, or by reorganizing around the loss.

These are different phenomena.

## 2. Model

Healthy state:

`x_0`

Damaged state:

`x_d`

Adapted state:

`x_a`

Loss:

`L=(Q_0-Q_d)/Q_0`

Adaptation gain:

`G=Q_a-Q_d`

Functional recovery:

`R=(Q_a-Q_d)/(Q_0-Q_d)`

Transformation:

`T=dist(x_a,x_0)`

Learning efficiency:

`E=G/cost`

## 3. Interpretation

High recovery + low transformation suggests restoration.

High recovery + high transformation suggests compensatory adaptation.

Low recovery indicates unsuccessful adaptation regardless of novelty.

## 4. Baselines

- endpoint performance
- conventional resilience metrics
- rollback/restoration score
- online-learning regret
- adaptation cost
- transfer/generalization performance

## 5. Ablations

- endpoint only
- no transformation term
- no invariant checks
- no cost term
- training disturbances only
- no held-out adaptation test

## 6. Falsification

If conventional adaptation and recovery metrics explain future function equally well under matched information and compute, AXOLOTL's additional structure is not justified.

## 7. Claim boundary

AXOLOTL is a computational evaluation framework. It does not imply biological regeneration or unrestricted autonomous self-improvement.
