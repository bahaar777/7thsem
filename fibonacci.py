n_terms = int(input("Enter the no. of terms you want: "))
n1,n2 = 0,1
count=0
if n_terms<=0:
    print("Invalid input")
elif n_terms == 1:
    print("Fibonacci Sequence: ")
    print(n1)
else:
    print("Fibonacci Sequence: ")
    while count<n_terms:
        print(n1)
        nth = n1+n2
        n1=n2
        n2 = nth
        count+=1
print("step count ",count)
