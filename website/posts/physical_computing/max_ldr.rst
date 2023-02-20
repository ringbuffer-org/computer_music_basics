.. title: Max for Live: Light Dependent Resistor
.. slug: max4live_ldr
.. date: 2023-02-08
.. tags:
.. category: basics:interfaces
.. priority: 4
.. link:
.. description:
.. type: text

This example shows how to send serial data from a single sensor
from an Arduino to Max for Live. The stream of data will be used
to control the cutoff frequency of a subtractive synth patch.




----

Breadboard Circuit
==================

The breadboard circuit for this example is the same used
in the first Arduino-Sensor-Circuit:

.. figure:: /images/basics/ldr_input_fritzing.png
  :figwidth: 100%
  :width: 44%
  :align: center


----

Arduino Code
============

The same Arduino code can be used to send data to Max or Max for Live:

.. code-block:: cpp

    int analogInput = 0;

    void setup()
    {
      Serial.begin(9600);
    }

    void loop()
    {

      float value = analogRead(analogInput);

      Serial.println(value);

      delay(5);
    }


-----

Max 4 Live Patch
================

The following patch is a ``Max Instrument``` which has two audio outputs.
It can be used like any other Live synthesizer.

No additional objects or packages are required
for getting the Arduino's data to Max or Max for Live via USB serial.
Receiving the data sent from the above Arduino code is managed with the ``serial`` object
in Max.
It needs the same baud rate as the sender (9600) as second argument and
the Arduino's serial port ID as first argument.
Clicking ``print`` gives the list of serial devices in the max console.
Enter the result into the ``serial`` object (in this case 'd' for 'usbmodem').

Once the proper id is set, the ``metro`` object can be started using the toggle switch.
Every ten milliseconds, data is read from the serial port.
The following objects unpack and format the stream and turn it into an integer.
The resulting values are just scaled and used for the cutoff frequency of two
parallel low pass filters.


.. figure:: /images/basics/arduino/max4live_ldr.png
  :figwidth: 100%
  :width: 66%
  :align: center

  LDR controlled subtractive synth in the Max device editor.




----

Additional Resources
====================

`This example <https://maker.pro/arduino/tutorial/how-to-send-and-receive-data-between-an-arduino-and-maxmsp>`_ works with the same approach.
