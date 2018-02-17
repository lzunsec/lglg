#!/usr/bin/env python

import libvirt
import yaml

yaml_path = "linux.yaml"
image_xml_path = "ubuntu_base.xml"
emulator = "qemu"
connection = libvirt.open(emulator + ":///system")

# This lists all domains on the host
connection.listDefinedDomains()

xml = ""
with open(image_xml_path, "r") as file:
	xml = file.read()

yaml_data = ""
with open(yaml_path, "r") as file:
    yaml_data = yaml.load(file)

print(yaml_data)

connection.defineXML(xml)

connection.listDefinedDomains()
