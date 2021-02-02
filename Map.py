from Settings import *

MAP = [
    "WWWWWWWWWW",
    "WW.......W",
    "W.WW.....W",
    "W.....W..W",
    "W...W.W..W",
    "W..W.....W",
    "W........W",
    "WWWWWWWWWW", ]
GAMEMAP = set()
for RowINDX, row in enumerate(MAP):
    for Index, char in enumerate(row):
        if char == "W":
            GAMEMAP.add((Index * TILE, RowINDX * TILE))
