from cmath import sqrt

print("Algorithme de resolution d'equation de second degré")
print("Soit ax2 + bx + c = 0")
a=int(input("Entrer l'entier a : "))
b=int(input("Entrer l'entier b : "))
c=int(input("Entrer l'entier c : "))
if a == 0 :
    print("Nous avons une seule solution")
    print(a,"x2 +",b,"x +",c)
    x = -c/b
    print("x = ",-c,"/",b," = ",x)
elif a != 0 :
    print("Nous avons l'equation :",a,"x2 +",b,"x +",c)
    print("calcul de delta = b*b - 4*a*c:")
    delta = b*b - 4*a*c
    print("delta = ",b*b - (4*a*c))
    if delta == 0 :
        print("nous avons une solution x1 = x2 = -b/2a")
        print("x = ",-b / (2*a))
    elif delta >= 0 :
        print("nous avons deux solutions x1 et x2")
        x1 = -b + sqrt(delta)/2*a
        x2 = -b - sqrt(delta)/2*a
        print("x1 = ",-b,"+",sqrt(delta),"/2 *",a)
        print("x2 = ",-b, "-",-sqrt(delta),"/2 *",a)
        print("x1 = ", x1)
        print("x2 = ", x2)







