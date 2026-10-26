# i = 1
# print(f"2 x {i} = {2*i}")

# i = 2
# print("2 x 2 = 4")

# i = 3
# print("2 x 3 = 6")

# i = 4
# print("2 x 4 = 8")

for dan in range(2,5):
    for i in range(1,5):
        print(f"{dan} x {i} = {dan*i}", end="\t")
    print("\n================================")

print("\n") 

for dan in range(1,5):
    for i in range(2,10):
        print(f"{i} x {dan} = {dan*i}", end="\t")
    print("\n")


'''
2 x 1 = 2  3 x 1 = 3  4 x 1 = 4
2 x 2 = 4  3 x 2 = 6  4 x 2 = 8
2 x 3 = 6  3 x 3 = 9  4 x 3 = 12
'''