.. title: SuperCollider: Light Dependent Resistor
.. slug: supercollider_ldr
.. date: 2023-02-08
.. tags:
.. category: basics:interfaces
.. priority: 3
.. link:
.. description:
.. type: text


This example shows how a single sensor can be streamed via
serial data from the Arduino to SuperCollider.


----

Breadboard Circuit
==================

The breadboard circuit is the same as in the first Arduino sensor example:

.. figure:: /images/basics/ldr_input_fritzing.png
  :figwidth: 100%
  :width: 44%
  :align: center


----

Arduino Code
============

For the SC example, serial data is sent in a simple way.
The additional scaling is optional, but makes it easier to
process the data in SuperCollider.

.. code-block:: cpp

    void setup() {

       Serial.begin(9600);
    }

    void loop() {

     int sensorValue = analogRead(A0);

     // scale to 0..1
     float voltage   = sensorValue/1024.0 ;

     Serial.println(voltage);

    }


-----

SC Code
=======

On Linux, the Arduino's serial interface can be found in the terminal:

.. code-block:: shell

    $ ls -l /dev/ttyACM*



On the SC receiver end, a serial port object is initialized with the matching serial interface:


.. code-block:: supercollider

    (
    p = SerialPort(
      "/dev/ttyACM0",
      baudrate: 9600,
      crtscts: true);
    )


A control rate bus is used to visualize the received data and make it accessible to other nodes:

.. code-block:: supercollider

    ~sensorBUS = Bus.control(s,1);
    ~sensorBUS.scope;


The actual receiving and decoding of the data happens inside a routine
with an infinite loop.
It appends incoming characters, until a return character (13) is
received. In this case, the assembled string is converted to a Float
and written to the sensor bus:


.. code-block:: supercollider

    (
    r= Routine({
        var byte, str, res;
        inf.do{|i|
            if(p.read==10, {
                str = "";
                while({byte = p.read; byte !=13 }, {
                    str= str++byte.asAscii;
                });
                res= str.asFloat;

                // ("read value:"+res).postln;

    			~sensorBUS.set(res);
            });
        };
    }).play;
    )




-----

External Resources
==================

The `SuperCollider Tutorial by Eli Fieldsteel <https://youtu.be/_NpivsEva5o>`_ shows a similar solution
for getting Arduino sensors into SuperCollider via USB.


-----

Exercise
========

.. admonition:: Exercise

    Create a synth node with a parameter mapped to the sensor bus.
