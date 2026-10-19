# import random
# ages = random.sample(range(15,100), 10)
# results = []
# for i in ages:
#         if i>=20:
#                 results.append('성인')
#         else:
#                 results.append('미성년자')

# print(results)

# 리스에서 불량을 모두 지우고 정상만 남게
items = ['정상','불량','불량','정상']
# target = items[:] #복사

# for item in target :
#     if item == '불량':
#         items.remove('불량')

# [ for item in items if item != '불량']
result = []
for item in items:
    if item != '불량':
        result.append(item)

print(f'검수결과 : {items}')

