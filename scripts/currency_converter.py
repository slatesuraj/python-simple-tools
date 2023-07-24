import argparse
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self):
        self.currency_rates = CurrencyRates()

    def convert(self, amount, from_currency, to_currency):
        try:
            converted_amount = self.currency_rates.convert(from_currency, to_currency, amount)
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        except ValueError:
            print("Invalid currency code(s). Please check the currency codes and try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Currency Converter CLI')
    parser.add_argument('amount', type=float, help='Specify the amount to convert')
    parser.add_argument('from_currency', help='Specify the currency code to convert from')
    parser.add_argument('to_currency', help='Specify the currency code to convert to')

    args = parser.parse_args()

    currency_converter = CurrencyConverter()
    currency_converter.convert(args.amount, args.from_currency, args.to_currency)
