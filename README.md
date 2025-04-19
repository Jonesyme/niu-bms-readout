# Niu Battery BMS Diagnostic Reader 
### Works with both 48V/60V Niu Batteries for N1S and other bikes

A simple python script to read data from a NIU BMS battery pack. This provides the same BMS functionality as the Niu H1 diagnostic tool (at least as far as its BMS feature, not others).

### Communication protocol: 
  `RS-485 @ 9600 8E1`
### Hardware Requirements:
* Tested using a cheap USB<->RS485 dongle available for $15: [from Amazon](https://www.amazon.com/Industrial-USB-RS485-Converter-Communication/dp/B081MB6PN2)

### Instructions:
* Connect RS-485 dongle's A+ and B- connections to battery port as shown below (female connector).
```
+-----------+
| A+ B- Gnd |
|   +   -   |
+-----------+
```
* Then run python script using following command:
    ```bms_read.py -d [USB-DEVICE-NAME]```

  On Windows the `[USB-DEVICE-NAME]` will likely be `COM0` on Linux it will likely be `/dev/TTYUSB0`.  For more help google how to find USB device name.

### Example readout from script:
