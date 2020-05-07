Uniprot = ['c', 'b', 'a', 'd']

test = ['a', 'b']
"""
for t in test:

    if t in Uniprot:
        print(Uniprot.index(t))

"""

n = 2

result = [Uniprot[i * n:(i + 1) * n] for i in range((len(Uniprot) + n - 1) // n )]

#print(result)


for ai in range(0, len(result)):

    Temp = result[ai]


print(type(Temp))
print(Temp)
