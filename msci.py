import unirest

response = unirest.get("https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary?region=US&symbol=AMRN",
  headers={
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "092f849010mshe64c016d6009f6bp13d678jsn4d31ff90363c"
  }
)

import pandas_datareader as pdr
import pandas as pd
import numpy as np
from datetime import datetime
import pandas_datareader as pdr
from pandas_datareader import data
import matplotlib.pyplot as plt


# PART A OF THE PORJECT


from datetime import datetime

aapl_daily = pdr.get_data_yahoo('AAPL',start=datetime(2018, 7, 1), end=datetime(2019, 7, 1))

aapl_weekly = pdr.get_data_yahoo('AAPL',start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='w')

aapl_monthly = pdr.get_data_yahoo('AAPL',start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')



start_date = '2010-01-01'
end_date = '2016-12-31'

#panel_data = data.DataReader('INPX', 'yahoo', start_date, end_date)
'''
def PARTa():
    stock1 = raw_input("what are the two stocks that you want to evaluate? Enter the first one.")
    stock2 = raw_input("Enter the second one.")
    
    stock1_monthly = pdr.get_data_yahoo(stock1, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock2_monthly = pdr.get_data_yahoo(stock2, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    
    del stock1_monthly['Adj Close'] # we do not need this data
    del stock1_monthly['Volume']
    del stock2_monthly['Adj Close'] # we do not need this data
    del stock2_monthly['Volume']
    
    stock1_monthly['Return'] = (stock1_monthly['Close'] - stock1_monthly['Open']) / stock1_monthly['Open']
    stock2_monthly['Return'] = (stock2_monthly['Close'] - stock2_monthly['Open']) / stock2_monthly['Open']
    
    data1 = np.array(stock1_monthly['Return'], dtype = np.float)
    data2 = np.array(stock2_monthly['Return'], dtype = np.float)
    
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)

    var1 = np.var(data1) 
    var2 = np.var(data2)
    
    std1 = np.std(var1) 
    std2 = np.std(var2)
    
    covar = np.cov(data1, data2)[0][1]

    stock1prop = (var2 - covar)/(var1 + var2 - 2*covar)
    stock2prop = 1 - stock1prop
   
    iter = np.arange(data1.size)
    return_port = np.zeros(data1.size)
    for i in iter:
        return_port[i] = data1[i]*stock1prop + data2[i]*stock2prop
    
    std_port = np.std(return_port)
    eReturn = stock1prop*mean1 + stock2prop*mean2

    print("MVP proportion ", stock1, ": ", round(stock1prop*100,2), "%")
    print("MVP proportion ", stock2, ": ", round(stock2prop*100,2), "%")
    print("MVP standard deviation: ", round(std_port*100,2), "%")
    print("MVP expected portfolio return: ", round(eReturn*100,2), "%")


# PART B OF THE PROJECT

def PARTb():
    stock1 = raw_input("what are the two stocks that you want to evaluate? Enter the first one.")
    stock2 = raw_input("Enter the second one.")
    rf = raw_input("what is your risk-free rate? if you do not know, just enter 0.02. DO NOT enter in percentages!!!")
    
    stock1_monthly = pdr.get_data_yahoo(stock1, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock2_monthly = pdr.get_data_yahoo(stock2, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    
    del stock1_monthly['Adj Close'] # we do not need this data
    del stock1_monthly['Volume']
    del stock2_monthly['Adj Close'] # we do not need this data
    del stock2_monthly['Volume']
    
    stock1_monthly['Return'] = (stock1_monthly['Close'] - stock1_monthly['Open']) / stock1_monthly['Open']
    stock2_monthly['Return'] = (stock2_monthly['Close'] - stock2_monthly['Open']) / stock2_monthly['Open']
    
    data1 = np.array(stock1_monthly['Return'], dtype = np.float)
    data2 = np.array(stock2_monthly['Return'], dtype = np.float)
    
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)

    var1 = np.var(data1) 
    var2 = np.var(data2)
    
    std1 = np.std(var1) 
    std2 = np.std(var2)
    
    stock1prop = 
    stock2prop = 1 - stock1prop
    
    eReturn_port1 = 
    stdev_port1 =
    stdev_excess = 
    sharpe = (eReturn_port1 - rf)/stdev_excess 

    eReturn_port2 = rf*0.5 + eReturn_port1*0.5
    stdev_port2 = 

    eReturn_port3 = rf*(-0.5) + eReturn_port1*1.5
    stdev_port3 = 

    print("Case 1")
    print("Given-Proportion invested in risk-free asset: 0%")
    print("Given-Proportion invested in market portfolio: 100%")
    print("Maximum Sharpe ratio", round(sharpe_max, 4))
    print("Market portfolio proportion ", stock1, round(stock1prop*100, 2), "%")
    print("Market portfolio proportion ", stock2, round(stock2prop*100, 2), "%")
    print("Market expected return ", round(eReturn_port1*100, 2), "%")
    print("Market standard deviation ", round(stdev_port1*100, 2), "%")
    print()

    print("Case 2")
    print("Given-Proportion invested in risk-free asset: 50%")
    print("Given-Proportion invested in market portfolio: 50%")
    print("Portfolio expected return ", round(eReturn_port2*100, 2), "%")
    print("Portfolio standard deviation ", round(stdev_port2*100, 2), "%")
    print()
    
    print("Case 3")
    print("Given-Proportion invested in risk-free asset: -50%")
    print("Given-Proportion invested in market portfolio: 150%")
    print("Portfolio expected return ", round(eReturn_port3*100, 2), "%")
    print("Portfolio standard deviation ", round(stdev_port3*100, 2), "%")
    print()

'''
def PARTc():
    # bonus part
    number = 7.0
    stock1 = 'DVCR'
    stock2 = 'TDOC'
    stock3 = 'UHS'
    stock4 = 'SBUX' # high returns
    stock5 = 'CSU'
    stock6 = 'EXPI'
    stock7 = 'ORPEF'

    stock1_monthly = pdr.get_data_yahoo(stock1, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock2_monthly = pdr.get_data_yahoo(stock2, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock3_monthly = pdr.get_data_yahoo(stock3, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock4_monthly = pdr.get_data_yahoo(stock4, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock5_monthly = pdr.get_data_yahoo(stock5, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock6_monthly = pdr.get_data_yahoo(stock6, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock7_monthly = pdr.get_data_yahoo(stock7, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
   

    stock1_monthly['Return'] = (stock1_monthly['Close'] - stock1_monthly['Open']) / stock1_monthly['Open']
    stock2_monthly['Return'] = (stock2_monthly['Close'] - stock2_monthly['Open']) / stock2_monthly['Open']
    stock3_monthly['Return'] = (stock3_monthly['Close'] - stock3_monthly['Open']) / stock3_monthly['Open']
    stock4_monthly['Return'] = (stock4_monthly['Close'] - stock4_monthly['Open']) / stock4_monthly['Open']
    stock5_monthly['Return'] = (stock5_monthly['Close'] - stock5_monthly['Open']) / stock5_monthly['Open']
    stock6_monthly['Return'] = (stock6_monthly['Close'] - stock6_monthly['Open']) / stock6_monthly['Open']
    stock7_monthly['Return'] = (stock7_monthly['Close'] - stock7_monthly['Open']) / stock7_monthly['Open']

    data1 = np.array(stock1_monthly['Return'], dtype = np.float)
    data2 = np.array(stock2_monthly['Return'], dtype = np.float)
    data3 = np.array(stock3_monthly['Return'], dtype = np.float)
    data4 = np.array(stock4_monthly['Return'], dtype = np.float)
    data5 = np.array(stock5_monthly['Return'], dtype = np.float)
    data6 = np.array(stock6_monthly['Return'], dtype = np.float)
    data7 = np.array(stock7_monthly['Return'], dtype = np.float)
    
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    mean3 = np.mean(data3)
    mean4 = np.mean(data4)
    mean5 = np.mean(data5)
    mean6 = np.mean(data6)
    mean7 = np.mean(data7)

    print("maximum return is from", max(mean1, mean2, mean3, mean4, mean5, mean6, mean7))
    print(mean1)
    print(mean2)
    print(mean3)
    print(mean4)
    print(mean5)
    print(mean6)
    print(mean7)

    stock1prop = 1.0/number 
    stock2prop = 1.0/number
    stock3prop = 1.0/number
    stock4prop = 1.0/number
    stock5prop = 1.0/number
    stock6prop = 1.0/number
    stock7prop = 1.0/number
    
    eReturn_port = stock1prop*mean1 + stock2prop*mean2 + stock3prop*mean3 + stock4prop*mean4 + stock5prop*mean5 + stock6prop*mean6 + stock7prop*mean7
    
    iter = np.arange(data1.size)
    return_port = np.zeros(data1.size)
    for i in iter:
        return_port[i] = data1[i]*stock1prop + data2[i]*stock2prop + data3[i]*stock3prop + data4[i]*stock4prop + data5[i]*stock5prop + data6[i]*stock6prop + data7[i]*stock7prop
    stdev_port = np.std(return_port)

    print("The stocks that we chose are:")
    print(stock1, stock2, stock3, stock4, stock5, stock6, stock7)
    print("Expected return is:", round(eReturn_port*100, 2), "%")
    print("Expected standard deviation is:", round(stdev_port*100, 2), "%")

if __name__ == "__main__":
    #PARTa()
    #PARTb()
    PARTc() # bonus part
