# Sensor calibration test - technical results

We are using cheap DHT22 temperature and relative humidity sensors in our sensor units.  They're pretty good,
but occasionally we get a rogue one in a batch.  To check the sensors before we send them out, we are trying
them the best we can against a reasonable range of temperature and relative humidity readings, comparing batches to each other and to a Lascar logger.  A better test would be against a mercury thermometer and a sling psychrometer, but that's time-consuming!  The DHTs are usually pretty good.  The test is just to make
sure we didn't get a rogue one in the batch.

```{image} calibrationSensors-1536x1152.jpg
:alt: our calibration test rig
:class: bg-primary mb-1
:width: 400px
:align: center
```
*Our calibration test rig.*

:TODO: write using blog post as source.  Include:  declared accuracy of Lascars (with disclaimer about
ours being old and real kit being calibrated frequently); ground truth being mercury thermometer and sling
psychrometer; if we really think cheaper could be worse quality, something about that, but I don't see why CK thinks that, market forces aren't about quality.  Are they all from one maker?  I think it's just occasional rogues in batches so that's what we're looking for.

Further reading: how a sling psychrometer works, DHT data sheet?, Lascar website?  - but there are other loggers out there, say so.

:TODO: Explain shower and fridge test. Forgot to add something about response time and how the DHT just seems to respond faster to temperature changes but that's not important in this setting, it's an artefact of using the fridge test.  RH shows the same property.  Remind reader also that RH about 80 is out of sensor declared range, we really don't care about the spread there.

:TODO: ensure all data sets are over a range.

:TODO: get the code to hide by default but you can see if you click.  This takes editing outside visual studio code - I think emacs just works, need to google on the right JSON to add for code metadata.


```{admonition} Tip
:class: tip

On the plots, you can zoom in by selecting the area you want to see, and out by double-clicking. You can also show and hide traces by clicking on their names in the legend.
```

