import random

classes = [[],[]]

names = [
    'a','b','c','d','e',
    'f','g','h','i','j',
    'k','l','m','n','o',
    'p','q','r','s','t',
    'u','v','w','x','y',
    'z','1','2','3','4',
    '5','6','7','8','9'
]

for name in names:
    index = random.randint(0,1)
    classes[index].append(name)

i = 1
for tempNames in classes:
    print('班级%d的人数为：%d' % (i,len(tempNames)))
    i += 1
    for name in tempNames:
        print('%s' % name,end=' ')
    print('\n')
    print('-'*20)