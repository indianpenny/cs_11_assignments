import math 

a = int(input("Coefficient on the cubic term "))
b = int(input("Coefficient on the quadratic term "))
c = int(input("Coefficient on the linear term "))
d = int(input("Constant term "))

def displayNum(n):
    if n>0:
        return " + "+str(n)
    else:
        return " - "+str(abs(n))
      
print("Your cubic polynomial was y =", a ,"x³",displayNum(b),"x²",displayNum(c),"x", displayNum(d))

#a *= x**3
#b *= x**2
#c *= x

factor_list = []
sums = []
new_factor_list = []


def factor(a,b,c,d):
    if d < 0:
        d *= -1
    for i in range(1, d+1):
        if d % i == 0:
            factor_list.append(i)
            
factor(a,b,c,d)

for j in range(len(factor_list)):
    n = factor_list[j] * -1
    factor_list.append(n)
print("The factors of the constant term are", factor_list)

for r in range(len(factor_list)):
  sum = a*(factor_list[r])**3 + b*(factor_list[r])**2 + c*(factor_list[r]) + d
  sums.append(sum)
  if sums[r] == 0:
    index_val = sums.index(0)
    print("So far we found one solution at x = " + str(float(factor_list[r])))
    break
if sums[-1] != 0:
  print ("Sorry, it seems like your polynomial is not factorable using this method.")


divisor = factor_list[index_val]*-1

def synthetic_div(a,b,c,d):
    global new_factor_list, a2, b2, c2
    divisor = factor_list[index_val]
    a2 = a
    new_factor_list.append(a2)
    b2 = (a2*divisor)+b
    new_factor_list.append(b2)
    c2 = (b2*divisor)+c 
    new_factor_list.append(c2)
    
synthetic_div(a,b,c,d)

if b2 == 0:
  print("After synthetic division, it looks like your cubic is the product of ("+str(a2)+"x²"+str(displayNum(c2))+")(x"+str(displayNum(divisor))+")")

  
else:
  print("After synthetic division, it looks like your cubic is the product of ("+str(a2)+"x²"+str(displayNum(b2))+"x"+str(displayNum(c2))+")(x"+str(displayNum(divisor))+")")

def poly_factored(a2, b2, c2):
  global sol1Numerator, sol1Denominator, sol2Denominator, sol2Numerator
  a2temp = a2
  b2temp = b2
  c2temp = c2
  
  if a2 < 0:
    a2 *= -1
  if b2 < 0:
    b2 *= -1
  if c2 < 0:
    c2 *= -1
    
  gcd = math.gcd(a2, b2, c2)

  #print(a2, "x²"+displayNum(b2),"x", displayNum(c2),"has a gcf of",gcd)


  if b2temp == 0 and c2temp <0:
    print("Your cubic factored into (" + str(a2temp) + "x²" + str(displayNum(c2temp)) + ")(x" + str(displayNum(divisor))+")")
    print("and the solutions to your cubic are x = "+ str(float((factor_list[r]))) + " and x = ∓ √(" + str((-1*c2temp)) +")")

  else:
    try:
      new_a = a2temp / gcd
      new_b = b2temp / gcd
      new_c = c2temp / gcd
      
      sol1Numerator=int(-new_b+(new_b**2-4*new_a*new_c)**(1/2))
      sol2Numerator=int(-new_b-(new_b**2-4*new_a*new_c)**(1/2))
      denom=int(2*new_a)
      sol1Gcd=math.gcd(sol1Numerator,denom)
      sol2Gcd=math.gcd(sol2Numerator,denom)
      sol1Numerator=-sol1Numerator/sol1Gcd
      sol1Denominator=denom/sol1Gcd
      sol2Numerator=-sol2Numerator/sol2Gcd
      sol2Denominator=denom/sol2Gcd 
  
            
      print("Your cubic factored nicely to", str(int(gcd*a2/abs(a2)))+"("+str(int(sol1Denominator))+"x"+displayNum((int(sol1Numerator)))+")("+str(int(sol2Denominator))+"x"+displayNum(int(sol2Numerator))+")(x"+displayNum(divisor)+")")
  
      solution1 = sol1Numerator * -1 / sol1Denominator
      solution2 = sol2Denominator * -1 / sol2Numerator
      solution3 = str(factor_list[r])
  
      print("The solutions to your cubic are x = " + str(solution1) + ", x = " + str(solution2) + ", and x = " + str(float(solution3)))
  
  
    except: 
      print("Hmm, seems like the only non-complex solution to your cubic was x = " + str(float((factor_list[r]))) + ".")


poly_factored(a2, b2, c2)



print("Cool, it worked!")
