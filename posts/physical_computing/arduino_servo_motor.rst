.. title: Controlling a Servo with Arduino
.. slug: servo_with_arduino
.. date: 2023-02-10
.. tags:
.. category: basics:interfaces
.. priority: 10
.. link:
.. description:
.. type: text
.. has_math: true

Servo motors are digitally controlled actuators, which allow the precise setting of angles via pulse-width encoding.
Servos used in RC models are low-cost and easy to program, which makes them attractive for prototyping in sound art and other DIY projects.
The following example is a copy of the `original example at Arduino <https://docs.arduino.cc/learn/electronics/servo-motors>`_.

----

Breadboard Wiring
=================

Connecting the servo motor to the Arduino requires no additional parts, except for
jumper cables. It is directly powered from the Arduino's 5V pin (larger servos may require an additional power source)
and receives data from the Pulse-With-Modulation pin ~9:

.. figure:: /images/basics/arduino/servo_arduino_bb.png
  :figwidth: 100%
  :width: 44%
  :align: center
  :alt: Arduino breadboard wiring for servo motor.

  Arduino breadboard wiring for servo motor.



----

Arduino Code
============

The following code lets the sweep 180 degrees forward and backward,
managed by two for loops (count up / count down) inside the main loop.
Most consumer servos manage this range from 0 to 180 degrees and wrap exceeding
values accordingly.

.. code-block:: cpp

  #include <Servo.h>

  Servo myservo;
  int pos = 0;

  void setup() {
    myservo.attach(9);
  }

  void loop() {

    for (pos = 0; pos <= 180; pos += 1) {
      myservo.write(pos);
      delay(15);
    }

    for (pos = 180; pos >= 0; pos -= 1) {
      myservo.write(pos);
      delay(15);
    }
  }



-----

Exercise
========

.. admonition:: Exercise

		Combine the servo example with the sensor example to control the position 'manually'.
