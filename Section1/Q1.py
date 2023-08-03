text = ['  + -- + - + -     ',
        ' + --- + - +     ',
        '   + -- + - + -    ',
        '  + - + - + - +    ', ]

for i in text:
    print(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'))

# 십진법으로 바꾸기
for i in text:
    print(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2))

# 문자로 바꾸기
for i in text:
    print(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))

#한 배열로 넣기
l=[]
for i in text:
    l.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))
    print(l)

#배열 한 단어로
print(''.join(l))

print(''.join([chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for i in text]))

# 다른 방법
s = [i.strip().replace(' ', '').replace('+', '1').replace('-', '0') for i in text]
print(s)

# map(function,s)
print(list(map(lambda x:chr(int(x,2)),s)))

#''빼고 문자열 합치기
def f(x):
    return chr(int(x,2))
print(''.join(list(map(f,s))))

print('011011011'.replace('0','!'))
print('011011011'.replace('0','!').replace('!','+'))
print('011011011'.replace('0','!').replace('!','+').replace('+','~'))
print('111'.zfill(10))

# 배열
# [for a in range(10): a]
# [a for in range(10)]
# 위 두 결과 다 => [0,1,2,3,4,5,6,7,8,9]
#
# 짝수만
# [a for in range(10) if a % 2==0]
# => [0,2,4,6,8]
# print('배열:' + str(d))

# 구구단
# [f '{b]x{c}={b*c}' for b in range(2,10) for c in range(1,10)]


# gugudan [f'{b}x{c}={b*c}' for b in range(2, 10) for c in range(1, 10)]


