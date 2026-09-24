import math

MAX_TERMS = 10_000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100_000
DIGITS = 4

def sign(n):
    return -1 if n % 2 == 0 else 1

def term_sqplus(n):
    return sign(n) / (n * n + 1)

def term_third(n):
    return sign(n) / (3 * n)


FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third":  (term_third,  "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
}

def solve_series(args):
    term, formula = FORMULAS[args['func']]
    if not args['eps'] is None:
        validate_eps(args['eps'])
        total, n = sum_by_eps(term, args['eps'])
    else:
        validate_terms(args['terms'])
        total, n = sum_by_terms(term, args['terms'])

    return formula, total, n

def validate_terms(cnt):
    if not 1 <= cnt <= MAX_TERMS:
        raise ValueError(f"количество слагаемых должно быть от 1 до{MAX_TERMS}")
    return cnt


def validate_eps(eps):
    if not math.isfinite(eps) or not 0 < eps <= MAX_EPS:
        raise ValueError(f"точность должна быть больше 0 и не грубее {MAX_EPS}")
    return eps

# ---------- суммирование ----------
def sum_by_terms(term, cnt):
    total = 0
    for n in range(1, cnt + 1):
        total += term(n)
    return total, cnt

def sum_by_eps(term, eps):
    total = 0
    for n in range(1, MAX_ITERATIONS + 1):
        value = term(n)
        total += value
        if abs(value) < eps:
            return total, n
    raise ValueError("точность не достигнута")

COMMANDS = {
    "series": solve_series
}