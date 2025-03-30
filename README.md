# Niu 48V/31Ah BMS Readout Tool

A simple script to read data from the BMS in a Niu 48V/31Ah battery pack. This should provide the same functionality as the Niu H1 tool used for battery (and other) diagnostics.

Inspired by embedded code found at [https://www.elektroroller-forum.de/viewtopic.php?t=8776&sid=4988eacad78e7169833be290458c63f0]. Protocol implemented there isn't fully compatible with the protocol used by my battery BMS, thus some deviations.

Communication is RS-485 @ 9600 8E1, I use it with a Digitus USB<->RS485 converter.

Connect RS-485 to A+ and B-, battery port as seen on battery (female connector).

```
+------------+
| A+ B- Gnd  |
|   +  -     |
+------------+
```
