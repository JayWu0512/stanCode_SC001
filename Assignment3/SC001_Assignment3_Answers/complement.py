"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    print complement strand of a DNA sequence.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    step 1 : print 'DNA strand is missing' when it's empty string.(boundary condition)
    step 2 : change the word from A to T, T to A , C to G ,G to C.
    step 3 : return the answer to main function.
    """
    if dna == '':
        dna = 'DNA strand is missing.'
        return dna
    else:
        ans = ''
        for i in range(len(dna)):
            if dna[i] == 'A':
                ans = ans + 'T'
            elif dna[i] == 'T':
                ans = ans + 'A'
            elif dna[i] == 'G':
                ans = ans + 'C'
            elif dna[i] == 'C':
                ans = ans + 'G'
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
