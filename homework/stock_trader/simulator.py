"""Task 4.4.

Before you start, copy and paste your code from Task 4.3.
CAUTION: You must implement make_stock_tuples, convert_to_objects functions to grade correctly.
         You CANNOT import any kind of module.
Complete the class Trader which has five methods.

"""

import csv
from typing import Optional, Union, List, Tuple

def make_stock_tuples(data_dir: str) -> List[Tuple[str, str, str, str, float, int]]:
    """
    copy your implementation from Task 4.1
    """
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

    def get_moving_average(self, date: str) -> Union[float, str]:
        """
        Return a moving average price between the given date and the previous 20 days of the given date.
        Details are in the document.
        
        Input arguments:
            date (str)
        Return:
            moving agerage price (float, rounded to two decimal places) 
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        lst = []
        for price in self.prices:
            d = price.date
            if d <= date:
                lst.append([d, price.price])
        
        lst.sort()
        lst.reverse()
        if len(lst) < 20 or lst[0][0] != date:
            return "Please check the date."
        
        lst = lst[:20]
        total_prc = 0
        for _, prc in lst:
            total_prc += prc

        return round(total_prc / 20.0, 2)

    def get_bollinger_bands(self, date: str) -> Union[Tuple[float, float], str]:
        """
        Return a tuple of the upper band and lower band of bollinger band between the given date and
        the previous 20 days of the given date.
        Details are in the document.
        
        Input arguments:
            date(str)
        Return:
            bollinger band (Tuple[float, float], rounded to two decimal places)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        lst = []
        for price in self.prices:
            d = price.date
            if d <= date:
                lst.append([d, price.price])
        
        lst.sort()
        lst.reverse()
        if len(lst) < 20 or lst[0][0] != date:
            return "Please check the date."
        
        lst = lst[:20]

        total_prc = 0
        for _, prc in lst:
            total_prc += prc
        avg = round(total_prc / 20, 2)

        std = 0
        for _, prc in lst:
            std += (prc - avg)**2
        std /= 19
        std = std**.5

        L = round(avg - 2*std, 2)
        U = round(avg + 2*std, 2)
        return (U, L)



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


class Trader:
    """Trader class."""

    name: str
    balance: float
    holdings: Tuple[str, str, int, float]

    def __init__(self, name: str, balance: float):
        """
        Initialize new Trader

        Args:
            name (str): name of market
            balance (float): current cash the trader has
            holdings (Tuple[str, str, int, float]): tuple consists of
                Date: str,
                Ticker: str,
                the amount of the stock: int, and
                the price when you bought: float

        """
        self.holdings = tuple()
        #################################################
        # YOUR CODE HERE
        #################################################
        self.name = name
        self.balance = balance

    def buy(self, ticker: str, price: float, date: str) -> None:
        """
        Update holdings and balance fields after buying.
        Details are in the document.
        
        Input arguments:
            ticker (str)
            price (float)
            date (str)
        Return:
            None
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        num_stock = self.balance // price
        self.holdings = (date, ticker, num_stock, price)
        self.balance = round(self.balance - price * num_stock, 2)

    def sell(self, ticker: str, price: float) -> None:
        """
        Update holdings and balance fields after selling.
        Details are in the document.
        
        Input arguments:
            ticker (str)
            price (float)
        Return:
            None
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        amount = 0
        if self.holdings[1] == ticker:
            amount = self.holdings[2] * price
            self.holdings = tuple()
        self.balance += amount
        self.balance = round(self.balance, 2)

    def check(self) -> Tuple[float, Tuple[str, str, int, float]]:
        """
        Return balance holdings fields.
        Details are in the document.
        
        Input arguments:
            None
        Return:
            Tuple[float, Tuple[str, str, int, float]]: tuple consists of
                balance (str), and
                holdings (Tuple[str, str, int, float])
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        return (self.balance, self.holdings)

    def simulate(self, markets: List[Market], ticker: str, date: str) -> Optional[str]:
        """
        Trading simulator with given date and ticker.
        Trading algorithm is as follows:
            1. You have to buy the stock when the price is lower than the lower band of the bollinger bands.
            2. You have to sell the stock when the price is higher than the upper band of the bollinger bands.
        Details are in the document.
        
        Input arguments:
            a list of parsed Market objects (List[Market])
            ticker (str)
            date (str)
        Return:
            None
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        market, stock = ticker.split(":")
        for market_obj in markets:
            if market_obj.name == market:
                for stock_obj in market_obj.stocks:
                    if stock_obj.symbol == stock:
                        market = market_obj
                        stock = stock_obj
                        break
                break

        bounds = stock.get_bollinger_bands(date)
        if isinstance(bounds, str):
            return "Please check the date."
        dates = []
        for price in stock.prices:
            if price.date >= date:
                dates.append((price.date, price.price))
        dates.sort()

        buying = True
        for date, price in dates:
            U, L = stock.get_bollinger_bands(date)
            if buying and price < L:
                self.buy(ticker, price, date)
                buying = False
            elif not buying and price > U:
                self.sell(ticker, price)
                buying = True

    def __repr__(self):
        return "<Trader %s>" % self.name


if __name__ == "__main__":
    # test your implementation
    stock_tuples = make_stock_tuples('data/stock.csv')
    markets = convert_to_objects(stock_tuples)
    t = Trader("Warren Buffet", 1000.)
    t.simulate(markets, "NASDAQ:AAPL", "2019-02-01")
    print(t.check())
    t = Trader("Warren Buffet", 1000.)
    t.simulate(markets, "NYSE:JNJ", "2019-02-01")
    print(t.check())