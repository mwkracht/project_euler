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
        ('problem_026', 983),
        ('problem_027', -59231),
        ('problem_028', 669171001),
        ('problem_029', 9183),
        ('problem_030', 443839),
        ('problem_031', 73682),
        ('problem_032', 45228),
        ('problem_033', 100),
        ('problem_034', 40730),
        ('problem_035', 55),
        ('problem_036', 872187),
        ('problem_037', 748317),
        ('problem_038', 932718654),
        ('problem_039', 840),
        ('problem_040', 210),
        ('problem_041', 7652413),
        ('problem_042', 162),
        ('problem_043', 16695334890),
        ('problem_044', 5482660),
        ('problem_045', 1533776805),
        ('problem_046', 5777),
        ('problem_047', 134043),
        ('problem_048', '9110846700'),
        ('problem_049', 296962999629),
        ('problem_050', 997651),
        ('problem_067', 7273),
    ]
)
def test_solutions(problem, answer):
    """Verify all solutions to each specific problem return expected answer."""
    for solution in getattr(project_euler, problem).SOLUTIONS:
        result = solution()
        assert result == answer, \
            '{0}.{1} retuned {2}, Answer {3}'.format(problem, solution.__name__, result, answer)
