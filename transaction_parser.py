import json

raw_json_data = '''
[
    {"transaction_id": "T001", "account": "Checking", "amount": 250.00, "type": "deposit"},
    {"transaction_id": "T002", "account": "Savings", "amount": -45.50, "type": "withdrawal"},
    {"transaction_id": "T003", "account": "Checking", "amount": -120.00, "type": "withdrawal"},
    {"transaction_id": "T004", "account": "Checking", "amount": 500.00, "type": "deposit"}
]
'''

# Step 1: Parse JSON string into Python objects
transactions = json.loads(raw_json_data)

# Step 2: Print each transaction
for txn in transactions:
    print(f"ID: {txn['transaction_id']} | Account: {txn['account']} | Amount: ${txn['amount']}")

# Step 3: Calculate totals (simple for-loop version)
total_deposits = 0
total_withdrawals = 0

for t in transactions:
    if t['type'] == 'deposit':
        total_deposits += t['amount']
    elif t['type'] == 'withdrawal':
        total_withdrawals += t['amount']

print(f"\nTotal deposits: ${total_deposits}")
print(f"Total withdrawals: ${total_withdrawals}")