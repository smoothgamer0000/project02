import pygame as pg

def from_sprite_sheet(start, size, col, row, sprite_sheet):
    frames = []
    for j in range(row):
        for i in range(col):
            location = (start[0] + size[0] * i, start[1] + size[1] * j)
            frames.append(sprite_sheet.subsurface(pg.Rect(location, size)))
    return frames


def strip_objects(file_name, objects):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    x, y, width, height = 0, 0, 0, 0
    for line in lines:
        numbers = line.split()
        if x == 0 and y == 0:
            x = int(numbers[0]) * 2
            y = int(numbers[1]) * 2
            width, height = 0, 0
        elif width == 0 and height == 0:
            width = int(numbers[0]) * 2 - x
            height = int(numbers[1]) * 2 - y
            objects.append(pg.Rect(x, y, width, height))
            x, y = 0, 0
