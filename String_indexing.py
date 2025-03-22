# Indexing --> accessing elements of a sequence using [] (index operator) [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[::-1])

print(credit_number[-1])

last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")