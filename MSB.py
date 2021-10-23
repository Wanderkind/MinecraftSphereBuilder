
R = int(input('\nRadius = '))
F = int(input('Floor = '))
X = int(input('Center X coordinate = '))
Z = int(input('Center Z coordinate = '))

Count = 0
for J in range(2*R + 1):
    j = J - R
    
    coord = []
    for I in range(2*R + 1):
        i = I - R
        
        for K in range(2*R + 1):
            k = K - R
            
            if R - 0.5 < (i**2 + j**2 + k**2)**(1/2) < R + 0.5:
                P = [i + X, j + R + F + 1, k + Z]
                coord.append(P)
    
    L = len(coord)
    print(coord)
    print('Blocks required for Y =', j, ':', L, '\n')
    
    Count = Count + L

print('Total blocks required :', Count, '\n')
