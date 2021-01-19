# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:53:29 2021

@author: janih
"""

import dataclasses as dtcls
from typing import List

comms = []
with open("input_day_8.txt","r") as f:
    for line in f:
        comms.append(line.rstrip())

@dtcls.dataclass()
class GameConsole:
    commands: List[str]    
    def __post_init__(self):
        self.used = []
        self.accumulator = 0
        self.index = 0

    def execute(self):
        while True:
            if (cmd := self.commands[self.index][:3]) == "nop":
                self.used.append(self.index)
                self.index += 1
            elif cmd == "acc":
                self.accumulator += int(self.commands[self.index][4:])
                self.used.append(self.index)
                self.index += 1
            elif cmd == "jmp":
                self.index += int(self.commands[self.index][4:])
                if self.index in self.used:
                    return self.accumulator

    def backwards(self):
        self.index = len(self.commands) - 1
        self.used_ = []
        while True:
            if (cmd := self.commands[self.index][:3]) == "nop" or cmd == "acc":
                self.used_.append(self.index)
                self.index -= 1
            elif cmd == "jmp":
                self.index -= int(self.commands[self.index][4:])
                if self.index in self.used:
                    break
        

g = GameConsole(comms)
solution = g.execute()