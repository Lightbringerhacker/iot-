def distri(a,b,c):
    left= a*(b + c)
    right= (a*b)+(a*c)
    if(left==right):
        print("a(b+c)=ab+ac")
        print("Distributive law proved(for Addition)")
    else:
        print("Distributive law Not proved")

    print("\n")
    
    le= a*(b-c)
    ri= (a*b)-(a*c)
    if(le==ri):
        print("a(b-c)=ab-ac")
        print("Distributive law proved(for Subtraction)")
    else:
        print("Distributive law Not proved")
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
distri(a,b,c)

