import yfinance as yf 

#Interval required 5 minutes
data = yf.download(tickers='AAPL', period='5d', interval='30m')
#Print data
print(data)