# Instructions for internet-connected version

You have two boxes - a sensor unit and a hub.  The sensor unit is usually white and the hub is usually black. 

The sensor unit takes the temperature and relative humidity readings and sends them to the hub using a radio link.  The hub then uploads the data to the internet.  To make this work, you need to tell the hub the password for the guest wifi network in your building.

```{image} ../images/sensor-unit-and-hub.jpg
:alt: sensor unit and hub
:class: bg-primary mb-1
:width: 400px
:align: center
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

1.	Plug in the hub
2.	Connect your phone/tablet/laptop to the open heathack wifi hotspot
3.	Visit 192.168.4.1 using your browser
4.	Enter the SSID and password for the venue's guest wifi network 
5.  Turn on the sensor unit and check for a blue flashing light on the hub showing the radio connection is working
5.	Visit your thingspeak.com URL to see data coming in
```

<!-- Colin's preferred version 
1. Plug in the hub unit.
2. Connect your phone/tablet/laptop to the open heathack hotspot
3. Visit 192.168.4.1 using your browser.
4. Select your Wi-Fi network from the list or enter the SSID manually, then enter your Wi-Fi password.
5. Reconnect your phone/tablet/laptop to your Wi-Fi and visit the thingspeak.com link printed on the hub unit box.
6. Confirm the setup has been successful by checking for an initial reading of 1°C on the temperature graph.
7. Turn on the sensor unit: it will start transmitting automatically.
8. For the first two minutes it transmits every 10 seconds and the hub flashes a little LED when it receives the transmittion.
9. Look in the hole in the hub case and you should see a blue flash every 10 seconds which lets you check you haven't put the sensor out of range.
10. If positioning takes a while you can restart the sensor for another spell of 10 second transmissions.
11. The range will be greatest when the aerials are pointing at right angles to the direction of the other unit.
(we will have an arrow on each box so maybe we word this differently)
-->

