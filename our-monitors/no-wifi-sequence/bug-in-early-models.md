# Bug in early models

If you have one of our early devices, there is a problem with them - after around a month the device will fill up and when you try to download the data, nothing will happen.

You can work around this problem as follows:

- **If it is not full yet.**

Download the data as usual and then restart the unit by turning it off and on again.  Connect as usual, but this time visit 192.168.4.1/deleteAllRecords. It should very quickly send you back to the normal screen you usually see. Choose "Download and Start" as usual.  It will download a very small file which you can discard.

- **If is is full and download takes forever.**

Restart the unit, and go to  192.168.4.1 as normal to ensure you are connected.  Then type in a new address to visit, 192.168.4.1/deleteAllRecords. 

This will empty the full storage space and start logging, but you will have lost the previous data.

<!-- :TODO: check it really starts logging automatically - i bet he means you have to press download and start. -->