from . import equations, integration, series, stats

HANDLERS = {
    **equations.HANDLERS,
    **integration.HANDLERS,
    **series.HANDLERS,
    **stats.HANDLERS
}