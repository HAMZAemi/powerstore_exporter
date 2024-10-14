#!/usr/local/bin/python
import configparser
from urllib.parse import parse_qs
from dorado_gather import collect_data, prometheus_output

address="192.168.128.101:8088"

collect_data(address)
