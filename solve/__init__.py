from . import equations, integration, stats, series, arrays_solve

SOLVES = {
    **equations.COMMANDS,
    **integration.COMMANDS,
    **stats.COMMANDS,
    **series.COMMANDS,
    **arrays_solve.COMMANDS
}