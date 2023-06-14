from exptrk.utils.read_index import read_index

import json


def get_assets() -> list:
    assets = []
    with open(read_index("portfolio"), "r") as f:
        parsed = json.load(f)
        f.close()

    for asset in parsed["assets"]:
        assets.append(
            (
                asset,
                parsed["assets"][asset]["Shares"],
                parsed["assets"][asset]["Buy Price"],
            )
        )

    return assets


def get_popular() -> list:
    popular = []
    with open(read_index("popular", True), "r") as f:
        parsed = json.load(f)
        f.close()

    for asset in parsed:
        popular.append((asset, parsed[asset]["Icon"], parsed[asset]["Symbol"]))

    return popular


def get_cryptos() -> list: 
    cryptos = []

    with open(read_index("cryptos", True), "r") as f: 
        parsed = json.load(f)
        f.close()

    for coin in parsed: 
        cryptos.append((coin, parsed[coin]["Icon"], parsed[coin]["Symbol"]))

    return cryptos

def get_markets() -> list: 
    markets = []

    with open(read_index("markets", True), "r") as f: 
        parsed = json.load(f)
        f.close()

    for market in parsed: 
        markets.append((market, parsed[market]["Icon"]))

    return markets