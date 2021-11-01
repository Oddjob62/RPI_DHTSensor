# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import datetime
import board
import sys
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

result_logged = False

while not result_logged:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        date = datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')
        print(
                "{}: Temp: {:.1f} C    Humidity: {}% ".format(
                date, temperature_c, humidity
            )
        )
        f = open("temp.txt", "a")
        f.write(
                "{}: Temp: {:.1f} C    Humidity: {}%\n".format(
                date, temperature_c, humidity
            )
        )
        f.close()
        result_logged = True
        dhtDevice.exit()
        sys.exit(0)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
