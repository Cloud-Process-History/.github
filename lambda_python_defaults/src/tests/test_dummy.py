import pytest

from lambda_code.lambda_code import lambda_handler

def test_dummy():

    result = lambda_handler({},{})
    assert result == 'hello!'