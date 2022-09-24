# -*- coding: utf-8 -*-

#Code extract from reference [1] and personalized comments

#Notations
#Fermat's Little Theorem = FLT

#DIGSIG
# will-bc
# github.com/will-bc/Blockchain-Cryptocurrency/tree/main/Finite_Field


class FieldElement:
        def __init__(self, num, prime): #declaration of number inside of vector (FiniteField) and the range of the field (prime number) according math definitions
                if num >= prime or num < 0: #conditions when the number (element) is not inside finite field
                        error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
                        raise ValueError(error)
                self.num = num
                self.prime = prime

        def __repr__(self):
                return 'FieldElement_{}({})'.format(self.prime, self.num) 

        def __eq__(self, other):
                if other is None:
                        return False
                return self.num == other.num and self.prime == other.prime #verification of the element from the field is the same

        def __add__(self, other):
                if self.prime != other.prime: #verification if the two numbers belong to the same finite field
                        raise TypeError('Cannot add two numbers in different Fields')
                num = (self.num + other.num) % self.prime  ##### <---- sum operation
                return self.__class__(num, self.prime)

        def __sub__(self, other): 
                if self.prime != other.prime:  #verification if the two numbers belong to the same finite field
                    raise TypeError('Cannot subtract two numbers in different Fields')
                num = (self.num - other.num) % self.prime  ##### <---- subtraction operation
                return self.__class__(num, self.prime)


        def __mul__(self,other):
                if self.prime != other.prime: #verification if the two numbers belong to the same finite field
                        raise TypeError('Cannot add two numbers in different Fields')
                num = (self.num * other.num) % self.prime  ##### <---- multiplication operation
                return self.__class__(num, self.prime)

        def __pow__(self, exponent): #exponent its not needs be field element
                n = exponent % (self.prime - 1 ) #playing around FLT to solve negative exponents
                num= pow(self.num, n, self.prime) ### <-- Exponention operation
                return self.__class__(num, self.prime)

        def __truediv__(self,other):
                if self.prime != other.prime: #verification if the two numbers belong to the same finite field
                        raise TypeError ('Cannot divide two numbers in different Fields')                
                num = self.num * pow(other.num, self.prime - 2, self.prime) % self.prime ### <-- division using FLT
                return self.__class__(num, self.prime)

        
