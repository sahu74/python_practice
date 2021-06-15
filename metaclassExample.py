class Demo:
    pass

# It prins <class '__main__.Demo'>
print(Demo)

obj= Demo()

# It prins <class '__main__.Demo'>
print(obj.__class__)

# It prins <class '__main__.Demo'>
print(type(obj))

#for t in int, float, dict, list, tuple:
#    print(t)


print(type(['foo', 'bar', 'baz']))