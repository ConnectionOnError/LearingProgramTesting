from test_Calculator import Calculator
#测试加法
def test_add():
    c = Calculator(3,5)
    result = c.add()
    assert result == 8, '加法运算失败'
#测试减法
def test_sub():
    c = Calculator(10,5)
    result = c.sub()
    assert result == 5, '减法运算失败'

def test_mul():
    c = Calculator(3,5)
    result = c.mul()
    assert result == 15, '乘法法运算失败'
#测试除法，人为的制造错误
def test_div():
    c = Calculator(6,2)
    result = c.div()
    assert result == 1, '除法运算失败'


if __name__ == '__main__':
    test_add()
    test_sub()
    test_mul()
    test_div()
