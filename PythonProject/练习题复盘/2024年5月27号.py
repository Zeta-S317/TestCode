"""
test = 0
for i in range(1, 101):
    test += i
print(test)
# Range只到100-1,需要多加记忆，

# """

"""
count = 0
result = 0
while count < 100:   #  应该是小于,而不是等于，不然会多出1
    count += 1
    print(count)
    result += count
print(result)
"""

"""
items = [0,1,2,3,4,5,6]
print(items[2:4])
list = []
for i in range(2,4):
    list.append(items[i])
print(list)
list2 = []
for i in items:
    if i >= 2 and i <=4:
        list2.append(i)
print(list2)

# range应该是2,5，现在只选取到了[2,3]
# 切片是从x开始，然后到y-1结束，所以2:4只取了[2,3]
"""

"""
nums = [1, 3, 5, 7, 9]
max_value = max(nums)
min_value = min(nums)

mean_values = sum(nums) / (len(nums))
print(mean_values)
"""

"""


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

max_v = max(prices.values())
min_v = min(prices.values())

mean_value = sum(prices.values()) / len(prices)
print(mean_value) 之前的代码无法选取到最小值，因为写法有问题
"""

"""
nums = [1, 4, -5, 10, -7, 'N/A', 3, -1]

for i in nums:
    if type(i) is int and i < 0:
        print(i)
        # 判断是否小于0且不是非int的数据
"""

"""
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not',
         'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you\'re",
         'under']

test = {}

for i in words:
    if i in test:
        test[i] += 1
    else:
        test[i] = 1

Top_three = []
test = sorted(test.items(), key=lambda x: x[1], reverse=True)
for i in test[0:3]:
    # for k in i:
    #     if type(k) is str:
    #         Top_three.append(k)

print(Top_three)

# 取出前三个最高的值
"""


"""
def test(n):
    if n == 0:
        return 1
    else:
        return n * test(n-1)


result = test(100)
print(result)
"""


# class Test:
#
#     def __init__(self, file_name, file_model):
#         self.file_name = file_name
#         self.file_model = file_model
#
#
#     def __enter__(self):
#         print("进入上文方法")
#         # 返回文件资源
#         self.file = open(self.file_name, self.file_model)
#         return self.file
#
#     # 下文方法
#     def __exit__(self, exc_type, exc_val, exc_tb):  # 里面参数是固定的，会自动生成
#         print("进入下文方法")
#         self.file.close()
#
#
# if __name__ == '__main__':
#     with Test("1.txt", "r") as file:
#         file_data = file.read()
#         print(file_data)
