# Check the connection


```{image}  /images/monitoring/wifi-sequence/thingspeak-graph.png
:alt: a very basic thingspeak graph
:class: mb-1
:width: 400px
:align: center
```

To check that the hub is working, connect to the internet the way you ordinariliy would and use your browser to go to the thingspeak.com address printed on your box.  

You will see three very basic graphs.  These are just to see if it's working.  We provide other ones for working with the data.  

You will get a fake voltage reading of 1 every time you power cycle the hub.  This is just so we can tell whether it has connected successfully to the internet.  In later models instead of 1 you will see a voltage reading.

If the sensor unit is working, when you power cycle the sensor unit you will also see a sequence of rapid temperature readings.  If they aren't sensible, the most likely cause is low battery voltage.  The ideal voltage is 3.3V.  The sensor can tolerate the range 3-3.5V.  We are having issues with our voltage readings and they are only approximate, so if you need to test the actual battery voltage, use a multimeter.

If you don't see any readings at all, the most likely problem is that the sensor unit is too far from the hub, although it could also be a completely dead battery or a damage to the sensor unit.

Once they are working,if anyone turns the sensor unit or hub off, they will start working again when you turn them back on.  You may wish to leave a note at the power socket, as cleaners often turn hubs off and stick them in the lost and found.

