#Stock Evaluation

Project by: Rosie (Mahshid) Bahrani, Angelo Gabriel Lao, Sailesh Nankani, Ruofan Xing

This is the instruction for running the project code.

Make sure to run the code with Python2. DO NOT run the code with Python 3 as this can cause unexpected results. 
'''python2 msci.py'''

The following libraries were used for data analysis. Please make sure that you have installed them all before running the program.
unirest -- version NOT FOUND -- discussed with Fuat in class & he said it's alright if we don't find the version for this.
pandas_datareader -- version u'0.7.0'
pandas -- version 0.24.2
numpy -- vesrion 1.16.4
datetime -- version unavailable as datetime is a python function, not an external library
pandas_datareader.data -- version u'0.7.0'
matplotlib.pyplot -- version '2.2.4'
scipy -- version 1.2.2

In case you have any trouble with running the program, please contact rosie.bahrani@uwaterloo.ca for an in-person demo.

NOTE: Sometimes, you might get the following error or something similar to it:

File "msci.py", line 133, in PARTb
    stock2_monthly = pdr.get_data_yahoo(stock2, start=datetime(2018, 7, 1), end=datetime(2019, 7, 1),interval='m')
  File "/usr/local/lib/python2.7/site-packages/pandas_datareader/data.py", line 70, in get_data_yahoo
    return YahooDailyReader(*args, **kwargs).read()
  File "/usr/local/lib/python2.7/site-packages/pandas_datareader/base.py", line 210, in read
    params=self._get_params(self.symbols))
  File "/usr/local/lib/python2.7/site-packages/pandas_datareader/yahoo/daily.py", line 142, in _read_one_data
    to_datetime(prices['Date'], unit='s').dt.date)
  File "/usr/local/lib/python2.7/site-packages/pandas/core/frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/usr/local/lib/python2.7/site-packages/pandas/core/indexes/base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Date'

DO NOT PANIC! This error is because your internet connection was poor at the moment you made the call to the YahooFinance API. Just run the command line again! :) 
