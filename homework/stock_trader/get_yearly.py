"""Task 4.2.

Before you start, copy and paste your code from Task 4.1.
CAUTION: You must implement make_stock_tuples, convert_to_objects functions to grade correctly.
         You CANNOT import any kind of module.
Implementation four methods get_highest_price(), get_lowest_price(), get_average_price(), get_average_volume() in Stock class.

"""

import csv
from typing import Union, List, Tuple

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

    def get_highest_price(self, date: str) -> Union[float, str]:
        """
        Return a highest price between the given date and the previous 260 days of the given date.
        Details are in the document.
        
        Input arguments:
            date (str)
        Return:
            highest price (float)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        if date <= "2019-01-01":
            return "Please check the date."
        
        lst = []
        for price in self.prices:
            d = price.date
            if d <= date:
                lst.append([d, price.price])
        
        lst.sort()
        lst.reverse()
        if len(lst) < 260 or lst[0][0] != date:
            return "Please check the date."
        
        lst = lst[:260]
        max_prc = 0
        for _, prc in lst:
            max_prc = max(max_prc, prc)

        return max_prc

    def get_lowest_price(self, date: str) -> Union[float, str]:
        """
        Return a lowest price between the given date and the previous 260 days of the given date.
        Details are in the document.
        
        Input arguments:
            date (str)
        Return:
            lowest price (float)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        if date <= "2019-01-01":
            return "Please check the date."

        lst = []
        for price in self.prices:
            d = price.date
            if d <= date:
                lst.append([d, price.price])
        
        lst.sort()
        lst.reverse()
        if len(lst) < 260 or lst[0][0] != date:
            return "Please check the date."
        
        lst = lst[:260]
        min_prc = float("inf")
        for _, prc in lst:
            min_prc = min(min_prc, prc)

        return min_prc
        

    def get_average_price(self, date: str) -> Union[float, str]:
        """
        Return an average price between the given date and the previous 260 days of the given date.
        Details are in the document.
        
        Input arguments:
            date (str)
        Return:
            agerage price (float, rounded to two decimal places)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        if date <= "2019-01-01":
            return "Please check the date."
        
        lst = []
        for price in self.prices:
            d = price.date
            if d <= date:
                lst.append([d, price.price])
        
        lst.sort()
        lst.reverse()
        if len(lst) < 260 or lst[0][0] != date:
            return "Please check the date."
        
        lst = lst[:260]
        total_prc = 0
        for _, prc in lst:
            total_prc += prc

        return round(total_prc / 260.0, 2)


    def get_average_volume(self, date: str) -> Union[float, str]:
        """
        Return an average volume between the given date and the previous 260 days of the given date.
        Details are in the document.
        
        Input arguments:
            year (int)
            month (int)
            day (int)
        Return:
            agerage volume (float, rounded to two decimal places)
            or error message (str)
        """
        #################################################
        # YOUR CODE HERE
        #################################################
        if date <= "2019-01-01":
            return "Please check the date."
        
        lst = []
        for price in self.prices:
            d = price.date
            if d <= date:
                lst.append([d, price.volume])
        
        lst.sort()
        lst.reverse()
        if len(lst) < 260 or lst[0][0] != date:
            return "Please check the date."
        
        lst = lst[:260]
        total_vol = 0
        for _, volume in lst:
            total_vol += volume

        return round(total_vol / 260.0, 2)     


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
    # test your implementation
    stock_tuples = make_stock_tuples('data/stock.csv')
    markets = convert_to_objects(stock_tuples)
    for market_obj in markets:
        if market_obj.name == "NASDAQ":
            for stock in market_obj.stocks:
                if stock.symbol == "AAPL":
                    print(stock.get_highest_price("2020-02-03"))
                    print(stock.get_lowest_price("2020-02-03"))
                    print(stock.get_average_price("2020-02-03"))
                    print(stock.get_average_volume("2020-02-03"))
                    print(stock.get_highest_price("2017-02-03"))
                    break
            break
