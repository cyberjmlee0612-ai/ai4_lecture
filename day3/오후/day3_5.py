names = ['홍길동','이순신','강감찬']

# id = 1
# for name in names:
#     print (f'{id}.{name}')

#     id += 1

# for id,name in enumerate(names,start=1):
#     print(id,name)



test_str = ["epoch=1,loss=0.45,acc=88.5"]
for line in test_str:
    result = dict(item.split("=") for item in line.split(","))
    print(result)
    parts = dict(item.split("=") for item in line.split(","))
    try:
        record = {
            "epoch": int(parts["epoch"]),
            "loss": float(parts["loss"]),
            "acc": float(parts["acc"]),
        }
        print(record)
    except Exception as e:
        print (e)


# # print(test_str.split(','))
# #int('abc)  valuError
# dict_1 = {}
# #dictt_1['abc']

''