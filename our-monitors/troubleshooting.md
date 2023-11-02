(troubleshooting)=
# Troubleshooting

These tips are for versions 1 and 2 of the monitor.

- **Temperature looks wrong.** Turn the sensor unit off and on, connect to the engineer network, and then visit http://192.168.4.1/extra.  Make sure DHT22 is selected.  If the sensor only reads a little warm, that may be because you've been handling it.

- **Turning hub on and off doesn't start the heathackhub network.** Probably you've already successfully entered your wifi network's SSID and password, so your hub is connecting to the internet.  If you want to change to a different wifi network, you need to move out of range of the current one first.  You may be able to visit your router admin page to see if you can spot the hub on your network; turning the hub off and on will make it appear and disappear.  You can also look for a 1 in field 3 (usually labelled "Voltage") on your ThingSpeak feed.  Otherwise, a dodgy power connection is the most likely cause; turn the hub off and on and look for a single blue flash.

