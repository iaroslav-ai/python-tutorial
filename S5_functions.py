# example function definition
def fnc(a, b=None):
    if not b is None:
        return a+b
    else:
        return a, "you passed none"

result = fnc(1,1)
print result

result, message = fnc(1)
print result, message

print fnc(a=1, b=2)