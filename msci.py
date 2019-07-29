from scipy.optimize import minimize
import unirest
import math


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

#aapl_daily = pdr.get_data_yahoo('AAPL',start=datetime(2018, 7, 1), end=datetime(2019, 7, 1))

#aapl_weekly = pdr.get_data_yahoo('AAPL',start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='w')

#aapl_monthly = pdr.get_data_yahoo('AAPL',start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')


def monthly_return(stock):
    lis = []
    i = 1  
    while i < ((stock['Close']).size):
        lis.append(stock['Close'][i]/stock['Close'][i-1] - 1)
        i+=1
    return lis

def calc_SR(w,mu,Sigma,rf):
    #this one is used for Q1
    return_p = np.matmul(w,mu.T)
    var_p= np.matmul(np.matmul(w,Sigma),w.T)
    sd_p = np.sqrt(var_p)
    return((return_p - rf)/sd_p)

start_date = '2010-01-01'
end_date = '2016-12-31'

rf = 0.02

def PARTa():
    stock1 = raw_input("what are the two stocks that you want to evaluate? Enter the first one.")
    stock2 = raw_input("Enter the second one.")
    
    stock1_monthly = pdr.get_data_yahoo(stock1, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock2_monthly = pdr.get_data_yahoo(stock2, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    
    return1 = monthly_return(stock1_monthly)
    return2 = monthly_return(stock2_monthly)
    
    data1 = np.array(return1, dtype = np.float)
    data2 = np.array(return2, dtype = np.float)
    
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    annual_return1 = (1+mean1)**12 - 1
    annual_return2 = (1+mean2)**12 - 1

    var1 = np.var(data1) 
    var2 = np.var(data2)
    var1annual = var1*12
    var2annual = var2*12
    
    std1 = np.std(var1) 
    std2 = np.std(var2)
    
    covar = np.cov(data1, data2)[0][1]
    covar_annual = covar*12

    stock1prop = (var2 - covar)/(var1 + var2 - 2*covar)
    stock2prop = 1 - stock1prop
   
    iter = np.arange(data1.size)
    return_port = np.zeros(data1.size)
    for i in iter:
        return_port[i] = data1[i]*stock1prop + data2[i]*stock2prop
    
    var_port = np.var(return_port)
    annual_var = var_port*12
    annual_std = (annual_var)**(1.0/2.0)
    eReturn = stock1prop*mean1 + stock2prop*mean2
    annual_return = (1+eReturn)**12 - 1

    print "MVP proportion " + stock1 + ": " + str(round(stock1prop*100,2)) + "%"
    print "MVP proportion " + stock2 + ": " + str(round(stock2prop*100,2)) + "%"
    print "MVP standard deviation: " + str(round(annual_std*100,2)) + "%"
    print "MVP expected portfolio return: " + str(round(annual_return*100,2)) + "%"

    # PLOTTING THE DATA
    weights_1 = np.array(list(range(0,11)))/10.0
    weights_2 = 1 - weights_1 
    weights   = np.array([weights_1,weights_2]).T
    returns = np.array([annual_return1, annual_return2])
    covariance = np.array([[var1annual,covar_annual],[covar_annual,var2annual]])
    port_returns = [w[0] * returns[0] + w[1] * returns[1] for w in weights]
    port_vars = [w[0]**2*covariance[0,0] + w[1]**2*covariance[1,1] + 2*w[0]*w[1]*covariance[0,1] for w in weights]
    port_sds = [np.sqrt(v) for v in port_vars]
    port_SRs = [calc_SR(w,returns,covariance,rf) for w in weights]
    df = pd.DataFrame([port_returns,port_sds, port_SRs]).transpose()
    df.columns=['Returns', 'Volatility', 'Sharpe Ratio']
    plt.style.use('seaborn-dark')
    df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio', cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    plt.xlabel('Volatility (Std. Deviation)')
    plt.ylabel('Expected Returns')
    plt.title('Efficient Frontier')
    plt.show()




# PART B OF THE PROJECT

def PARTb():
    stock1 = raw_input("what are the two stocks that you want to evaluate? Enter the first one.")
    stock2 = raw_input("Enter the second one.")

    stock1_monthly = pdr.get_data_yahoo(stock1, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    stock2_monthly = pdr.get_data_yahoo(stock2, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
    
    return1 = monthly_return(stock1_monthly)
    return2 = monthly_return(stock2_monthly)
    
    data1 = np.array(return1, dtype = np.float)
    data2 = np.array(return2, dtype = np.float)
    
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    annual_return1 = (1+mean1)**12 - 1
    annual_return2 = (1+mean2)**12 - 1

    var1 = np.var(data1) 
    var2 = np.var(data2)
    var1annual = var1*12
    var2annual = var2*12

    covar = np.cov(data1, data2)[0][1]
    covariance = covar*12

    std1 = np.std(var1) 
    std2 = np.std(var2)
    
    b = (0.0, 1.0) # this is the constraint for the stockprop values
    bnds = (b)

    def sharpe_ratio(stock1prop_guess):
        #this one is used for Q2
        #note: this function returns the negative of the sharpe ratio, so when we minimize this, we are actually maximizing the sharpe ratio itself.
        stock2prop_guess = 1 - stock1prop_guess
        r_port = stock1prop_guess*annual_return1 + stock2prop_guess*annual_return2
        rf = 0.02
        var_port = stock1prop_guess**2 * var1annual + stock2prop_guess**2 * var2annual + 2*stock1prop_guess*stock2prop_guess*covariance
        stdev_port = math.sqrt(var_port)
        res = (r_port - rf)/stdev_port
        return -1*res #just to minimize this value


    if std1 >= std2:
        stock1prop_guess = 0.99
    if std1 < std2:
        stock1prop_guess = 0.01
    res = minimize(sharpe_ratio, stock1prop_guess, bounds=((0.0, 1.0),))
    stock1prop = res.x[0]
    stock2prop = 1 - stock1prop
    
    eReturn_port1 = stock1prop*annual_return1 + stock2prop*annual_return2
    var_port1 = stock1prop**2 * var1annual + stock2prop**2 * var2annual + 2*stock1prop*stock2prop*covariance
    stdev_port1 = (var_port1)**(0.5)
    sharpe_max = (eReturn_port1 - rf)/stdev_port1 

    eReturn_port2 = rf*0.5 + eReturn_port1*0.5
    var_port2 = 0.5**2 * var_port1 
    stdev_port2 = math.sqrt(var_port2)

    eReturn_port3 = rf*(-0.5) + eReturn_port1*1.5
    var_port3 = 1.5**2 * var_port1
    stdev_port3 = math.sqrt(var_port3)

    print "Case 1"
    print "Given-Proportion invested in risk-free asset: 0%"
    print "Given-Proportion invested in market portfolio: 100%"
    print ""
    print "Maximum Sharpe ratio: " + str(round(sharpe_max, 4))
    print "Market portfolio proportion: " + stock1 + " " + str(round(stock1prop*100, 2)) + "%"
    print "Market portfolio proportion: " + stock2 + " " + str(round(stock2prop*100, 2)) + "%"
    print "Market expected return: " + str(round(eReturn_port1*100, 2)) + "%"
    print "Market standard deviation: "+ str(round(stdev_port1*100, 2)) + "%"
    print ""

    print "Case 2"
    print "Given-Proportion invested in risk-free asset: 50%"
    print "Given-Proportion invested in market portfolio: 50%"
    print ""
    print "Portfolio expected return: " + str(round(eReturn_port2*100, 2)) + "%"
    print "Portfolio standard deviation: " + str(round(stdev_port2*100, 2)) + "%"
    print ""
    
    print "Case 3"
    print "Given-Proportion invested in risk-free asset: -50%"
    print "Given-Proportion invested in market portfolio: 150%"
    print "Portfolio expected return: " + str(round(eReturn_port3*100, 2)) + "%"
    print "Portfolio standard deviation: " + str(round(stdev_port3*100, 2)) + "%"
    print ""

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
   

    stock1_monthly['Return'] = monthly_return(stock1_monthly)
    stock2_monthly['Return'] = monthly_return(stock2_monthly)
    stock3_monthly['Return'] = monthly_return(stock3_monthly)
    stock4_monthly['Return'] = monthly_return(stock4_monthly)
    stock5_monthly['Return'] = monthly_return(stock5_monthly)
    stock6_monthly['Return'] = monthly_return(stock6_monthly)
    stock7_monthly['Return'] = monthly_return(stock7_monthly)

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
'''
if __name__ == "__main__":
    PARTa()
    PARTb()
    #PARTc()
