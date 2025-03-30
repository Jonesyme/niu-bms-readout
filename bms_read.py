#!/usr/bin/env python3
"""
Simple script to read data from the BMS in a Niu 48V/31Ah battery pack.
Communication is RS-485 @ 9600 8E1

Inspired by embedded code found at:
https://www.elektroroller-forum.de/viewtopic.php?t=8776&sid=4988eacad78e7169833be290458c63f0
"""

import argparse
import binascii
import logging
import struct
import sys

import serial


class BMSReader:
    """Connect and read data from the BMS of a Niu 48V/31Ah battery pack"""

    def __init__(self, device, verbose):
        self._serial = serial.Serial(
            device,
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_ONE,
            timeout=0.5,
            exclusive=True,
        )
        self._log = logging.getLogger("BMSReader")
        handler = logging.StreamHandler(sys.stdout)
        if verbose:
            self._log.setLevel(logging.DEBUG)
        else:
            self._log.setLevel(logging.INFO)
        handler.setFormatter(
            logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
        )
        self._log.addHandler(handler)

    # def send_cmd1(self):
    #     """Read something unused"""
    #     cmd_bytes = b"\x34\x5f\x66"
    #     self._send_cmd(cmd_bytes)
    #     self._read_header_and_data(cmd_bytes)

    def send_cmd2(self):
        """Read pack data and temperatures"""
        self._log.debug("Sending command 2")
        cmd_bytes = b"\x60\x42\x75"
        self._send_cmd(cmd_bytes)
        response = self._read_header_and_data()
        if len(response) == 0:
            return

        if len(response) != 17:
            self._log.error("Got %d when reading, expected 17", len(response))
            return

        self._log.debug(response)
        data = struct.unpack(">HHBBBBBBBBBBHB", response)
        pack_voltage = float(data[0] - 0x3333) / 10
        current = float(data[1] - 0x3333) / 10
        soc = data[4] - 0x33
        time_remain = float(data[6] - 0x33) / 10
        temp1 = data[7] - 0x33
        temp2 = data[8] - 0x33
        temp3 = data[9] - 0x33
        temp4 = data[10] - 0x33

        print(f"Pack voltage:\t{pack_voltage}")
        print(f"Current:\t{current}")
        print(f"SOC:\t\t{soc}")
        print(f"Time remaining:\t{time_remain}")
        print(f"Temperature 1:\t{temp1}")
        print(f"Temperature 2:\t{temp2}")
        print(f"Temperature 3:\t{temp3}")
        print(f"Temperature 4:\t{temp4}")

    def send_cmd3(self):
        """Read cell voltages"""
        self._log.debug("Sending command 3")
        cmd_bytes = b"\x6f\x5b\x9d"
        self._send_cmd(cmd_bytes)
        response = self._read_header_and_data()
        if len(response) == 0:
            return

        if len(response) != 42:
            self._log.error("Got %d when reading, expected 42", len(response))
            return

        self._log.debug(response)
        data = struct.unpack(">HHHHHHHHHHHHHHHHHHHHBB", response)
        cell1_u = float(data[0] - 0x3333) / 1000
        cell2_u = float(data[1] - 0x3333) / 1000
        cell3_u = float(data[2] - 0x3333) / 1000
        cell4_u = float(data[3] - 0x3333) / 1000
        cell5_u = float(data[4] - 0x3333) / 1000
        cell6_u = float(data[5] - 0x3333) / 1000
        cell7_u = float(data[6] - 0x3333) / 1000
        cell8_u = float(data[7] - 0x3333) / 1000
        cell9_u = float(data[8] - 0x3333) / 1000
        cell10_u = float(data[9] - 0x3333) / 1000
        cell11_u = float(data[10] - 0x3333) / 1000
        cell12_u = float(data[11] - 0x3333) / 1000
        cell13_u = float(data[12] - 0x3333) / 1000
        cell14_u = float(data[13] - 0x3333) / 1000
        cell15_u = float(data[14] - 0x3333) / 1000
        cell16_u = float(data[15] - 0x3333) / 1000
        cell17_u = float(data[16] - 0x3333) / 1000
        cell18_u = float(data[17] - 0x3333) / 1000
        cell19_u = float(data[18] - 0x3333) / 1000
        cell20_u = float(data[19] - 0x3333) / 1000
        print(f"Cell 1 voltage:\t{cell1_u}")
        print(f"Cell 2 voltage:\t{cell2_u}")
        print(f"Cell 3 voltage:\t{cell3_u}")
        print(f"Cell 4 voltage:\t{cell4_u}")
        print(f"Cell 5 voltage:\t{cell5_u}")
        print(f"Cell 6 voltage:\t{cell6_u}")
        print(f"Cell 7 voltage:\t{cell7_u}")
        print(f"Cell 8 voltage:\t{cell8_u}")
        print(f"Cell 9 voltage:\t{cell9_u}")
        print(f"Cell 10 voltage:\t{cell10_u}")
        print(f"Cell 11 voltage:\t{cell11_u}")
        print(f"Cell 12 voltage:\t{cell12_u}")
        print(f"Cell 13 voltage:\t{cell13_u}")
        print(f"Cell 14 voltage:\t{cell14_u}")
        print(f"Cell 15 voltage:\t{cell15_u}")
        print(f"Cell 16 voltage:\t{cell16_u}")
        print(f"Cell 17 voltage:\t{cell17_u}")
        print(f"Cell 18 voltage:\t{cell18_u}")
        print(f"Cell 19 voltage:\t{cell19_u}")
        print(f"Cell 20 voltage:\t{cell20_u}")

    def send_cmd4(self):
        """Read serial number"""
        self._log.debug("Sending command 4")
        cmd_bytes = b"\x3c\x43\x52"
        self._send_cmd(cmd_bytes)
        response = self._read_header_and_data()
        if len(response) == 0:
            return

        if len(response) != 18:
            self._log.error("Got %d when reading, expected 18", len(response))
            return

        self._log.debug(response)
        data = struct.unpack(">BBBBBBBBBBBBBBBBBB", response)

        serial_nbr = ""
        for i in range(16):
            serial_nbr += chr(data[i] - 0x33)

        print(f"Serial:\t{serial_nbr}")

    def send_cmd5(self):
        """Read HW/SW version"""
        self._log.debug("Sending command 5")
        cmd_bytes = b"\x35\x35\x3d"
        self._send_cmd(cmd_bytes)
        response = self._read_header_and_data()
        if len(response) == 0:
            return

        if len(response) != 4:
            self._log.error("Got %d when reading, expected 4", len(response))
            return

        self._log.debug(response)
        data = struct.unpack(">BBBB", response)
        if data[0] > 0:
            sw_ver = [(data[0] - 0x33) // 16, (data[0] - 0x33) % 16]
        else:
            sw_ver = [0, 0]
        if data[1] > 0:
            hw_ver = [(data[1] - 0x33) // 16, (data[1] - 0x33) % 16]
        else:
            hw_ver = [0, 0]

        print(f"Software version:\t{sw_ver[0]}.{sw_ver[1]}")
        print(f"Hardware version:\t{hw_ver[0]}.{hw_ver[1]}")

    def send_cmd6(self):
        """Read cycles, charged/discharged capacity"""
        self._log.debug("Sending command 6")
        cmd_bytes = b"\x5c\x46\x75"
        self._send_cmd(cmd_bytes)
        response = self._read_header_and_data()
        if len(response) == 0:
            return

        if len(response) != 21:
            self._log.error("Got %d when reading, expected 21", len(response))
            return

        self._log.debug(response)
        data = struct.unpack(">BBHBBBBBBBBBBBBBBBBB", response)
        cycles = data[2] - 0x3333

        print(f"Cycles:\t{cycles}")

    def _send_cmd(self, cmd_data: str):
        # Start of frame + preamble
        data = b"\xfe\xfe\xfe\xfe" + b"\x68\x31\xce\x68\x02\x02"

        data = data + cmd_data

        # append end of command
        data = data + b"\x16"

        self._serial.write(data)

    def _read_header_and_data(self) -> str:
        compare = b"\x68\x31\xce\x68\x82"
        header = self._serial.read(len(compare) + 1)

        if header[0:5] != compare or len(header) != len(compare) + 1:
            self._log.error("Header mismatch")
            self._log.error(
                "Expected %s, got %s",
                binascii.hexlify(compare),
                binascii.hexlify(header[0:5]),
            )
            return ""

        bytes_to_read = header[-1] + 2
        data = self._serial.read(bytes_to_read)
        if len(data) != bytes_to_read:
            self._log.error(
                "Data length mismatch, expected to read %d but got %d",
                bytes_to_read,
                len(data),
            )
            return ""

        if data[-1] != 0x16:
            self._log.error("Footer mismatch, expected 0x16, got %s", hex(data[-1]))
            return ""

        return data


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    required_args = argparser.add_argument_group("required arguments")
    required_args.add_argument(
        "-d",
        "--device",
        help="Serial device",
        required=True,
    )
    argparser.add_argument(
        "-v", "--verbose", help="Verbose logging", action=argparse.BooleanOptionalAction
    )
    args = argparser.parse_args()

    reader = BMSReader(args.device, args.verbose)

    reader.send_cmd2()
    reader.send_cmd3()
    reader.send_cmd4()
    reader.send_cmd5()
    reader.send_cmd6()
