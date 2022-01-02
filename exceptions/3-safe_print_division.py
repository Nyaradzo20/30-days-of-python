def safe_print_division(a, b):
    d = 0
    try:
        d = a / b
        print("{}".format(d))
    except ZeroDivisionError:
        print()
    finally:
        print("Inside result: {}".format(d))
        