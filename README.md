# Niu Battery BMS Diagnostic Reader 
---
### Works with 48V and 60V Niu Batteries associated with N1S and other Niu bikes
  A simple python script to read data from a NIU BMS battery pack. <br />
  Provides equivelent BMS diagnostic functionality the official Niu H1 diagnostic tool.

### Communication protocol: 
* RS-485 @ 9600 8E1

### Hardware Requirements:
* Tested using the following USB->RS-485 adapter for $15: [from Amazon](https://www.amazon.com/Industrial-USB-RS485-Converter-Communication/dp/B081MB6PN2)

### Instructions
  1. Make sure you have `Python3` installed along with `pyserial` library
  2. Connect RS-485 terminals A+ and B- to battery port as shown below (female connector).
     ```
     +-----------+
     | A+ B- Gnd |
     |   +   -   |
     +-----------|
     ```
  3. Find device name associated with your RS-485 adapter<br />
     > Linux users can run the following, then plug RS-485 adapter into PC and see new device name appear:
     >```
     >dmesg | grep tty
     >sudo udevadm monitor -u
     >```
     - For Windows `[DEVICE-NAME]` will likely be similar to the form `COM0`
     - For Linux `[DEVICE-NAME]` will likely be in the form of `/dev/TTYUSB0`    

  4. Run python script:
     ```
     python3 bms_read.py -d [DEVICE-NAME]
     ```

### Example readout from script:
```
Pack voltage:	69.4
Current:	0.0
SOC:		  93
Time remaining:	  0.0
Temperature 1:	  0
Temperature 2:	  19
Temperature 3:	  19
Temperature 4:	  20
Cell 1 voltage:	  3.823
Cell 2 voltage:	  3.823
Cell 3 voltage:	  3.822
Cell 4 voltage:	  3.825
Cell 5 voltage:	  3.827
Cell 6 voltage:	  3.835
Cell 7 voltage:	  3.827
Cell 8 voltage:	  3.835
Cell 9 voltage:	  3.833
Cell 10 voltage:	3.821
Cell 11 voltage:	3.83
Cell 12 voltage:	3.825
Cell 13 voltage:	3.819
Cell 14 voltage:	3.836
Cell 15 voltage:	3.837
Cell 16 voltage:	3.823
Cell 17 voltage:	3.832
Cell 18 voltage:	0.0
Cell 19 voltage:	0.0
Cell 20 voltage:	0.0
Serial: SNXXXXXXXXXXXXXX
Software version:	2.0
Hardware version:	1.1
Cycles:	92
```
