import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol}.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
            print(f"Removed {quantity} shares of {symbol}.")
        else:
            print(f"Cannot remove {quantity} shares of {symbol}.")

    def get_stock_price(self, symbol):
        stock = yf.Ticker(symbol)
        return stock.history(period='1d')['Close'][0]

    def get_portfolio_value(self):
        total_value = 0.0
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            total_value += price * quantity
        return total_value

    def show_portfolio(self):
        print("Current Portfolio:")
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            print(f"{symbol}: {quantity} shares @ ₹{price:.2f} each")
        print(f"Total Portfolio Value: ${self.get_portfolio_value():.2f}")


def main():
    portfolio = StockPortfolio()

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.show_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()