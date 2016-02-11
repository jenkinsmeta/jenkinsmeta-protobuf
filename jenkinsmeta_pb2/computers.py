#!/usr/bin/env python2
import computers_pb2

class Computers():
    def __init__(self):
        self.protocol = computers_pb2.Computers()

    def to_json(self):
        pass
