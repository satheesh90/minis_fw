#Standardisation of GPIOs of RPis

### Connections for NFC Reader - Adafruit PN532 with RPi

| NFC Reader   |  BCM GPIO  |  Physical Pin |
|--------------|:----------:|--------------:|
|     MOSI     |     10     |       19      |
|      SS      |      8     |       24      |
|     MISO     |      9     |       21      |
|     SCK      |     11     |       23      |


### Packet Position Sensors - Digital Output connections to GPIOs 

|Packet Position Sensors|  BCM GPIO  |  Physical Pin |
|--------------|:----------:|--------------:|
|     PPS1     |    18      |     12        |
|     PPS2     |    17      |     11        |
|     PPS3     |    27      |     13        |
|     PPS4     |    22      |     15        |

### Neighbourhood Detection Connections - RPi GPIOs

|Neighbourhood |  BCM GPIO  |  Physical Pin |
|--------------|:----------:|--------------:|
|     IN       |    19      |    35         |
|     OUT      |    20      |    38         |
|     LEFT     |    26      |    37         |
|     RIGHT    |    21      |    40         |

### DC Motor Control GPIOs for Pololu DRV8838

| Motors        | BCM GPIO(EN,PH)|Physical Pin(EN,PH)|
|---------------|:--------------:|------------------:|
|Conveyor Motor |     5, 6       |      16, 18       |
|Sorter Motor1  |   23, 24       |      29, 31       |          
|Sorter Motor2  |   12, 13       |      32, 33       |    

### Shutdown GPIO

|  Shutdown  |  BCM GPIO  |  Physical Pin |
|------------|:----------:|--------------:|
|  Shutdown  |    16      |    36         |

