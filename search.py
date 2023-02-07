#We start by importing the necessary library
#If you are working on google colab 
!pip install pytrends

#else just run
py -m pip install pytrends

#importing the necessary libraries
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trend = TrendReq()

#Getting the result for ChatGPT
trend.build_payload(kw_list=["ChatGPT"])
data = trend.interest_by_region()
data = data.sort_values(by="ChatGPT", ascending=False)
data = data.head(20)
print(data)

#Now visualizing the result
data.reset_index().plot(x="geoName", y="ChatGPT", figsize=(5,12), kind="bar")
plt.style.use("fivethirtyeight")
plt.show()

#Trend result over time
data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['ChatGPT'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data['ChatGPT'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches ChatGPT', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()
