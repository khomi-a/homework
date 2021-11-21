from random import randint
# from abc import ABC, abstractmethod


class RNA:

    def __init__(self, acid):
        if not isinstance(acid, str):
            raise TypeError('Acid must be str type')
        if acid.count('A') + acid.count('U') + \
                acid.count('G') + acid.count('C') != len(acid):
            raise Exception('Only nucliotides A, U, G, C must be in RNA')
        self.acid = acid

    def __getitem__(self, item):
        return self.acid[item]

    def __add__(self, other):
        return RNA(self.acid + other.acid)

    def __mul__(self, other):
        s1, s2 = self.acid, other.acid
        if len(s1) < len(s2):
            s1, s2 = s2, s1  # make s1 longer
        res = ''
        for i in range(len(s2)):
            if bool(randint(0, 1)):
                res += s1[i]
            else:
                res += s2[i]
        if len(s1) != len(s2):
            res += s1[len(s2)+1:]
        return RNA(res)

    def __eq__(self, other):
        return self.acid == other.acid

    def __ne__(self, other):
        return self.acid != other.acid

    def __repr__(self):
        return self.acid, 'Class RNA'

    def __str__(self):
        return 'RNA: ' + self.acid


class DNA:

    def __init__(self, acid):
        if not isinstance(acid, str):
            raise TypeError('Acid must be str type')
        if acid.count('A') + acid.count('T') + \
                acid.count('G') + acid.count('C') != len(acid):
            raise Exception('Only nucliotides A, T, G, C must be in DNA')
        self.acid = acid
        d = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        acid2 = ''
        for N in acid:
            acid2 += d[N]
        self.acid2 = acid2

    def __getitem__(self, item):
        return self.acid[item] + '-' + self.acid2[item]

    def __add__(self, other):
        return DNA(self.acid + other.acid)

    def __mul__(self, other):
        s1, s2 = self.acid, other.acid
        if len(s1) < len(s2):
            s1, s2 = s2, s1  # make s1 longer
        res = ''
        for i in range(len(s2)):
            if bool(randint(0, 1)):
                res += s1[i]
            else:
                res += s2[i]
        if len(s1) != len(s2):
            res += s1[len(s2)+1:]
        return DNA(res)

    def __eq__(self, other):
        return self.acid == other.acid

    def __ne__(self, other):
        return self.acid != other.acid

    def __repr__(self):
        return [self.acid, self.acid2], 'Class DNA'

    def __str__(self):
        return 'DNA: ' + self.acid + '\n' + ' '*5 +\
               '|' * len(self.acid) + '\n' + ' '*5 + self.acid2
