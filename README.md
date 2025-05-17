# AI Data Platform Johannesburg IoT Gift

![logo](images/logo.jpg)


This repository is dedicated to creating a starting point for your new and shiny Rapsberry Pi Pico using Azure IoT via Azure IoT Central.  

Start with the <b>Getting Started</b> page for the Pico provided by the <b>Raspberry Pi Foundation</b>  [Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)

Follow the <b>Getting Started</b> page for Azure IoT Contral provided by <b>Microsoft</b>  [IoT Central](https://learn.microsoft.com/en-us/azure/iot-central/core/howto-create-iot-central-application?tabs=azure-portal
)  

Create a new Device Template by clicking on the <b>New</b> button

![NewTemplate](images/newtemplate.png)

Create an IoT Device which is a cloud connected IoT Device.

![NewTemplateDevice](images/newtemplateiotdevice.png)

Provide a template name.

![CreateTemplate](images/templatename.png)

Create the Template.

![CreateTemplate](images/createtemplate.png)

Import the provided model.  This is found in the <b>Models</b> folder within the Github repository.

![ImportModel](images/importmodel.png)

Once imported, generate template views from the model.

![GenerateViews](images/generateviews.png)

Publish the template as a versioned template.

![PublishTemplate](images/publishtemplate.png)

Create a new device using the created template.

![NewDevice](images/newdevice.png)

Create the new device with name and device id.   Be sure to select the previously created template.

![DeviceFields](images/createdevicefields.png)

Open the Device Connection screen.

![DeviceConnect](images/deviceconnect.png)

Take note of all the connection settings for using in the provided source code.

![NewTemplate](images/connectionsettings.png)

Build the cicuit on the breadboard using the provided components.

![breadboard](images/picogift_bb.png)

Edit the provided code.  Provide your wifi <b>SSID</b> and <b>WIFIPASSWORD</b>

![breadboard](images/wifi.png)

Provide the <b>SCOPEID</b>, <b>DEVICEID</b> and <b>PRIMARYKEY</b>

![breadboard](images/provisionsettings.png)


Run the application on the Pico and have FUN!

![breadboard](images/running.png)