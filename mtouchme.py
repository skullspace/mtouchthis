#!/usr/bin/env python

# Copyright (C) 2014 Skullspace
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.

from string import ljust

from sys import argv

def binary_str_of_byte(byte_ord):
    return_value = hex(byte_ord)
    for i in range(8):
        return_value = str(byte_ord & 0x1) + " " + return_value
        byte_ord = byte_ord >> 1
    return return_value

yo = open(argv[1], 'r')
while True:
    da_byte = ord(yo.read(1))
    print binary_str_of_byte(da_byte),
    if da_byte & 0x40:
        if da_byte & 0x2:
            print " trouble skip"
            continue
        das_packet = yo.read(4)
        status = "release" if da_byte & 0x01 else "touch"
        post_status = " (with extra funky bit)" if 0x10 & da_byte else ""
        print " %s: %x %x | %x %x%s" % (
            status,
            ord(das_packet[0]), ord(das_packet[1]),
            ord(das_packet[2]), ord(das_packet[3]),
            post_status
            )
    else:
        print " threw away"
