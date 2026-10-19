# ZIP
# 리스트 컴프리헨션
'''
result = []

list_1 = [1,2,3,4,5]

# for i in list_1:
#     if i % 2 == 0:
#         result.append(1)

result = [ int(i) for i in list_1 ]

print(result)

menu - ['아메리카노','라떼','초코']
ice_menu = ['아이스'+i for i in menu]
len_,enu = [len(i) for i in menu if len(i)%2==0]


print(len_menu)

# ['참' if 조건 else '거짓' for i in 집합]
# ['참' for i in 집합 if 조건]
'''

'''
ages = [20,15,60,25,30,45,5]
print( [ i for i in ages if i>=20 ] )
print( [ '성인' if i>=20 else '미성년' for i in ages ] )

# print( set([1,2,3,4,5,6,7,8,1,2,3,4,5]) )
'''

bad_words = ['바보','멍충이','멍텅구리','','멍충이']
words = sorted(set(word for word in bad_words if word), key=len, reverse=True)
print(words)

import re
print( [re.escape(word) for word in words])
print( type( "ㅣ".join(words)))
