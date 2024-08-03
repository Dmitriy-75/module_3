calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    leng_string = int(len(string))
    string_ap = str.upper(string)
    string_lw = str.lower(string)
    str_info = leng_string, string_ap, string_lw
    return str_info
def is_contains(string, list_to_search):
    count_calls()
    is_c = str.lower(string) in list(map(str.lower, list_to_search))
    return is_c

print(string_info("Телевизор"),"- число букв в слове, слово с верхним и нижнем регистром букв")
print(string_info("education"),"-  --//--//--//--//--//--")
print(is_contains("ПривеТ",["приВет","пока","досвидоC"])," -     наличие  слова - ПривеТ -  в списке")
print(is_contains("PoWer",["strong","power","diamond"])," -     наличие  слова - PoWer-   в списке")
print(calls," -        количество обращений к функциям")




