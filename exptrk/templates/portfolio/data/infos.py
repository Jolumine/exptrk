import finnhub
from datetime import datetime

import json

client = finnhub.Client("cgi8fq9r01qnl59fi4j0cgi8fq9r01qnl59fi4jg")

start = int(datetime(2023, 1, 1).timestamp())
end = int(datetime(2023, 1, 31).timestamp())

res = client.stock_candles('AAPL', 'D', start, end)
print(res)

#Convert to Pandas Dataframe
import pandas as pd

with open("./data.json", "w") as f: 
    parsed = json.loads(pd.DataFrame(res).to_json())
    json.dump(parsed, f, indent=4, sort_keys=False)
    f.close()

