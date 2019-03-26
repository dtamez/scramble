#! /usr/bin/env python
# -*- coding: utf-8 -*-
class Tile:
    """
    Rerpresents one scramble squares puzzle piece.
    The id is an arbitrary way of labeling each piece.
    north, south, east, and west represent the values at each side of the square.
    rotation is the number of clockwise turns the piece has been through in a given solution.
    """

    def __init__(self, id, north, east, south, west, rotation=0):
        self.id = id
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.rotation = rotation

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        self.north, self.east, self.south, self.west = self.west, self.north, self.east, self.south

    def __repr__(self):
        return f'<Tile(id: {self.id}, n: {self.north} e: {self.east} s: {self.south} w: {self.west} rot: {self.rotation})>'


def is_valid(tiles):
    """
    Check that the tile being placed correctly fits with the other tiles.
    Only validate the last piece as previous pieces are already valid.
    """
    current = len(tiles)
    if current < 2:
        return True
    elif current == 2:
        return tiles[0].east + tiles[1].west == 10
    elif current == 3:
        return tiles[1].east + tiles[2].west == 10
    elif current == 4:
        return tiles[0].south + tiles[3].north == 10
    elif current == 5:
        return tiles[3].east + tiles[4].west == 10 and tiles[4].north + tiles[1].south == 10
    elif current == 6:
        return (
            tiles[4].north + tiles[1].south == 10 and
            tiles[4].east + tiles[5].west == 10 and
            tiles[5].north + tiles[2].south == 10
        )
    elif current == 7:
        return tiles[3].south + tiles[6].north == 10
    elif current == 8:
        return (
            tiles[6].east + tiles[7].west == 10 and
            tiles[7].north + tiles[4].south == 10
        )
    elif current == 9:
        return (
            tiles[7].east + tiles[8].west == 10 and
            tiles[8].north + tiles[5].south == 10
        )

def solve(placed, left):
    valid = is_valid(placed)
    if valid and not left:
        # last tile is valid and no tiles left - solution found
        print(f'solved: {placed}')
        return True
    elif valid:
        # last tile is valid but we're not done
        for tile in left:
            for _ in range(4):
                tile.rotate()
                placed2 = placed[:]
                placed2.append(tile)
                left2 = left[:]
                left2.remove(tile)
                if solve(placed2, left2):
                    break

    else:
        # tile is not properly placed so don't recurse
        return False


def main():
    t1 = Tile('A', 6, 7, 1, 8)
    t2 = Tile('B', 7, 8, 3, 4)
    t3 = Tile('C', 3, 9, 2, 9)
    t4 = Tile('D', 7, 1, 4, 8)
    t5 = Tile('E', 4, 8, 1, 6)
    t6 = Tile('F', 6, 9, 3, 2)
    t7 = Tile('G', 2, 3, 9, 4)
    t8 = Tile('H', 1, 7, 8, 6)
    t9 = Tile('I', 6, 3, 8, 9)
    tiles = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
    solve([], tiles)


if __name__ == "__main__":
    main()
