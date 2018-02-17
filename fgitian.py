#!/usr/bin/env python

import libvirt

image_xml_path = "ubuntu_base.xml"
emulator = "qemu"
connection = libvirt.open(emulator + ":///system")

# This lists all domains on the host
connection.listDefinedDomains()

xml = ""
with open(image_xml_path, "r") as file:
	xml = file.read()

connection.defineXML(xml)

connection.listDefinedDomains()
