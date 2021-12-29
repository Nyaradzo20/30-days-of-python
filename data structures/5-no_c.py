def no_c(my_string):
    value = "C" or "c"
    if value in my_string:
        my_string.pop(value)
        print(my_string )