(internet-control-features)=
# Internet controls

```{admonition} Needs improvement

We intend with experience and through some of our expert advisers to improve this section, and will do our best to support venues that need more help with this as we learn. We mention brand names because it's hard to help our venues without, but this information is based solely on internet research.

```

It used to be difficult to find controls that had the right features for community buildings.  This is becoming easier with the introduction of internet controls that can communicate with each other using radios or over a wifi network and that you set using a phone app or website.  It's easiest to find ones that are designed for use in homes, and these are often suitable.  There are companies that market models for larger buildings that integrate more closely with more advanced heating control systems and that may work better over longer distances.

```{admonition} "Smart controls"
:class: tip

Some sources use "smart" to mean controls with energy efficiency features:  optimisation, weather compensation, and/or load compensation.  Others use "smart" to mean internet controls. 

"Smart thermostatic radiator valve (TRV)" can mean either 

- a TRV that you can program with a heating schedule and control using a phone app, usually only when you are within 10m of the radiator or sometimes only when your phone is touching the TRV.  
- a TRV that you can program and control over the internet, where you might be able to make all the TRVs in a room behave together, and the TRVs might be capable of turning the boiler on and off.

On this page, we're assuming the second type.  Some manufacturers describe the first type as "stand-alone" or "wireless", but you have to read the documentation to be sure.
```

Internet controls usually:

- incorporate modern energy efficiency features like optimised start control and weather compensation. 
- usually allow building users to make temporary thermostat changes within limits you set.  For rooms with multiple thermostatic radiator valves (TRVs), you can set them up so that adjusting one adjusts them all.  However, models designed for commercial buildings might not allow users to make any changes.
- allow you to program the heating timings for individual rooms even if your heating isn't zoned, by controlling smart TRVs.

Some heavily advertise that they will learn your heating schedule - not generally a useful feature in community buildings - but we think they all will let you set a heating schedule instead.

They also have some disadvantages:

- They require building wifi, a major expense if you don't already have it.
- It might take some experimentation to get all the components to communicate with each other, especially in stone buildings.
- If you have many radiators in rooms you want to control individually, the costs soon mount up.
- Not many of our heating suppliers have experience installing and configuring them.
- Their security can be poor.  This is something the UK is trying to address through legislation.
- They usually use batteries that you will have to remember to change or your devices will stop working.  That probably means replacing them all at once when you think they are about to fail, so that you still serve your users well. A few brands don't use batteries, instead generating electricity to run the devices from the heat of the radiator (e.g., DEOS.AG) or by powering the TRV from the mains (e.g., Danfoss Ally).
- Being more expensive than standard TRV heads, they are more likely to be stolen, although some vendors have theft protection systems for use in public buildings.

Just like with other heating controls, it's necessary to check all the details on the system you have in mind, and sometimes to ask questions of the manufacturer.  

- Not all internet controls make use of the ability of modern boilers to modulate their output.  This could lose the energy efficiency advantage of a newer boiler.
- In some systems, the individual TRVs can fire up the boiler.   In others, they just control the flow of water through the radiator.
- With some internet controls, changes to the heating can only be done using a phone app or website.  That might mean registering the leaders of every group that uses your building.

- Some manufacturers advise you to call for advice if your system is gravity fed rather than being a combi-boiler or a high pressure system.  This is common with old Victorian pipework, for instance, in church buildings.
- With some brands, the TRV heads are larger than usual or intended for only horizontal or only vertical use.


```{admonition} Radio and wireless range
Internet controls communicate with you and with each other using radio frequencies.   If there are stone walls or lots of obstacles between two devices that need to communicate by radio, the signal might not be strong enough for the system to work.  If your building is like this, you may be better off with lower radio frequencies, since they pass through stone more readily.  The radio frequencies in use for internet heating controls, from low to high, with some companies that use them, are: 

- 433 MHz - Energenie, Lightwave
- 868 MHz - Honeywell, Tado, Netatmo, Aeotec, Danfoss Living Connect; anything that uses the Z-Wave protocol
- 1.9 GHz - anything that uses the DECT Ultra Low Energy protocol
- 2.4 GHz - Drayton Wiser, Danfoss Ally, Hive (from British Gas), Tuya; anything that uses the Zigbee or Bluetooth protocols or where all the devices communicate by Wifi 

For the range, the power of the radio and whether the various devices can pass messages via devices that are closer to the centre also matter.  The security of the different protocols also varies. Devices that use the Lora/LoraWAN protocol might be operating at 433, 868, or 915 MHz and are generally aimed at large commercial buildings or even whole estates.

There are many competing manufacturers for "smart" TRVs. We think Google Nest can operate with a range of devices, but there is some confusion on the web as they retire the "Works with Nest" programme in favour of tighter control.  Don't get confused if you see 160 MHz mentioned on their web pages; it's to do with a kind of wireless internet that isn't in use in the UK. 

Wireless internet is 2.4 GHz and this is always what the main component uses to try to reach your wireless router so you can control the system from an app or website.  The trick is to get the main component close enough to the TRVs that need controlled for it to reach, but also close enough to your router.  You can check the wireless internet (wifi) signal strength in different parts of your building using your phone.  There are two ways to get signal to an area that doesn't have it.  If the router and the new area are on the same phase of electricity, you can use an internet over powerline extender.  Otherwise, you need a more powerful router or a wireless repeater between the two locations.   

```

```{admonition} More information

These resources compare the most popular systems and models, but there are many more out there.

- [Internet control comparisons from the Heating Hub](https://www.theheatinghub.co.uk/nest-thermostat-vs-hive-heating-vs-worcester-wave)
- [Smart TRV guide from The Heating Hub; includes wireless/standalone](https://www.theheatinghub.co.uk/smart-radiator-valves-product-and-compatibility-guide)

```

<!-- - [BEAMA list of smart TRVs on UK market, 2020](https://www.beama.org.uk/resourceLibrary/smart---connected-trvs.html) List suspiciously short! maybe British only? -->
