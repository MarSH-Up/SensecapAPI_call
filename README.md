<div align="center">
 <h1>Sensecap Weather Station for agriculture monitoring </h1>
</div>

<div align="center">
  <img src="https://seeklogo.com/images/S/seeed-studio-logo-4F3B000EB9-seeklogo.com.png" height="200"/>
  <br/>
  <a href="https://github.com/MarSH-Up/SensecapAPI_call">
    <img src="https://img.shields.io/badge/python-v3.7-blue">
  </a>
</div>


This repository is a small project that will work as an example of how to request the Sensecap API data using a minimal configuration to recompile all the data recompiled by the nodes or gateways deployed. 

This project uses the [SenseCAP S2120 8-in-1 LoRaWAN Weather Sensor](https://www.seeedstudio.com/sensecap-s2120-lorawan-8-in-1-weather-sensor-p-5436.html) to help a local farm in a community in Puebla, México, to take care of the crops they have as local production for the community. The station recompile:
- Air Temperature
- Air Humidity
- Barometric Pressure
- Rain Hourly
- Wind Speed
- Wind Direction 
- Light Intensity
- UV Index

Each one independently every 20 minutes using LoRaWAN from Helium coverage. Check the full project story in [Hackser.io](https://www.hackster.io/MarsUpM/sensecap-s2120-8-in-1-lorawan-weather-sensor-063603). 

## Docs & Resources

- [SenseCAP API](https://sensecap-docs.seeed.cc/introduction.html)
- [twilio](https://www.twilio.com/en-us/messaging/programmable-messaging-api)


## Running and building the app

```
#Install libraries
$ python pip install twilio

# Run
$ python src/SenseCapModel.py 
```

## Requirements

<div align='left'>
    <ul>
        <li>You may need to generate you API key from <a href='http://sensecap.seeed.cc/portal/#/dashboard'>SenseCAP Dashboard</a></li>
    </ul>
</div>

## To Do

<div align='left'>
    <ul>
        <li>Implement the systems in a fully chatbot where you can ask the data anytime</li>
        <li>Implement the project in a Raspberry PI as a local server</li>
    </ul>
</div>
