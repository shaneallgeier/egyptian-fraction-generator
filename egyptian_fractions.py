# Implements Ian Stewart's Short Sequence method
# https://www.ics.uci.edu/~eppstein/numth/egypt/force.html#short
import sys
from datetime import datetime
from fractions import Fraction


NUMBER_OF_TERMS = 3

def egyptian_fractions(num, k=2, b=0, current_terms=None):
    if not current_terms:
        current_terms = [Fraction(1, 1)] * NUMBER_OF_TERMS

    if num.numerator == 0:
        # The base case
        if b == NUMBER_OF_TERMS:
            # If we're in here, it means we made it to a solution
            return True
        else:
            # No solution was found, give up and move on
            return False

    j = (num.denominator + num.numerator - 1) // num.numerator
    if j >= k:
        k = j

    for i in range(k, j*(NUMBER_OF_TERMS-b)+1):
        current_terms[b] = Fraction(1, i)
        if egyptian_fractions(num - current_terms[b], i+1, b+1, current_terms):
            print ' '.join(map(str, current_terms))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: %s <number that is being divided by 4>' % sys.argv[0])
    num = int(sys.argv[1])
    then = datetime.now()
    print 'Finding x,y,z for %d' % num
    egyptian_fractions(Fraction(4, num))
    print '\nTime taken: %s' % (datetime.now() - then)
