from typing import List

import numpy


def mean(values: List[float]) -> float:
    """Calculate arithmetic mean

    Parameters
    ----------
    values : list of values for mean calculation

    Returns
    -------
    Mean value

    """
    result = numpy.mean(values)
    return result
