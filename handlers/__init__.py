from . import equations_hnd, integration_hnd, series_hnd, stats_hnd

HANDLERS = {
    **equations_hnd.HANDLERS,
    **integration_hnd.HANDLERS,
    **series_hnd.HANDLERS,
    **stats_hnd.HANDLERS
}