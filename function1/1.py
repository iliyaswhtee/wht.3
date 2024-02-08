def grams_to_ounces(x):
    return 28.3495231 * x
grams = int(input("Enter the number: "))
ounces = grams_to_ounces(grams)
print (ounces)