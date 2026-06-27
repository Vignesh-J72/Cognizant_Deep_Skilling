import pytest

#PyTest uses 'test_NAME.py' syntax to discover test programs

#Assert using function
def func(x):
    return x+5

#Multiple tests in one class
# PyTest using TestClass and 'test_' keywords to discover testing classes 
class TestClass:
    def test_one(self):
        x=0
        assert x==1
    
    def test_two(self):
        x="H"
        assert x in "Hello world"



if __name__=="__main__":
    #Basic assert
    assert sum([12,3,5])==20, "Should be equal to 20"
    
    #assert using function
    assert func(4)==9

    
    
