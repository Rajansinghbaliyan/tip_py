# Write your tip function here:
def tip(total,percentage):
    tip1=total*(percentage*.01)
    total +=tip1
    return tip1
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
