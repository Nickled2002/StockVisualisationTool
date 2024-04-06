import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_csv('case1.csv')
data3= pd.read_csv('case3.csv')
data2= pd.read_csv('case2.csv')

'''
#=============================close price-time===============================================
# Plot the adjusted close price

plottable = pd.DataFrame()
plottable['value'] = data['close']
timestamp=pd.to_datetime(data['timestamp'])
plottable = plottable.set_index(timestamp)
plt.plot(plottable,label = data.at[0,'name'])
plt.gcf().autofmt_xdate()
plt.plot(figsize=(20, 17))
#plt.plot(data['timestamp'],data['close'])
# Define the label for the title of the figure
plt.title("Close Price of Apple", fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
# Show the plot
plt.legend()
plt.show()
#=============================volume of stock===============================================
plottable = pd.DataFrame()
plottable['data'] = data['volume']
timestamp=pd.to_datetime(data['timestamp'])
plottable = plottable.set_index(timestamp)
plt.plot(plottable,label = 'AAPL')
plt.gcf().autofmt_xdate()
plt.plot(figsize = (15,7))
plt.title("Volume of Stock traded", fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.legend()
plt.show()
#=============================volume of stock===============================================
plottable = pd.DataFrame()
plottable['data'] = data['open']*data['volume']
timestamp=pd.to_datetime(data['timestamp'])
plottable = plottable.set_index(timestamp)
plt.plot(plottable,label = 'AAPL')
plt.gcf().autofmt_xdate()
plt.plot(figsize = (15,7))
plt.title("Market Cap", fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.legend()
plt.show()
plotdata = pd.concat([data['open'],data2['open']],axis=1)
plotdata.columns = [data.at[0,'name'],data2.at[0,'name']]
pd.plotting.scatter_matrix(plotdata, figsize = (15,7))
plt.show()
plotdata = pd.concat([data['open'],data2['open'],data3['open']],axis=1)
plotdata.columns = [data.at[0,'name'],data2.at[0,'name'],data3.at[0,'name']]
pd.plotting.scatter_matrix(plotdata, figsize = (15,7))
plt.show()
'''
plottable = pd.DataFrame()
plottable2 = pd.DataFrame()
plottable3 = pd.DataFrame()
plottable['returns'] = (data['close']/data['close'].shift(1)) -1
plottable2['returns'] = (data2['close']/data2['close'].shift(1))-1
plottable3['returns'] = (data3['close']/data3['close'].shift(1)) - 1
plottable['returns'].hist(bins = 100, label = data.at[0,'name'], alpha = 0.5, figsize = (15,7))
plottable2['returns'].hist(bins = 100, label = data2.at[0,'name'], alpha = 0.5)
plottable3['returns'].hist(bins = 100, label = data3.at[0,'name'], alpha = 0.5)
plt.title("Volatility", fontsize=16)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.legend()
plt.show()