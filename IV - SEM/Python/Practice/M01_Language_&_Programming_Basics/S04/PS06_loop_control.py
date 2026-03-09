p1="abc123"
for i in range(3):
    p2=input()
    if p2==p1:
        print("Login successful")
        break
    else:
        print("Account locked")