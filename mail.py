mass = [input()[:-12] for _ in range(int(input()))]
mass2 = [input() for _ in range(int(input()))]
for i in mass2:
    flag = 0
    mass3 = []
    k = 0
    for j in mass:
        if i == j:
            mass3.append("0")
        if i == j[:len(i)] and i != j:
            mass3.append(j[len(i):])

    while True:
        if str(k) not in mass3:
            flag = k
            break
        k += 1       
    mass.append(f'{i}{"" if flag==0 else flag}')
    print(f'{i}{"" if flag==0 else flag}@beegeek.bzz')