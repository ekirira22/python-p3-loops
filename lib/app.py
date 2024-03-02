import ipdb

# Fibonacci Sequence


# def fibonacci_refactored_print(n):
#     empty_li = []
#     for i in range(0, n):
#         if i == 0:
#             empty_li.append(i)
#         else:
#             num1 = empty_li[i-1]
#             num2 = i
#             num_to_add = num1 + num2
#             empty_li.append(num_to_add)
#             print(empty_li)
#     print(empty_li)
#     print('This the fibonacci sequence for the number you put in')
#     return empty_li

capitals = {
    "USA": "Washington D.C",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
    "Africa": {
        "Kenya": "Nairobi",
        "Uganda": "Kampala"
    }
}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# capitals.update({"Germany": "Berlin"})
# keys = capitals.keys()


# for key, value in capitals.items():
#     if isinstance(value, dict):
#         for k, v in value.items():
#             print(f"My Object within is {k}: {v}")
#     else:
#         print(f"{key}: {value}")
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# //Multiply by 7920 and store in a new initiated list

new_heights = [height * 7920 for height in player_heights]
for height in new_heights:
    below_avg = "not qualified" if height < 70 else "Qualified"
    print(below_avg)
