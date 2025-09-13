import yfinance as yf
import pandas as pd
import plotly.graph_objects as g 
import matplotlib.pyplot as plt
from datetime import datetime

# 讀取csv檔
#stock_list = pd.read_csv('/stock_id.csv')
#stock_list.columns = ['stock_id', 'name']
historical_data = pd.DataFrame()
#for i in stock_list.index:    
    # 抓取股票資料
ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2025-04-25"

current_date = datetime.now().strftime('%Y-%m-%d')

if end_date > current_date:
    printf(f"Note: End data is in the future. Data will oney available until {current_date}")
    end_date = current_date
data = yf.download(ticker, start=start_date, end=end_date)

print(f"\n{ticker} Stock Data:")
print(data.head())

print("\nSummary Statistics:")
print(data['Close'].describe)

#df = data.history(period="max")
# 增加股票代號
#df['stock_id'] = stock_list.loc[i, 'stock_id']
# 合併
#historical_data = pd.concat([historical_data, df])
#time.sleep(0.8)
data.to_csv('data.csv', index=True)