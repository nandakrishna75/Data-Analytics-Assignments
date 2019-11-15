        library("fpp2")
# MOVING AVERAGES
# using the electicity sales of south australia as the dataset
autoplot(elecsales) + xlab("Year") + ylab("GWh") + ggtitle("Annual electricity sales: South Australia")
# plotting and using 2 Moving Average as the prediction model
ma(elecsales, 2)
autoplot(elecsales, series="Data") + autolayer(ma(elecsales,2), series="2-MA") + xlab("Year") + ylab("GWh") + ggtitle("Annual electricity sales: South Australia") + 
    scale_colour_manual(values=c("Data"="grey50","2-MA"="red"), breaks=c("Data","2-MA"))
# plotting and using 3 Moving Average as the prediction model
ma(elecsales, 3)
autoplot(elecsales, series="Data") + autolayer(ma(elecsales,3), series="3-MA") + xlab("Year") + ylab("GWh") + ggtitle("Annual electricity sales: South Australia") + 
    scale_colour_manual(values=c("Data"="grey50","3-MA"="red"), breaks=c("Data","3-MA"))
# plotting and using 5 Moving Average as the prediction model
ma(elecsales, 5)
autoplot(elecsales, series="Data") + autolayer(ma(elecsales,5), series="5-MA") + xlab("Year") + ylab("GWh") + ggtitle("Annual electricity sales: South Australia") + 
    scale_colour_manual(values=c("Data"="grey50","5-MA"="red"), breaks=c("Data","5-MA"))
# plotting and using 10 Moving Average as the prediction model
ma(elecsales, 10)
autoplot(elecsales, series="Data") + autolayer(ma(elecsales,10), series="10-MA") + xlab("Year") + ylab("GWh") + ggtitle("Annual electricity sales: South Australia") + 
    scale_colour_manual(values=c("Data"="grey50","10-MA"="red"), breaks=c("Data","10-MA"))
#using the 12 moving average prediction model on electric equipment orders dataset
autoplot(elecequip, series="Data") + autolayer(ma(elecequip, 12), series="12-MA") + xlab("Year") + ylab("New orders index") + 
    ggtitle("Electrical equipment manufacturing (Euro area)") + scale_colour_manual(values=c("Data"="grey","12-MA"="red"), breaks=c("Data","12-MA"))

# SIMPLE EXPONENTIAL SMOOTHING
# using oil spill in saudi arabia from year 1996 as dataset
oildata <- window(oil, start=1996)
autoplot(oildata) + ylab("Oil (millions of tonnes)") + xlab("Year")
# using simple exponential smoothing model (ses)
fc <- ses(oildata, h=5)
round(accuracy(fc),2) #obtaining all accuracy and metric scores rounded to 2 decimal places
# plotting SES model
autoplot(fc) + autolayer(fitted(fc), series="Fitted") + ylab("Oil (millions of tonnes)") + xlab("Year")