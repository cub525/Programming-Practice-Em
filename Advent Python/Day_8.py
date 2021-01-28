# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:53:29 2021

@author: janih
"""

import dataclasses as dtcls
from typing import List


with open("input_day_8.txt","r") as f:
    comms = [line.rstrip() for line in f]

@dtcls.dataclass()
class GameConsole:
    commands: List[str]    
    def __post_init__(self):
        self.used = []
        self.accumulator = 0
        self.index = 0

    def execute(self):
        while True:
            self.used.append(self.index)
            if (cmd := self.commands[self.index][:3]) == "nop":
                self.index += 1
            elif cmd == "acc":
                self.accumulator += int(self.commands[self.index][4:])
                self.index += 1
            elif cmd == "jmp":
                self.index += int(self.commands[self.index][4:])
            if self.index in self.used:
                return self.accumulator

    def debug(self):
        change_list = []
        try:
            while True:
                if not self.index in change_list:
                    self.used.append(self.index)
                    change_list.append(self.index)
                    if (cmd := self.commands[self.index][:3]) == "jmp":
                        self.index += 1
                    elif cmd == "acc":
                        self.accumulator += int(self.commands[self.index][4:])
                        self.index += 1
                    elif cmd == "nop":
                        self.index += int(self.commands[self.index][4:])
                        # if self.index in self.used:
                        #     pass
                    self.execute()
                    self.accumulator = 0
                    self.index = 0
                    self.used.clear()
                else:
                    self.used.append(self.index)
                    if (cmd := self.commands[self.index][:3]) == "nop":
                        self.index += 1
                    elif cmd == "acc":
                        self.accumulator += int(self.commands[self.index][4:])
                        self.index += 1
                    elif cmd == "jmp":
                        self.index += int(self.commands[self.index][4:])
        except IndexError:
            return self.accumulator
        

g = GameConsole(comms)
solution = g.debug()