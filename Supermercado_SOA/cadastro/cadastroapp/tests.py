from django.test import TestCase

# Create your tests here.
import re

__all__ = ['validar_cpf']

def validar_cpf(cpf):

    cpf = ''.join(re.findall('\d', str(cpf)))
    print (cpf)
    if (not cpf) or (len(cpf) < 11):
        return False


    inteiros = map(int, cpf)
    novo = inteiros[:9]

    while len(novo) < 11:
        r = sum([(len(novo)+1-i)*v for i,v in enumerate(novo)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)


    if novo == inteiros:
        return cpf
    return False


if __name__ == "__main__":
    import doctest, sys
    result = doctest.testmod() #verbose=True)
    if result[0] == 0:
        print "OK!"
    else:
        print result