@smoke
a = "hi"
b = "worldunion"
a = a + b
print(a)
b = a[:len(a) - len(b)]
print(b)
a = a[len(b):]
print(a)
print(b)
from os.path import split

# l = [1,2,3]
# cl = []
# # for i in l:
#     cl.append(i)
# print(cl)
# for i in l:
#     cl += [i]
# print(cl)
#
d = {1:'a', 2:'b', 3:'c', 4:'d'}
rd = {}
# for k,v in d.items():
#     if v in rd:
#         rd[v].append(k)
#     else:
#         rd[v] = [k]
# for k,v in d.items():
#     rd[v] = [k]
# print(rd)
# json = json.dumps(d)
# print(json)
# a = "python programs"
# b = reverse(a)
# #print(a[::-1])
# print(b)
# c = "".join(reversed(a))
#5)occurance of each string in the string list
# arr = ['haritha', 'python', 'code', 'program', 'code']
# dict = {}
# for str in arr:
#     if str in dict:
#         dict[str] += 1
#     else:
#         dict[str] = 1
# print(dict)
# a = "python programing"
# print(a)
# b = a.split()
# print(b)
# c = "".join(b)
# print(c)
# d = "".join(reversed(b))
# print(d)
# f = d.split()
# print(f)
# # count = 0
# e = {}
# for i in c:
#     if i in e:
#         e[i] += 1
#     else:
#         e[i] = 1
# print(e)
#l = [1,2,3,4,5,1,2,3,2,2,3,8,9]
# out = {}
# for i in l:
#     if i in out:
#         out[i] += 1
#     else:
#         out[i] = 1
# print(out)
# char = 2
# count = 0
# for i in l:
#     if  i == char:
#         count += 1
# print(count)
# lst = [1,2,3]
# lst.insert(1, 4)
# print(lst)
str1 = "hello"
str2 = "world"
#swap = str1.swapcase()
# swap = str1
# str1 = str2
# str2 = swap
# print(str1, str2)
# str1,str2 = str2,str1
# print(str1)
# print(str2)
dic = {
    "health": [
        {"id": 1, "name": "haritha", "des": "eye"},
        {"id": 2, "name": "har", "des": "ear"}
    ],
    "company": [
        {"id": 1, "name": "haritha", "des": "developer"},
        {"id": 2, "name": "kiran", "des": "tester"}
    ],
    "technology": [
        {"id": 1, "name": "python", "des": "language"},
        {"id": 2, "name": "selenium", "des": "automation"}
    ]
}
# Print all categories
print("Categories:", list(dic.keys()))

# Print all health records
# print("\nHealth records:")
# for item in dic["health"]:
#     print(item)










