from dataclasses import dataclass
from APIclasses.creatureData import size, alignment, speed, walk, abilities, sense, action
import math
import tkinter.ttk as ttk

@dataclass
class creature:
    name: str
    size: size
    alignment: alignment
    base_ac: int
    base_hp: int
    hp: int
    hit_dice: str
    speed: list[speed]
    abilities: abilities
    proficiencies: list
    dmg_vulnerabilities: list
    dmg_resistances: list
    dmg_immunities: list
    condition_immunities: list
    senses: list[sense]
    language: list[str]
    actions: list[action]
    reactions: list[action]

    def getSTRbonus(self):
        return math.floor((self.abilities.strength - 10)/2.0)

    def getDEXbonus(self):
        return math.floor((self.abilities.dexterity - 10)/2.0)
    
    def getCONbonus(self):
        return math.floor((self.abilities.constitution - 10)/2.0)

    def getINTbonus(self):
        return math.floor((self.abilities.intelligence - 10)/2.0)

    def getWISbonus(self):
        return math.floor((self.abilities.wisdom - 10)/2.0)

    def getCHAbonus(self):
        return math.floor((self.abilities.charisma - 10)/2.0)

    def getAC(self):
        return self.base_ac

    def show(self, window):
        frame = ttk.Frame(window)

        ttk.Label(frame, text=f"Name: {self.name}").pack()
        ttk.Label(frame, text=f"Size: {self.size}").pack()
        ttk.Label(frame, text=f"Alignment: {self.alignment}").pack()
        ttk.Label(frame, text=f"AC: {self.getAC()}").pack()
        ttk.Label(frame, text=f"HP: {self.hp}").pack()
        ttk.Label(frame, text=f"Hit Dice: {self.hit_dice}").pack()
        self.showSpeed(frame)
        ttk.Label(frame, text=f"STR: {self.abilities.strength} - {self.getSTRbonus()}").pack()
        ttk.Label(frame, text=f"DEX: {self.abilities.dexterity} - {self.getDEXbonus()}").pack()
        ttk.Label(frame, text=f"CON: {self.abilities.constitution} - {self.getCONbonus()}").pack()
        ttk.Label(frame, text=f"INT: {self.abilities.intelligence} - {self.getINTbonus()}").pack()
        ttk.Label(frame, text=f"WIS: {self.abilities.wisdom} - {self.getWISbonus()}").pack()
        ttk.Label(frame, text=f"CHA: {self.abilities.charisma} - {self.getCHAbonus()}").pack()

        return frame

    def showSpeed(self, window):
        for s in self.speed:
            if isinstance(s, walk):
                ttk.Label(window, text=f"walk speed: {s.value}")

@dataclass
class monster(creature):
    type: str
    subtype: str
    cr: float
    xp: int
