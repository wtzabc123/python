li = [100, 'Conan', True, [1, 2, 3]]

# 索引
print(li[0], type(li[0]))
print(li[1], type(li[1]))
print(li[-1])

# 切片  (顾头不顾尾)
print(li[1: 3])
print(li[: 2])


# 练习题
li = [1, 3, 2, "a", 4, "b", 5, "c"]
# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
l1 = li[: 3]
print(l1)

# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
l2 = li[3: -2]
print(l2)

# 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
l4 = li[1: -2: 2]
print(l4)

# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
l6 = li[-3: 0: -2]
print(l6)




