#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) # this will print 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) # will print error number of days in a week silicon or triangle sides and 5 military branches not defined


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) # will print 5 because stops at first return statement.


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) # will print 5 because stops at first return statement.


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x) #will print 5 and null.


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3)) # will print 3, 5


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) # will print 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b) #will print 100
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) # will print 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # will print 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # will print 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # will print 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) # will print 8


#11
b = 500
print(b) # will print 500
def foobar():
    b = 300
    print(b) # will print 500
print(b) # will print 300
foobar()
print(b) # will print 500


#12
b = 500
print(b) # will print 500
def foobar():
    b = 300
    print(b) #will print 500
    return b
print(b) # will print 300
foobar()
print(b) # will print 500


#13
b = 500
print(b) # will print 500
def foobar():
    b = 300
    print(b) # will print 500
    return b
print(b) # will print 300
b=foobar()
print(b) # will print 300


#14
def foo():
    print(1) #will print 1
    bar()
    print(2) #will print 2
def bar():
    print(3) #will print 3
foo()


#15
def foo():
    print(1) #will print 1
    x = bar()
    print(x) #will print 10
    return 10
def bar():
    print(3) #will print 3
    return 5
y = foo()
print(y) #will print 5