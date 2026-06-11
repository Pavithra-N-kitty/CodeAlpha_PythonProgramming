def track_portfolio():
    # Hardcoded dictionary defining stock prices as specified in the internship scope
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 175,
        "AMZN": 185,
        "MSFT": 420
    }
    
    portfolio = {}
    
    print("--- Stock Portfolio Tracker ---")
    print("Available stocks to track:", ", ".join(stock_prices.keys()))
    
    while True:
        stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper().strip()
        if stock_name == "DONE":
            break
            
        if stock_name not in stock_prices:
            print("Stock not found in our system. Please try a valid symbol.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity of shares for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            
            # Save or update portfolio quantity
            portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")

    # Calculate total investment value and compile the report
    report_lines = []
    report_lines.append("=== PORTFOLIO INVESTMENT SUMMARY ===")
    
    total_portfolio_value = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        total_stock_value = qty * price
        total_portfolio_value += total_stock_value
        report_lines.append(f"{stock}: {qty} shares @ ${price} each = ${total_stock_value}")
        
    report_lines.append("------------------------------------")
    report_lines.append(f"Total Portfolio Value: ${total_portfolio_value}")
    report_lines.append("====================================")
    
    # Display the results in the terminal
    print("\n" + "\n".join(report_lines))
    
    # Save the result to a text file locally as requested by the task scope
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("\n".join(report_lines))
    
    print(f"\nReport successfully saved locally to '{filename}'")

if __name__ == "__main__":
    track_portfolio()