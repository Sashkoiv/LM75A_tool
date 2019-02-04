# LM75A tool
For setting Overtemterature Shutdown.

[![LM75A](https://img.shields.io/badge/NXP-LM75A-7EA5DD.svg)](https://www.nxp.com/docs/en/data-sheet/LM75A.pdf)
[![I2C](https://img.shields.io/badge/I2C-tutorial-00AD6B.svg)](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/)

## CLI commands
Also available by calling Usage command.

- -a (--addr) set device address (DEC)
- -b (--bus) set bus number
- -O (--os) set upper temperature treshold
- -H (--hyst) set lower temperature treshold
- -h (--help) usage help obviously=)

## Example
* Install required packages
```sh
$ sudo apt-get update
$ sudo apt-get install -y python-smbus i2c-tools
```
* Chech if i2c enabled
```sh
$ lsmod | grep i2c
```
* Check addresses on the bus
```sh
$ i2cdetect -y 1
```
* Run script with default values.
```sh
$ cd lm75a_tool
$ python lm75a_tool.py -a 79 -b 1 -O 35 -H 25
```
* Output
```sh
Previous config
1010000 binary & 80.000000 read from OS
1001011 binary & 75.000000 read from HYST
Current config
100011 binary & 35.000000 read from OS
11001 binary & 25.000000 read from HYST
The temperature is:
10110 binary & 22.000000 Celsius
```