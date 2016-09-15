# Exercise 1
x = 10
def f(x):
    ans = x**2 + 10  #Squaring input then adding 10
    return ans       #Returning computed value

f(10) #100 + 10 = 110

#Exercise 2
def swapping(x):
    if(not (len(x) == 1)):
        #temp = x[0] #Storing the data
        #x[0] = x[1]
        #x[1] = temp
        x[0], x[1] = x[1], x[0] #Shortcut
        return x    #Return the data
    return x

print(swapping([2, 3, 5]))

#Exercise 3
def temperature(x):
    if x > 86:            #check 86
        return 'hot'
    elif x > 32:          #check 32
        return 'cool'
    else:                 #check the last
        return 'freezing'

print(temperature(35))
print(temperature(98))
print(temperature(3))

#Exercise 4
def BMI(weight, height):
    bmi = weight * 703 / (height ** 2)
    if bmi > 25:
        return 'Overweight'
    elif bmi < 18.5:
        return 'Underweight'
    else:
        return 'Normal'

print(BMI(190, 75))
print(BMI(140, 75))
print(BMI(240, 75))

#Exercise 5
def divisors(x):
    ls =[]
    for i in range(2, x + 1):
        if x % i == 0:
          ls.append(i)
    return ls

print(divisors(6))

#Exercise 6
def hyp(x, y):
    return (x**2 + y**2)**0.5

print(hyp(3, 4))

#Exercise 7
def listing(coursename, location):
    for a,b in zip(coursename, location):
        print(a + '\t' + b)

listing(['java', 'python', 'c++'], ['LH001', 'LH002', 'LH003'])
