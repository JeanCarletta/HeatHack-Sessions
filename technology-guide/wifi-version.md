# Instructions for internet-connected version

You have two boxes - a sensor unit and a hub.  The sensor unit is usually white and the hub is usually black. 

The sensor unit takes the temperature and relative humidity readings and sends them to the hub using a radio link.  The hub then uploads the data to the internet.  To make this work, you need to tell the hub the password for the guest wifi network in your building.

:TODO: add a picture of the hub and sensor unit together.
<!-- 
```{image} TODO.jpg
:alt: sensor unit and hub
:class: bg-primary mb-1
:width: 400px
:align: center
```
 -->

```{admonition} Safety
:class: important
It's possible for someone who knows what they're doing to find out the wifi password if they steal the hub and then, while they are still on your premises, see what else they can access on your network.  If this worries you, please ask us how to reconfigure your sensor unit to work without an internet connection.
```

The sensor unit is battery-powered, but the hub has to be plugged using a phone charger.  It uses the older style "micro-USB" connectors like for older Android phones.  Many people have old chargers from previous phones.  If you don't have one with the right connector, but do have one where the cable detaches, micro-USB cables are cheap.  

```{image} micro_usb_connector.jpg 
:alt: Micro USB connector
:class: bg-primary mb-1
:width: 400px
:align: center
``` 
*(c) <a href="http://www.freeimages.co.uk/">freeimageslive.co.uk</a>, licensed under Creative Commons <a href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a>.*


```{admonition} Overview for technophiles

1.	Plug in the hub unit and turn on the sensor unit.
2.	Connect your phone/tablet/laptop to the open heathackhub hotspot
3.	Visit 192.168.4.1 using your browser.
4.	Select your Wi-Fi network from the list or enter the SSID manually, then enter your Wi-Fi password.
5.	Reconnect your phone/tablet/laptop to your Wi-Fi and visit the thingspeak.com link printed on the hub unit box. 
6.	Confirm the setup has been successful by checking for an initial reading of 1°C on the temperature graph.
```



