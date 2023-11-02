import random
random.seed(42)
min_num = 1200
max_num = 2500
input_click_numbers = [random.randrange(min_num, max_num) for _ in range(365)]

print(input_click_numbers)

def test(capsys):
    expected = '1.0.0'
    assert np.__version__ >= expected

import numpy as np
capsys = np.__version__
test(capsys)