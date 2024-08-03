
def split_tuple(d):
  list_ = []
  for i in d:
    list_.append(i)
  return list_



d = ((), [{(2, 'Urban', ('Urban2', 35))}])


list_str=[]
list_num=[]

for i in d:
  for j in i:
    if type(j) is tuple:
      b = split_tuple(j)
    if type(j) is str:
      list_str.append(i)
    if type(j) is int:
      list_num.append(i)
    else:
      split_tuple(i)
print(list_str)
print(list_num)






#






# # test_list = [{(2, 'Urban', ('Urban2', 35))}]
# test_list=[(), ({(2, 'Urban', ('Urban2', 35))},)]
# res = []
# for i in test_list:
#     x = []
#     for j in i:
#         if type(j) is tuple:
#             x.extend(list(j))
#         else:
#             x.append(j)
#     res.append(tuple(x))
#
# # printing result
# print("The unpacked nested tuple list is : " + str(res))
























