
with open("input.txt") as f:
    arr = []
    for line in f.read().split("\n"):
        arr.append(list(line))
    print(arr)
    n = len(arr)
    m = len(arr[0])
    def checkSymbol(i, j, arr):
        n = len(arr)
        m = len(arr[0])
        return 0 <= i and i < n and 0 <= j and j < m and (not arr[i][j].isdigit()) and arr[i][j] != '.' 
    ans = 0
    gears = {}
    for i in range(n):
        d = 0

        gearsList = []
        for j in range(m):
            c = arr[i][j]    
            if c.isdigit():
                d = d * 10 + int(c)
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if checkSymbol(i + a, j + b, arr) and arr[i + a][j + b] == '*':
                            gearsList.append((i + a, j + b))
            else:
        
                if gearsList:
                    print(d, gearsList)
                    for gear in set(gearsList):
                        gears.setdefault(gear, list()).append(d)
                gearsList = []
                d = 0
        if gearsList:
            for gear in set(gearsList):
                gears.setdefault(gear, list()).append(d)
        gearsList = []
        d = 0
    for g, l in gears.items():
        print(g, l)
        if len(l) == 2:
            ans += l[0] * l[1]
    print(ans)