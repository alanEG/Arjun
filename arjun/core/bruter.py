import core.config as mem

from core.anomaly import compare
from core.requester import requester
from core.error_handler import error_handler


def bruter(request, factors, params, mode='bruteforce',match_string=None,match_regex=None):
    """
    returns anomaly detection result for a chunk of parameters
    returns list
    """
    if mem.var['kill']:
        return []
    response = requester(request, params)
    conclusion = error_handler(response, factors)
    if conclusion == 'retry':
        return bruter(request, factors, params, mode=mode)
    elif conclusion == 'kill':
        mem.var['kill'] = True
        return []
    comparison_result = compare(response, factors, params,match_string,match_regex)
    if mode == 'verify':
        return comparison_result[0]
    return comparison_result[1]
