def add(a,b):
    return a+b

def test_add():
    assert add(10,5) == 15



#----------fixtures----------

import pytest
@pytest.fixture
def my_data():
    return [1,2,3,4,5]

def test_my_data(my_data):
    assert len(my_data) == 5



#----------parameterization----------

import pytest
@pytest.mark.parametrize("a,b,expected", [(2,3,5),
                                          (5,5,10),
                                          (1,1,2),
                                          ])
def test_add(a,b,expected):
    assert a+b == expected



#----------grouping test using class----------

class test:
    def test_setup(self):
        self.a = 10
        self.b = 20

    def test_add(self):
        assert 10+20 == 30



import pytest

def add(a,b):
    return a+b


class testassert:
    def test_add(self):
        assert 10+20 == 3

    def test_sub(self):
        assert 20-10 == 2
        
        
#----------handling exception----------

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    else:
        return a/b

def test_divide_success():
    assert divide(10,2) == 2

def test_divide_failure():
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(10,0)
        assert "cannot divide by zero" in str(excinfo.value)


import pytest
@pytest.mark.smoke
def test_login():
    assert True

def test_add_success():
    assert True
@pytest.mark.regression
def test_add_failure():
    assert False

#----------

@pytest.mark.skip(reason="this is a skip")
def test_skip():
    assert True
    
@pytest.mark.xfail
def test_xfail():
    assert False

