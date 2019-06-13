#this is the version that allows the fizz and buzz to be changed
#
# fizz = 3
# buzz = 5
# n = 1
# while n < 100:
#     print('Counter is ' + str(n))
#
#     if n % (fizz * buzz) == 0:
#         print('FIZZBUZZ')
#     else:
#         if n % fizz == 0:
#             print('FIZZ')
#         if n % buzz == 0:
#             print('BUZZ')
#     n = n + 1
#     print(' ')

#Test
#Test2
#Test3
#Test4
#Test6
#Test7
#Test8
#this is the more concise version

for n in range (1,101):
    print(n)
    if n % (3 * 5) == 0:
        print('FIZZBUZZ')
    else:
        if n % 3 == 0:
            print('FIZZ')
        if n % 5 == 0:
            print('BUZZ')
    n = n + 1
    print(' ')