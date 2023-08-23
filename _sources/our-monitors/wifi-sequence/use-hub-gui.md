# Configure the hub

```{image} /images/monitoring/wifi-sequence/use-hub-gui.png
:alt: type URL
:class: mb-1
:width: 400px
:align: center
```
You should now see the hub's interface.  Choose "Configure Wifi", and choose the venue's guest wifi network from the list.  If you don't see it, refresh the list by choosing "Scan".  Then enter the wifi password and choose "Save".

Some venues deliberately hide the wifi network - in this case you can type in its name (SSID).  You may be able to look up the name using a phone you have used on the wifi before or find it on the back of the router. 

```{admonition} Important - heathackhub will disappear
If after you save the password, heathackhub disappears from your list of connections, the hub is probably  successfully connected to the internet.   You can also check by looking at your ThingSpeak feed.  You should see a very recent value in Field 3 - either a 1, meaning your hub has just newly connected, or in newer models, a voltage reading.  

If you don't see anything on ThingSpeak, you probably entered the wrong password and need to try again.
``` 

