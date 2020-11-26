"""Task 4.1.

Complete two functions: make_stock_tuples, convert_to_objects
Complete three class implementations: Price, Stock, Market
(DO NOT TOUCH ATTRIBUTES OF EACH CLASS)
CAUTION: You CANNOT import any kind of module.

Use csv library to read and parse CSV format.
https://docs.python.org/3/library/csv.html

"""

import csv
from typing import List, Tuple

def csv_load_example():
    with open('data/stock.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(row)


def make_stock_tuples(data_dir: str) -> List[Tuple[str, str, str, str, float, int]]:
    """

    Read the rows (exclude header) of the CSV and return them via tuple given data_dir.

    Args:
        data_dir (str)

    Returns:
        Tuple[str, str, str, str, float, int]: tuple consists of
        Date: str,
        Market: str,
        Company Name: str,
        Symbol: str,
        Price: float, and
        Volume: int

    """
    #################################################
    # YOUR CODE HERE
    #################################################
    lst = []
    with open(data_dir, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        fst = True
        for row in reader:
            if fst:
                fst = False
                continue
            date, market, name, sym, prc, vol = row
            prc = float(prc)
            vol = int(vol)
            lst.append((date, market, name, sym, prc, vol))
    return lst



class Price:
    """Price class."""

    date: str
    price: float
    volume: int

    def __init__(self, date: str, price: float, volume: int):
        """
        Initialize new Price

        Args:
            date (str): date of price
            price (float): price for the date
            volume (int): volume of trading for the date

        """
        #################################################
        # YOUR CODE HERE
        #################################################
        self.date = date
        self.price = price
        self.volume = volume

    def __repr__(self):
        return "<Price %s>" % self.date


class Stock:
    """Stock class."""

    name: str
    symbol: str
    prices: List[Price]

    def __init__(self, name: str, symbol: str, prices: List[Price]):
        """
        Initialize new Stock

        Args:
            name (str): name of stock
            prices (List[Price]): list of price objects for the stock

        """
        #################################################
        # YOUR CODE HERE
        #################################################
        self.name = name
        self.symbol = symbol
        self.prices = prices

    def __repr__(self):
        return "<Stock %s (%s)>" % (self.name, self.symbol)


class Market:
    """Market class."""

    name: str
    stocks: List[Stock]

    def __init__(self, name: str, stocks: List[Stock]):
        """
        Initialize new Market

        Args:
            name (str): name of market
            stocks (List[Stock]): list of stock objects that belong to the market

        """
        #################################################
        # YOUR CODE HERE
        #################################################
        self.name = name
        self.stocks = stocks

    def __repr__(self):
        return "<Market %s>" % self.name


def convert_to_objects(stock_prices: List[Tuple[str, str, str, str, float, int]]) -> List[Market]:
    """

    Read the CSV file given stock_prices (output of make_stock_tuples function) and return list of 
    parsed Market objects.

    Args:
        stock_prices (Tuple[str, str, str, str, float, int]): output of make_stock_tuples function

    Returns:
        List[Market]: a list of parsed Market objects

    """
    #################################################
    # YOUR CODE HERE
    #################################################
    markets = dict()
    stocks = dict()
    for date, market, name, symbol, price, volume in stock_prices:
        price = Price(date, price, volume)
        if name in stocks:
            stocks[name].append(price)
        else:
            stocks[name] = [price]
        if market in markets:
            markets[market].append((name, symbol))
        else:
            markets[market] = [(name, symbol)]
    
    market_list = []
    for market_name, stock_list in markets.items():
        lst = []
        for name, symbol in stock_list:
            stock = Stock(name, symbol, stocks[name])
            lst.append(stock)
        market = Market(market_name, lst)
        market_list.append(market)
    
    return market_list



if __name__ == "__main__":
    # csv_load_example()
    # test your implementation
    stock_tuples = make_stock_tuples('stock.csv')
    markets = convert_to_objects(stock_tuples)
    print(type(markets))
    for market in markets:
        print(market)
        for stock in market.stocks:
            print(stock)
            for price in stock.prices:
                print(price)
                print(price.price, price.volume)
                break
            break
        break
