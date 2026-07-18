# Lifecycle Transition Validator

> **Evidence classification:** New synthetic demonstration.

## Purpose

Test whether synthetic lifecycle transitions follow an explicit set of allowed movements and ownership rules.

## Checks

- Missing required fields
- Unknown stages
- Invalid stage transitions
- Missing owner
- Recycling without a reason

## Run

```bash
python validator.py sample_transitions.csv
```

## Test

```bash
python -m unittest test_validator.py
```

## Governance principle

The rules are deliberately visible in `ALLOWED_TRANSITIONS`. A real organisation would approve its own stage meanings, transitions and exceptions before configuration.

The validator supports governance; it does not decide what the lifecycle should be.

## Data boundary

The sample file is fictional and contains no customer, employee or production data.
