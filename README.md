# TPLink AP Scraper

A simple Python script to log into a TP-Link EAPxxx wireless access point and extract the client list.  Potentially useful for presence tracking of mobile devices, for building or home automation.

TP-Link EAP330 tested with firmware 1.2.0 - may work on other similar models.  Some models support extraction of client list via SNMP, but this model does not.  That is likely a better approach if yours supports it.

It's simple, fragile code meant to be used as an example to build upon for a real project.  Error checking is minimal, addresses and credentials are hardcoded in the Python script.  Output is a pretty table to stdout.

Library pre-reqs: request, json, hashlib, prettytable

