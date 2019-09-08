"""Module contains utility classes for generating number sequences and testing membership."""


class NumberSequence(object):

    # cache calculated terms of the sequence - use set for O(1) membership lookups and 
    # use sequence for O(1) lookup of max computed term
    SEQUENCE = [1]
    TERMS = {1}

    @classmethod
    def term(cls, n):
        """Return the value of the Nth term of the sequence."""
        raise NotImplementedError('Method must be implemented by child class')

    @classmethod
    def has_term(cls, value):
        """Return True if provided value is member of sequence."""
        while value > cls.SEQUENCE[-1]:
            next_term = cls.term(len(cls.SEQUENCE) + 1)
            cls.SEQUENCE.append(next_term)
            cls.TERMS.add(next_term)

        return value in cls.TERMS  # use set to test membership for constant time complexity


class TriangularNumbers(NumberSequence):

    @classmethod
    def term(cls, n):
        """Return the value of the Nth term of the sequence."""
        return int((n * (n + 1)) / 2)


class PentagonalNumbers(NumberSequence):

    @classmethod
    def term(cls, n):
        """Return the value of the Nth term of the sequence."""
        return int(n * ((3 * n) - 1) / 2)


class HexagonalNumbers(NumberSequence):

    @classmethod
    def term(cls, n):
        """Return the value of the Nth term of the sequence."""
        return int(n * ((2 * n) - 1))


class SquareNumbers(NumberSequence):

    @classmethod
    def term(cls, n):
        """Return the value of the Nth term of the sequence."""
        return int(n * n)
