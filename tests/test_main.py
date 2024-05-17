from src.main import *
import pytest
from contextlib import nullcontext as not_raise


class Testmain:
    @pytest.mark.parametrize("x,y,res, not_error",
                             [(0,10,10,not_raise()),
                              (5,20,25,not_raise()),
                              (5,-20,-15,not_raise()),
                              (20,-5,15,not_raise()),
                              (0,-5,-5,not_raise()),
                              (10,-10,0,not_raise()),
                              (4.5,4.5,9,not_raise()),
                              (4.5,5,9.5,not_raise()),
                              (5,4.5,9.5,not_raise()),
                              (4.5,-4.5,0,not_raise()),
                              (-4.5,-4.5,-9,not_raise()),
                              (0,0,0,not_raise()),
                              ("0",10,10,pytest.raises(TypeError)),
                              (5,"1",6,pytest.raises(TypeError)),
                              ("5","1",6,pytest.raises(TypeError))
                             ])
    def test_sum(self,x,y,res,not_error):
        with not_error:
            assert Main().sum(x,y) == res

    @pytest.mark.parametrize("x,y,res, not_error",
                             [(0,5,0,not_raise()),
                              (5,0,0,not_raise()),
                              (5,5,25,not_raise()),
                              (-5,5,-25,not_raise()),
                              (5,-5,-25,not_raise()),
                              (-5,-5,25,not_raise()),
                              (2.5,5,12.5,not_raise()),
                              (5,2.5,12.5,not_raise()),
                              (4,2.5,10,not_raise()),
                              ("4",5,20,pytest.raises(TypeError)),
                              (4,"5",20,pytest.raises(TypeError)),
                              ("4","5",20,pytest.raises(TypeError))])
    def test_mul(self,x,y,res,not_error):
        with not_error:
            assert Main().mul(x,y) == res


    @pytest.mark.parametrize("x,y,res, not_error",
                             [(10,2,5,not_raise()),
                              (10,10,1,not_raise()),
                              (10,-5,-2,not_raise()),
                              (-10,-5,2,not_raise()),
                              (-10,5,-2,not_raise()),
                              (5,2.5,2,not_raise()),
                              (5.5,2,2.75,not_raise()),
                              (-5,2.5,-2,not_raise()),
                              (5.5,-2,-2.75,not_raise()),
                              (0,5,0,not_raise()),
                              (10,0,0,pytest.raises(ZeroDivisionError)),
                              ("10",2,5,pytest.raises(TypeError)),
                              (10,"2",5,pytest.raises(TypeError)),
                              ("10","2",5,pytest.raises(TypeError))])
    def test_div(self,x,y,res,not_error):
        with not_error:
            assert Main().div(x,y) == res

    @pytest.mark.parametrize("x,y,res, not_error",
                             [(10,5,5,not_raise()),
                              (10,10,0,not_raise()),
                              (10,-10,20,not_raise()),
                              (-10,10,-20,not_raise()),
                              (0,0,0,not_raise()),
                              (10.5,5,5.5,not_raise()),
                              (10,5.5,4.5,not_raise()),
                              ("10",5,5,pytest.raises(TypeError)),
                              (10,"5",5,pytest.raises(TypeError)),
                              ("10","5",5,pytest.raises(TypeError))])
    def test_sub(self,x,y,res,not_error):
        with not_error:
            assert Main().sub(x,y) == res

