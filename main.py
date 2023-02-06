import random

def random_bom(rows: int, cols: int, bom_number: int) -> list:
    field = [[0] * cols for i in range(rows)]
    countbomb = min(bom_number, rows*cols)
    BomPositionList = []
    
    while countbomb:
        BomPosition = random.randint(0,rows-1),random.randint(0,cols-1)
        if BomPosition not in BomPositionList:
            BomPositionList.append(BomPosition)
            countbomb -= 1
    for i in range(rows):
        for j in range(cols):
            if (i,j) in BomPositionList:
                field[i][j] -= 1
    return field

if __name__ == "__main__":
    mine = random_bom(5, 5, 5)
    for box in mine:
        print(box)