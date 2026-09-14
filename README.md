# JSON Transaction Parser

A Python script that parses JSON-formatted transaction data and calculates total deposits and withdrawals.

## What it does
- Parses a JSON string into Python objects using `json.loads()`
- Prints each transaction's ID, account, and amount
- Sums up all deposits and all withdrawals separately

## How to run
```bash
python transaction_parser.py
```

## What I learned
- Using the `json` module to convert a JSON string into Python dictionaries/lists with `json.loads()`
- Accessing values in a list of dictionaries with dictionary key lookups (`txn['transaction_id']`)
- Categorizing and summing values based on a field (`type`) using a for-loop with conditionals
