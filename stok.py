# --- Simple Stock Tracker Program ---

# Hardcoded dictionary for stock prices (you can modify these)
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 140,  # Google
    "MSFT": 320,   # Microsoft
    "AMZN": 130    # Amazon
}

# Display available stocks
print("Available Stocks and Prices (USD):")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter the number of stocks you want to add:")
n = int(input("How many stocks do you own? "))

portfolio = {}  # To store user's stocks and quantities

# User input for stocks and quantities
for i in range(n):
    stock_name = input(f"\nEnter stock symbol #{i+1}: ").upper()
    if stock_name not in stock_prices:
        print("❌ Stock not found! Please choose from the available list.")
        continue
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    portfolio[stock_name] = quantity

# Calculate total investment
total_value = 0
for stock, qty in portfolio.items():
    total_value += stock_prices[stock] * qty

# Display total investment
print("\n--- Investment Summary ---")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock] * qty}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to file
save_option = input("\nDo you want to save the result? (yes/no): ").lower()
if save_option == "yes":
    file_type = input("Save as .txt or .csv? ").lower()
    
    if file_type == "txt":
        with open("stock_investment.txt", "w") as f:
            f.write("--- Investment Summary ---\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value: ${total_value}")
        print("✅ Saved to stock_investment.txt")
    
    elif file_type == "csv":
        import csv
        with open("stock_investment.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_value])
        print("✅ Saved to stock_investment.csv")
    else:
        print("❌ Invalid file type selected.")