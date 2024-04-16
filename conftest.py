import pytest

@pytest.fixture(scope='class')
def X_Xsrf_Token():
    X_Xsrf_Token = '1fd61d4f21844f8489c56e6981737c59'
    return X_Xsrf_Token

@pytest.fixture(scope='class')
def Cookie():
    Cookie = 'XSRF-TOKEN=1fd61d4f21844f8489c56e6981737c59; CURRENT_USER=admin; ACCESS_TOKEN=ff0efd87e7774dbdb97c6b4b001483e9'
    return Cookie