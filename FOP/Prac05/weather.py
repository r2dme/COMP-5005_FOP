#
# weather.py: Print min and max temps from a file
# (Source:http://www.bom.gov.au/climate/)

import matplotlib.pyplot as plt

fileobj = open('marchweather.csv','r')

minsline = fileobj.readline()
maxsline = fileobj.readline()

fileobj.close()

mins = minsline.split(',')
maxs = maxsline.split(',')

dates = range(1,32)

plt.plot(dates,mins,dates,maxs)
plt.show()


