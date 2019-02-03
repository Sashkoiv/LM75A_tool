# LM75A tool
For setting Overtemterature Shutdown.

[![LM75A](https://img.shields.io/badge/NXP-LM75A-7EA5DD.svg)](https://www.nxp.com/docs/en/data-sheet/LM75A.pdf)


## CLI commands
Also available by calling Usage command.

- -a (--addr) set device address (DEC)
- -b (--bus) set bus number
- -O (--os) set upper temperature treshold
- -H (--hyst) set lower temperature treshold
- -h (--help) usage help obviously=)

## Example
Default values shown.
```sh
$ cd lm75a_tool
$ python lm75a_tool.py -a 79 -b 1 -O 35 -H 25
```
Output
```sh
Previous config
100011 binary & 35.000000 read from OS
11001 binary & 25.000000 read from HYST
Current config
100011 binary & 35.000000 read from OS
11001 binary & 25.000000 read from HYST
The temperature is:
10110 binary & 22.000000 Celsius
```