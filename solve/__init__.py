from . import equations, integration, stats, series

SOLVES = {
    **equations.COMMANDS,
    **integration.COMMANDS,
    **stats.COMMANDS,
    **series.COMMANDS
}