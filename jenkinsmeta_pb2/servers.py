#!/usr/bin/env python2
import computers_pb2

class Servers():
    def __init__(self):
        self.protocol = servers_pb2.Servers()

    def debug(self):
        return self.protocol
