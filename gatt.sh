#!/bin/bash

DEVICE_MAC="C0:49:EF:92:5E:66 "

{
echo "connect"
sleep 1  # give it a second to connect
echo "char-write-req 0x000c 11"
sleep 1
echo "exit"
} | gatttool -b $DEVICE_MAC --interactive

exit
