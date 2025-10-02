# Password Strength Checker

## Overview
This Python script evaluates the strength of a given password based on its length, character variety, and estimated entropy. It also provides an estimate of how long it would take to brute-force the password assuming a rate of 1 billion guesses per second.

## Features
- Detects presence of lowercase, uppercase, digits, and symbols.
- Calculates character pool size based on character types used.
- Computes entropy in bits using the formula:  
  `entropy = length × log₂(pool size)`
- Rates password strength from "Very Weak" to "Very Strong".
- Estimates crack time in seconds and years using brute-force simulation.

## How It Works
1. The user provides a password string.
2. The script checks for different character types.
3. It calculates the total pool size based on character diversity.
4. Entropy is computed using logarithmic formula.
5. Based on entropy, a strength rating is assigned.
6. The script estimates how long it would take to crack the password.

## Example Usage
```python
import string
import math

def password_strength(password):
    # [Function logic here...]

pwd = "12345678"
result = password_strength(pwd)

for k, v in result.items():
    if isinstance(v, dict):
        print(f"{k}:")
        for sub_k, sub_v in v.items():
            print(f"  - {sub_k}: {sub_v}")
    else:
        print(f"{k}: {v}")
