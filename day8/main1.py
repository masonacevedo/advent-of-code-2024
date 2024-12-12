import sys
import copy
import pprint
import math
from enum import Enum

def downPossibility(pair):
	pass

def upAndRightDiagonal(pair):
	pass

def inGrid(grid, coords):
	row, col = coords 
	return (0 <= row <= len(grid)) and (0 <= col <= len(grid[0]))

def antinodesFromVertical(grid, y1, y2, xCoord):
	deltaY = math.abs(y1-y2)
	topPossibility = [math.max(y1, y2) + deltaY, xCoord]
	bottomPossibility = [math.min(y1, y2) - deltaY, xCoord]
	ans = []
	ans.append(topPossibility) if inGrid(grid, topPossibility) else None
	ans.append(bottomPossibility) if inGrid(grid, bottomPossibility) else None
	return ans

def antinodesFromHorizontal(grid, x1, x2, yCoord):
	deltaX = math.abs(x1-x2)
	leftPossibility = [yCoord, math.max(x1, x2) + deltaX]
	rightPossibility = [yCoord, math.min(x1, x2) - deltaX]
	ans = []
	ans.append(leftPossibility) if inGrid(grid, leftPossibility) else None
	ans.append(rightPossibility) if inGrid(grid, rightPossibility) else None
	return ans

def antinodeFromPair(grid, pair):
	loc1, loc2 = pair
	y1, x1 = loc1
	y2, x2 = loc2
	
	if x1 == x2:
		return antinodesFromVertical(grid, y1, y2, x1)
	if y1 == y2:
		return antinodesFromHorizontal(grid, x1, x2, y1)
	
	deltaX = math.abs(x1-x2)
	deltaY = math.abs(y1-y2)
	
	rightPossibility = math.max(x1,x2) + deltaX
	leftPossibility = math.min(x1,x2) - deltaX
	
	upPossibility = math.min(y1,y2) - deltaY
	downPossibility = math.max(y1,y2) + deltaY
	
	if upAndRightDiagonal(pair):
		possibleNodes = pass
	elif downAndRightDiagonal(pair):
		possibleNodes = pass
	else:
		raise Exception("shouldn't be possible to get here")
	
def getPairs(locationsMap):
	pairsMap = {}
	for key in locationsMap.keys():
		locs = locationsMap.get(key)
		pairsMap[key] = [[loc1, loc2] for loc1, loc2 in zip(locs[0:-1], locs[1:])]
	print("pairsMap")
	pprint.pprint(pairsMap)
	return pairsMap
		

def getLocationsMap(grid):
	locationsMap = {}
	for rowIndex, row in enumerate(grid):
		for colIndex, item in enumerate(row):
			if item != ".":
				locationsMap.setdefault(item, []).append([rowIndex, colIndex])
	return locationsMap

def main(file_name):
	with open(file_name) as file_handle:
		lines = file_handle.readlines()
	grid = [list(line.replace("\n","")) for line in lines]
	pprint.pprint(grid)
	locationsMap = getLocationsMap(grid)
	pairs = getPairs(locationsMap)
		
	

if __name__ == "__main__":
	print(main(sys.argv[1]))
