def calculate_profit_or_loss(C, S):
    if C < S:
        # There is a profit
        return 1, S - C  # Return 1 for profit and the profit amount
    else:
        # There is a loss
        return -1, C - S  # Return -1 for loss and the loss amount

# Input cost price (C) and selling price (S)
C = int(input("Enter the cost price"))
S = int(input("Enter the selling price"))

# Calculate profit or loss and total amount
profit_or_loss, total_amount = calculate_profit_or_loss(C, S)

# Output the results
print(profit_or_loss)
print(total_amount)

