from polygon import RESTClient
from polygon.rest.models import (Agg,)
import csv
import datetime
import io
import matplotlib.pyplot as plt
import pandas as pd

# Make call to polygon
client = RESTClient('APIKEY')

def addtocsv(aggs,num,name):
    # Add data to csv
    # headers
    headers = [
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "vwap",
        "transactions",
        "year",
        "name",
        #"otc",
    ]
    # creating the csv string
    csv_string = io.StringIO()

    #writer = csv.DictWriter(csv_string, fieldnames=headers)

    with open('case'+str(num)+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        #writer = csv.DictWriter(csv_string, fieldnames=headers)
        writer.writerow(headers)
        #writer.writeheader()
        # writing data
        for agg in aggs:
            # verify this is an agg
            if isinstance(agg, Agg):
                # verify this is an int
                if isinstance(agg.timestamp, int):
                    writer.writerow([
                                        datetime.datetime.fromtimestamp(agg.timestamp / 1000).strftime('%Y-%m-%d'),
                                        agg.open,
                                        agg.high,
                                        agg.low,
                                        agg.close,
                                        agg.volume,
                                        agg.vwap,
                                        agg.transactions,
                                        datetime.datetime.fromtimestamp(agg.timestamp / 1000).year,
                                        name
                        ]
                    )
def retrieve():
    aggs = []
    while not aggs:
        x = input('Enter a stock name you want to analyse:')
        # Request data
        for a in client.list_aggs(
            x,
            1,
            "day",
            "2022-04-05",
            datetime.datetime.today().strftime('%Y-%m-%d'),
            limit=50000,
        ):
            aggs.append(a)
        if not aggs:
            print('Stock ', x, ' doesnt exist try again')
    return aggs,x


while True:
    ammount=input('How many stocks would you like to compare (1-3):')
    try:
        ammount = int(ammount)
    except:
        print('Please use numeric digits.')
        continue
    if ammount < 1 or ammount > 3:
        print('Please enter a number within the scope.')
        continue
    break
for num in range (0,ammount):
    aggs = []
    aggs,name=retrieve()

    while True:
        decision=input('Would you like to [1]Save the data locally or [2]Save it to the database :')
        try:
            decision = int(decision)
        except:
            print('Please choose either numerical option [1]Save the data locally or option [2]Save it to the database')
            continue
        if decision < 1 or decision > 2:
            print('Please enter a number within the scope.')
            continue
        break
    if decision ==1:
        num +=1
        addtocsv(aggs,num,name)
        num -=1
    elif decision ==2:
        print("add to database")
        #TODO ADD to db
data = pd.read_csv('case1.csv')
if ammount > 1:
    data2 = pd.read_csv('case2.csv')
if ammount > 2:
    data3 = pd.read_csv('case3.csv')

#=============================close price-time===============================================
# Plot the adjusted close price

plottable = pd.DataFrame()
plottable['value'] = data['close']
timestamp=pd.to_datetime(data['timestamp'])
plottable = plottable.set_index(timestamp)
plt.plot(plottable,label = data.at[0,'name'])
plt.plot(figsize = (15,7))
if ammount > 1:
    plottable2 = pd.DataFrame()
    plottable2['value'] = data2['close']
    timestamp2=pd.to_datetime(data2['timestamp'])
    plottable2 = plottable2.set_index(timestamp2)
    plt.plot(plottable2,label = data2.at[0,'name'])
if ammount > 2:
    plottable3 = pd.DataFrame()
    plottable3['value'] = data3['close']
    timestamp3=pd.to_datetime(data3['timestamp'])
    plottable3 = plottable3.set_index(timestamp3)
    plt.plot(plottable3,label = data3.at[0,'name'])
plt.gcf().autofmt_xdate()
#plt.plot(data['timestamp'],data['close'])
# Define the label for the title of the figure
plt.title("Close Price", fontsize=16)
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
plottable['value'] = data['volume']
timestamp=pd.to_datetime(data['timestamp'])
plottable = plottable.set_index(timestamp)
plt.plot(plottable,label = data.at[0,'name'])
plt.plot(figsize = (15,7))
if ammount > 1:
    plottable2 = pd.DataFrame()
    plottable2['value'] = data2['volume']
    timestamp2=pd.to_datetime(data2['timestamp'])
    plottable2 = plottable2.set_index(timestamp2)
    plt.plot(plottable2,label = data2.at[0,'name'])
if ammount > 2:
    plottable3 = pd.DataFrame()
    plottable3['value'] = data3['volume']
    timestamp3=pd.to_datetime(data3['timestamp'])
    plottable3 = plottable3.set_index(timestamp3)
    plt.plot(plottable3,label = data3.at[0,'name'])
plt.gcf().autofmt_xdate()
plt.title("Volume of Stock traded", fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.legend()
plt.show()
#=============================Market Cap stock===============================================
plottable = pd.DataFrame()
plottable['data'] = data['open']*data['volume']
timestamp=pd.to_datetime(data['timestamp'])
plottable = plottable.set_index(timestamp)
plt.plot(plottable,label= data.at[0,'name'])
plt.plot(figsize = (15,7))
if ammount > 1:
    plottable2 = pd.DataFrame()
    plottable2['value'] = data2['open']*data2['volume']
    timestamp2=pd.to_datetime(data2['timestamp'])
    plottable2 = plottable2.set_index(timestamp2)
    plt.plot(plottable2,label = data2.at[0,'name'])
if ammount > 2:
    plottable3 = pd.DataFrame()
    plottable3['value'] = data3['open']*data3['volume']
    timestamp3=pd.to_datetime(data3['timestamp'])
    plottable3 = plottable3.set_index(timestamp3)
    plt.plot(plottable3,label = data3.at[0,'name'])
plt.gcf().autofmt_xdate()
plt.title("Market Cap", fontsize=16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.legend()
plt.show()
#=============================Scattered plot===============================================


if ammount == 2:
    plotdata = pd.concat([data['open'],data2['open']],axis=1)
    plotdata.columns = [data.at[0,'name'],data2.at[0,'name']]
    pd.plotting.scatter_matrix(plotdata, figsize = (15,7))
    plt.show()
if ammount == 3:
    plotdata = pd.concat([data['open'],data2['open'],data3['open']],axis=1)
    plotdata.columns = [data.at[0,'name'],data2.at[0,'name'],data3.at[0,'name']]
    pd.plotting.scatter_matrix(plotdata, figsize = (15,7))
    plt.show()

#=============================Volatility===============================================
plottable = pd.DataFrame()
plottable['returns'] = (data['close']/data['close'].shift(1)) -1
plottable['returns'].hist(bins = 100, label = data.at[0,'name'], alpha = 0.5, figsize = (15,7))
plt.title("Volatility", fontsize=16)
if ammount > 1:
    plottable2 = pd.DataFrame()
    plottable2['returns'] = (data2['close']/data2['close'].shift(1))-1
    plottable2['returns'].hist(bins = 100, label = data2.at[0,'name'], alpha = 0.5)
if ammount > 2:
    plottable3 = pd.DataFrame()
    plottable3['returns'] = (data3['close']/data3['close'].shift(1)) - 1
    plottable3['returns'].hist(bins = 100, label = data3.at[0,'name'], alpha = 0.5)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.legend()
plt.show()
