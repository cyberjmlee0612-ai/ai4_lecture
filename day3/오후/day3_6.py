# def calc_order_legacy(u_type, price, qty, coupon):
#     total = price * qty
#     if u_type == 1:
#         total = total * 0.95
#     elif u_type == 2:
#         total = total * 0.90
#     elif u_type == 3:
#         total = total * 0.80
#     if coupon == "YES":
#         total = total - 3000
#     if total < 0:
#         total = 0
#     return int(total),


# result = calc_order_legacy(1,100,20,"yes")

# def preprocess_legacy(data):
#     res = []
#     for row in data:
#         score = float(row["score"])
#         res.append(round(score / 100.0, 4))
#     return res

# data = [
#     {"score": 80},
#     {"score": 50},
#     {"score": 100}
# ]

# result = preprocess_legacy(data)


# print(result)