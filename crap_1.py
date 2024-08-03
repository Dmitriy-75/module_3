

def count_(m):
    list_str=[]
    list_int=[]
    for i in m:

        if isinstance(i, tuple):
            m=i
            t = count_(m)
            print(m,type(m),t)

        if isinstance(i, int):
            int_ = i
            print(i, type(i), int_)


        if isinstance(i, str):
           print(i , type(i),len(i))



        if isinstance(i, list):
            for j in i:
                if type(j) is str:
                    list_str.append(j)
                if type(j) is int:
                    list_int.append(j)
                sum_list_str=len("".join(list_str))
                sum_list_int=sum(list_int)
            sum_list_str = len("".join(list_str))
            sum_list_int = sum(list_int)
            print(i,type(i),((sum_list_int)+(sum_list_str)))






        if isinstance(i, dict):
           keys_len = len("".join(list(i)))
           value_sum=sum(i.values())
           dict_sum =keys_len+value_sum
           print(i,type(i),dict_sum)



data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
  ]


a = count_(data_structure)















