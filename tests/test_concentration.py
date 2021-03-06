import os
import random

import pytest
from pytest import list_of

from src.lib.math import concentration
from src.lib.io import file_read

TEST_DATAFILE = file_read.asc(
    os.path.join(os.path.dirname(__file__), "files/full_file.dp_rpc_asc")
)


class TestConcentration:
    @pytest.mark.randomize(
        impurities=list_of(float, items=100), matrix=list_of(float, items=100)
    )
    def test_calculate(self, impurities, matrix):
        ia = random.random()
        rsf = random.uniform(1e15, 1e25)
        assert concentration.calculate(impurities, ia, matrix, rsf) == [
            i / ia / 100 / m * rsf for i, m in zip(impurities, matrix)
        ]

    @pytest.mark.randomize(
        impurities=list_of(float, items=random.randint(1, 100)),
        matrix=list_of(float, items=random.randint(101, 200)),
    )
    def test_list_len(self, impurities, matrix):
        ia = random.random()
        rsf = random.uniform(1e15, 1e25)
        with pytest.raises(AssertionError):
            concentration.calculate(impurities, ia, matrix, rsf)
