# Converting an internet-connected unit to standalone

If you discover you need to monitor location where there isn't a good wifi signal, you can ignore the hub and switch your sensor unit to behave as a standalone device.

The standalone sensor for venues without wifi  is described in the same Tech Guide, and if you ignore your hub - which has the USB port - you can convert your sensor to work as it describes.

- [Standalone monitor instructions](https://jeancarletta.github.io/HeatHack-Tech-Guide/no-wifi-version.html)

To convert it, you turn on the *sensor unit* (with the white checkerboard  sensor in it) and connect to the engineer wifi access point (password heathack), but instead of going to the main setup screen, go to this link:  

- [192.168.4.1/extra - this link will only work for a few minutes when the sensor unit is first turned on](http://192.168.4.1/extra)

There's a radio button to switch to Memory - leave everything else as it is and click Submit.  From here it will take you to the main setup screen where you can proceed as in the standalone guide. Before you press "Download and Start", please check that the temperature reading looks sensible.  It might be a bit high because you've been handling it, but in the right ballpark.  If it looks wrong, go back to http://192.168.4.1/extra and make sure DHT22 is selected. 

```{admonition} Important Note

You must press "Download Data and Start" for this to work, but if you don't have data you want already stored on the device, you can throw the downloaded file away.  ```

If you are converting your unit to standalone permanently, please contact us.  Internet-connected units are more expensive and difficult to build, so we may ask you to swap for a simpler unit.