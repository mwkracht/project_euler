"""Module contains unit tests which verify problem solutions return expected answers."""
import pytest

import project_euler


@pytest.mark.parametrize(
    'problem, answer',
    [
        ('problem_001', 233168),
        ('problem_002', 4613732),
        ('problem_003', 6857),
        ('problem_004', 906609),
        ('problem_005', 232792560),
        ('problem_006', 25164150),
        ('problem_007', 104743),
        ('problem_008', 23514624000),
        ('problem_009', 31875000),
        ('problem_010', 142913828922),
        ('problem_011', 70600674),
        ('problem_012', 76576500),
        ('problem_013', 5537376230),
        ('problem_014', 837799),
        ('problem_015', 137846528820),
        ('problem_016', 1366),
        ('problem_017', 21124),
        ('problem_018', 1074),
        ('problem_019', 171),
        ('problem_020', 648),
        ('problem_021', 31626),
        ('problem_022', 871198282),
        ('problem_023', 4179871),
        ('problem_024', 2783915460),
        ('problem_025', 4782),
        ('problem_067', 7273),
    ]
)
def test_solutions(problem, answer):
    """Verify all solutions to each specific problem return expected answer."""
    for solution in getattr(project_euler, problem).SOLUTIONS:
        result = solution()
        assert result == answer, \
            '{0}.{1} retuned {2}, Answer {3}'.format(problem, solution.__name__, result, answer)
