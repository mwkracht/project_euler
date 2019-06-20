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
    ]
)
def test_solutions(problem, answer):
    """Verify all solutions to each specific problem return expected answer."""
    for solution in getattr(project_euler, problem).SOLUTIONS:
        result = solution()
        assert result == answer, \
            '{0}.{1} retuned {2}, Answer {3}'.format(problem, solution.__name__, result, answer)
