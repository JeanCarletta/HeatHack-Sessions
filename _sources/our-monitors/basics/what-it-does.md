# What the monitor does

This page describes version 3 monitors but comments on how versions 1 and 2 differ.  

```{admonition} Tip
:class: Tip

Both modes work better if the monitor is left on except when you are accessing it.  If your building's occupants fiddle with the monitor, put a piece of tape over the on-off switch.
```


## In internet mode

Once you have set it up, the monitor will take temperature and relative humidity readings and send them to the internet immediately.  It will do it again after five minutes and then after another five minutes.  This is so you can check the monitor is working using ThingSpeak.  After this, the monitor will take readings every five minutes, but to save battery, it doesn't send them to the web instantly.  During the day (6 am to 6 pm), it saves an hour worth of readings and sends them all at once.  At night, and also during the day if your wifi is very slow, it saves them for 6 hours.  There's a further delay in that our website only checks for new data every four hours.  That means it can be 16 hours before the readings appear with the rest of your data on our website. 

You can re-check whether a monitor is still working at any time by turning it off, waiting 10 seconds, and turning it on again.  The monitor will wait for a minute to see if you want to connect to heathack-s but after that restart using the wifi connection details you entered when you set it up. 

ThingSpeak do not guarantee timely arrival of the data but batch updates usually complete within a minute.  We have noticed rare very long delays, over an hour.  The timestamps will be correct when they do eventually arrive.  

Versions 1 and 2 are similar but all readings are sent to the internet immediately.

## In save mode

The monitor will take temperature and relative humidity readings every five minutes and save them.  It can store around three weeks worth of readings.  Every time you restart the monitor, it will offer to download the data it has saved and start collecting data again.  There is no way to restart the device without downloading the data, but if you don't want the data file, you can delete it. 

You must go through full set up whenever you collect the data.  The monitor is so cheap it relies on your phone or laptop to know what time it is when you start the device and when you pick up the data.  Its own internal clock can run fast or slow so we rely on these timings to correct the times in the data.  We can't do this if anyone turns the monitor off and on without downloading the data.  Don't turn the monitor off until you are ready to download the data. If you need to, you can always carry the monitor around **still running** until you can deal with it.

Although you will be entering information about where you have placed the monitor, our processing doesn't save that yet.  You can you use our diary template for recording monitor movements until we get this sorted.

- [Thermal monitoring location diary template](https://docs.google.com/spreadsheets/d/1Lb59luV7bnODQef9KC9vKmHjVDsIbQYyRfcX4VaVAA4/edit?usp=sharing)



