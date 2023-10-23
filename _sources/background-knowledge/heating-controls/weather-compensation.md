(weather-and-load-compensation)=
# Weather compensation and load (room) compensation

Weather compensation and load compensation are energy efficiency features that can be used with modern modulating boilers that can vary their heat output by varying the boiler flow temperature - the temperature of the hot water fed to your radiators.

Weather compensation and load compensation, also called room compensation, vary your boiler flow temperature - the temperature of the hot water fed to your radiators. They make the water cooler when you need less heat.  When modern condensing boilers can run cooler, they use gas more efficiently because they can recover the heat, and the gentler delivery of heating makes it less likely that your system will overshoot its target temperature.

With weather compensation, the flow temperature will depend on the outside temperature, as obtained from an external temperature sensor or a GPS weather data service.  

With load/room compensation, the flow temperature will depend on the temperature inside your building, as obtained by one or more temperature sensors.

Systems with load compensation react more quickly to changes in the temperature inside your building than ones with weather compensation.  That's not always a good thing.  If your building is poorly insulated, doesn't all heat up at the same rate because it is of mixed construction, or has the room sensor in a room where the temperature is influenced by more than heating system, the internal temperature reading could vary in a way that doesn't reflect user comfort.  All the stopping and starting makes the boiler less efficient.   In these cases, weather compensation could be a better option.  On the other hand, weather compensation is really designed for buildings that are heated all the time.  In buildings that are heated occasionally, weather compensation increases warm up time.  Moreover, if you need the building at different temperatures for different user groups, you may need load compensation to make those changes happen.  

In general, weather compensation is more efficient than load compensation.

The more expensive weather compensation systems don't make you choose - with them, you set a weather compensation curve but also set a "room influence" parameter.  A small room influence will make the flow a little hotter than it would be otherwise if the indoor reading is cool.  A large room influence will change the flow temperature more.  

- [Weather compensation of load compensation? (Heat Geek)](https://www.heatgeek.com/weather-compensation-or-load-compensation/)
- [Guide to optimisation and compensation (The Heating Hub)](https://www.theheatinghub.co.uk/best-smart-heating-controls-compatibility-guide)
- [Explanation of boiler modulation (Heat Geek)](https://www.heatgeek.com/what-is-boiler-modulation/)

```{admonition} Stone: a special case 

If the stone building has *internal* wall insulation, ignore this box. 

Buildings made of stone and other materials that absorb and release heat slowly are something of a special case because they can't react quickly to changes.   Many groups have leaky stone buildings in occasional use and heat them by running the boiler hot to make the building comfortable in as short a time as possible.  This means weather compensation isn't useful.

It could be more efficient to heat the building lower and longer despite the occasional use, especially if it has a condensing boiler.  This could be achieved through a combination of a higher setback temperature and a steeper weather compensation curve.  This is also likely to be comfortable at a lower indoor air temperature because the walls be warmer. 

```

```{admonition} Choosing settings

You should check that your installer has thought about your building when setting the control system parameters, not just used the default settings or settings that they always use.  These are unlikely to suit your building and how you use it.  Unfortunately, if pressed, some installers will leave the settings up to you.

Weather compensators are controlled by choosing a curve that defines the flow temperature at different outdoor temperatures.  The flow temperature is always the same as the outdoor temperature when that is at or exceeds your target room temperature.  The flow temperature when it is cold out needs to be higher for buildings with higher heat loss, making a steeper (higher) "heating curve".  With 24/7 heating, the most efficient choice of curve is the lowest one that will still let your building reach its target temperature and there must be rules of thumb for initial values to use based on the building's construction.  

We have not found good advice for how to choose inital values where weather compensation is combined with room influence, or when the building isn't heating constantly and there is a compromise to be made between the curve steepness and the building's warmup time.  As far as we can tell, proper optimisation can only be achieved through experimenting while taking regular meter readings and using weather data to do degree day measurement.  The maths for this doesn't look too bad for venues with regular heating schedules but it soon gets very complicated if the heating schedule varies week to week.  

Many manufacturers have models that include both optimised start control and weather compensation.  This makes the experimentation to optimise the system more difficult.  

We hope through this programme to develop a better understanding of the difficulties our buildings face that will lead to better advice.

```


```{admonition} Old boilers

There are ways of faking weather compensation with an older on/off boiler, but in a community building, it's unlikely this would be worthwhile. We describe this mostly in case you already have such a system.   Some very old weather compensators for on/off boilers use a motorised valve to mix cold water in with the flow to cool it down. Other controllers have a  feature called "time proportional interval" that simply turns the boiler off for a proportion of the time that it is scheduled to run, where the proportion is higher when it is warm out.  

```