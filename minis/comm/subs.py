#!/usr/bin/env python

import paho.mqtt.subscribe as subscribe
import time

x = subscribe.simple("ledstatus", hostname="ILSORT01.local", port=1883)

print x


