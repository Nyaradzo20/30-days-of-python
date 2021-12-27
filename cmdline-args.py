import sys
a = len(sys.argv)
if a == 1:
    print("{} argument :".format(a))
elif a  > 1 :
    print("{} arguments :".format(a))   
else:
    print("{} arguments".format(a))
print("sure sure ")