def superftoc(f):
    return (5/9) * (f - 32)

f = int(input("Enter the number: "))
c = superftoc(f)
print ("{0} centigrade".format(c))