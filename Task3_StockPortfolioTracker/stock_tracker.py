# Stock Portfolio Tracker - CodeAlpha Python Internship, Task 3
# By Waliullah Aziz
# A simple tracker: add shares, remove shares, and see the total value
# of your portfolio. Prices are sample prices saved in a table below,
# so the program works without internet. You can edit them any time.

# Sample prices for each stock (price of 1 share, in dollars)
prices = {
    "AAPL": 227.50,   # Apple
    "GOOGL": 176.30,  # Google
    "MSFT": 428.15,   # Microsoft
    "AMZN": 197.12,   # Amazon
    "TSLA": 338.40,   # Tesla
}

portfolio = {}   # the stocks you own: name -> number of shares


def show_portfolio():
    print("\n--- Your Portfolio ---")
    if len(portfolio) == 0:
        print("You do not own any stocks yet.")
        return
    total = 0
    for name in portfolio:
        value = portfolio[name] * prices[name]
        total = total + value
        print(name, "- shares:", portfolio[name],
              "| price: $", prices[name], "| value: $", round(value, 2))
    print("Total portfolio value: $", round(total, 2))


def add_stock():
    print("Stocks you can buy:", ", ".join(prices.keys()))
    name = input("Write the stock name: ").upper()
    if name not in prices:
        print("Sorry, that stock is not in the price list.")
        return
    shares = int(input("How many shares? "))
    if name in portfolio:
        portfolio[name] = portfolio[name] + shares
    else:
        portfolio[name] = shares
    print("Done. You now have", portfolio[name], "shares of", name)


def remove_stock():
    name = input("Write the stock name to remove: ").upper()
    if name not in portfolio:
        print("You do not own that stock.")
        return
    del portfolio[name]
    print(name, "removed from your portfolio.")


print("Welcome to the Stock Portfolio Tracker!")

while True:
    print("\nWhat do you want to do?")
    print("1 - See my portfolio")
    print("2 - Add a stock")
    print("3 - Remove a stock")
    print("4 - Exit")
    choice = input("Write a number: ")

    if choice == "1":
        show_portfolio()
    elif choice == "2":
        add_stock()
    elif choice == "3":
        remove_stock()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please write 1, 2, 3 or 4.")
