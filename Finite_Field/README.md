# Finite Field

Basically it's a different way to operate addition, subtractions, multiplication and division considering the existent numbers in vectors. Not all vectors can be Finite Field, they need have some properties. 

> F<sub>x</sub>  = {0,1,2, ... , x -1 } 

### For **Sum** and **Subtractions**:

'''(12 + 843) % 60 = 15'''

> The sign % consider the rest of division, in the case rest the division by 60. 

### **Multiplication** and **Exponentiation**:

For F<sub>19</sub>   

'''3 *<sub>f</sub> 5 = 5 +<sub>f</sub> 5 +<sub>f</sub>  5 = 15 % 19 = 15'''

> The sign ' f ' means finite field, so ' +<sub>f</sub> ' sum of finite field.


*Resume*: 

  a +<sub>f</sub> b = (a + b)%p  