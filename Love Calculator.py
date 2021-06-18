#Am writing a code that checks the compactibility of two people in love
print("Welcome to your love calculator find out if you are compatible with your crush")
name=input("Enter your name: ")
crush=input("Enter your crush name: ")
name=name.lower()
crush=crush.lower()
T= name.count('t') + crush.count('t')
R= name.count('r') + crush.count('r')
U= name.count('u') + crush.count('u')
E= name.count('e') + crush.count('e')
L= name.count('l') + crush.count('l')
O= name.count('o') + crush.count('o')
V= name.count('v') + crush.count('v')
E= name.count('e') + crush.count('e')
first=str(T+R+U+E)
second=str(L+O+V+E)
score=int(first+second)
print(f"you compatibility is {score}")
if score<10 or score>90:
    print(f"Your love score is {score}, and you go like coke and mentos")
elif score>=40 and score<=50:
    print(f"your love score is {score}, you are alright together")
else:
    print(f"your love score is {score}")