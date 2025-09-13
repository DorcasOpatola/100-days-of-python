print(" === LOAN CALCULATOR ===")
print()
print()

total_amount_owed = 1000
for loan_years in range (10):
    total_amount_owed += 5 * total_amount_owed / 100
    print("Total amount owed is", round(total_amount_owed,2), "and this is year", loan_years)
    print()
print("After 10 years, the total loan amount owed is now", round(total_amount_owed,2))
