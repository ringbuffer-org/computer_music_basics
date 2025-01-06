.. title: Pure Data: Light Dependent Resistor
.. slug: puredata_ldr
.. date: 2023-02-08
.. tags:
.. category: basics:interfaces
.. priority: 2
.. link:
.. description:
.. type: text

There is a variety of different approaches for receiving (and sending) data via a serial port in PD.
The solution in this example relies OSC via serial and needs additional libraries for both the Arduino sender
and the PD receiver.
In return it offers a flexible approach for handling multiple sensors.


----

Breadboard Circuit
==================

The breadboard circuit is the same as in the first Arduino sensor example:

.. figure:: /images/basics/ldr_input_fritzing.png
  :figwidth: 100%
  :width: 33%
  :align: center


----

Arduino Code
============

For the following Arduino program, the additional `OSC Library <https://github.com/CNMAT/OSC>`_ by Adrian Freed
needs to be installed. It can be cloned from the repository or simply installed with
the builtin package manager in the Arduino IDE (``Tools->Manage Libraries``).
``OSCMessage.h`` is included in the code.
In addition, the type of serial connection is retrieved.
The ``OSCMessage`` class is used in the main loop to pack the data and send it.

.. code-block:: cpp

    #include <OSCMessage.h>

    #ifdef BOARD_HAS_USB_SERIAL
    #include <SLIPEncodedUSBSerial.h>
    SLIPEncodedUSBSerial SLIPSerial( thisBoardsSerialUSB );
    #else
    #include <SLIPEncodedSerial.h>
     SLIPEncodedSerial SLIPSerial(Serial);
    #endif

    void setup() {

        Serial.begin(9600);
    }

    void loop() {

      int sensorValue = analogRead(A0);

      float voltage = sensorValue;

      // Serial.println(voltage);

      OSCMessage msg1("/brightness");
      msg1.add(voltage);
      SLIPSerial.beginPacket();
      msg1.send(SLIPSerial);
      SLIPSerial.endPacket();
      msg1.empty();

    }


-----

Pure Data Patch
===============

The Pure Data receiver patch relies on the ``mrpeach`` externals: `mrpeach GitHub Repository <https://github.com/pd-externals/mrpeach>`_
Like many externals, they can be installed by cloning the repository to one of PD'2 search paths - or by using Deken. The external is named ``mrpeach``: `Instructions for using Deken </computer_music_basics/Puredata/installing-externals-with-deken/>`_

Serial data is received with the comport object. All available devices can be printed
to PD's console. The proper interface can be opened with an extra message or as
first argument of the object. On Linux systems, this is usually ``/dev/ttyACM0``.
The ``slipdec`` object decodes the SLIP-encoded OSC message, which is then
unpacked and routed.


.. figure:: /images/basics/pd-arduino-ldr.png
  :figwidth: 100%
  :width: 44%
  :align: center
