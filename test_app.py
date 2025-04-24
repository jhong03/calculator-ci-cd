import pytest
import yaml
from app import calculate

import os
path = os.path.join(os.path.dirname(__file__), "test_data.yml")
with open(path, "r") as f:
    test_cases = yaml.safe_load(f)['tests']

@pytest.mark.parametrize("test", test_cases)
def test_calculator(test):
    a = test['a']
    b = test['b']
    operation = test['operation']
    if 'expected' in test:
        result = calculate(a, b, operation)
        assert result == pytest.approx(test['expected']), f"Failed on {test}"
    elif 'error' in test:
        with pytest.raises(Exception) as e:
            calculate(a, b, operation)
        assert test['error'] in str(e.value)
