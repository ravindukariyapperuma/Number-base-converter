n = int(input('Enter an intiger number : '))
st = ""
while n!=0:
    q=n//2
    r=n%2
    n=q
    st=str(r)+st
print('Binary value is : '+ st)
