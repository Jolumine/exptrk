from iexfinance.stocks import Stock


def get_information(symbol:str) -> dict: 
    asset = Stock(symbol)
    return {"Name": symbol, "Price": asset.get_price(), "MarketCap": asset.get_market_cap()}


print(get_information("MSFT"))