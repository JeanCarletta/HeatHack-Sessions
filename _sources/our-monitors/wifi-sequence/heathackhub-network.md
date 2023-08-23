# Connect to the wifi hotspot

```{image} /images/monitoring/wifi-sequence/connect-to-heathackhub.png
:alt: connect to heathackhub wifi hotspot
:class:  mb-1
:width: 400px
:align: center
```
The heathackhub network will appear.  Connect to it.  It is an open network and doesn't require a password. If you were already connected to a wifi network, this will disconnect you from that network.

```{admonition} One at a time

Only one person at a time should try this step - the hub gets confused if two people are both trying to connect. If you have trouble and someone else wants to try with their phone, turn the hub off and on again.
```

Ignore any warnings about internet not being available - keep the wifi connection to the hub anyway. You will be unable to use the internet while you are connected to the hub.

Every time you turn the hub on and off, if it is connected to the internet it will send a 1 to "Field 3" of your ThingSpeak channel.  This is useful for knowing whether it is working, although there is a delay of arbitrary length before the 1 appears.  Any readings above 1 on Field 3 show your sensor unit's voltage but also demonstrate it has been working.  These other readings are only sent occasionally.

```{admonition} Important

Once you are successful, you won't be able to see the heathackhub network again even if you turn the router off and on - because the hub will connect automatically to the internet instead.  You will only see the heathackhub network if you move out of wifi range.  The hub only stores the details for one wifi network at a time.
```
