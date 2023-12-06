
with open("input.txt") as f:
    ans = 0
    lines = f.read().split("\n")
    k = len(lines)
    cards = [1 for _ in range(k)]
    for i, line in enumerate(lines):
        a = line.split(":")[1]
        b = a.split("|")
        c = set(b[0].split(" "))
        d = set(b[1].split(" "))
        c.remove('')
        d.remove('')
        e = d & c
        l = len(e)
        for n in range(l):
            cards[i + 1 + n] += cards[i]
    print(cards)
    print(sum(cards))