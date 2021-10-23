#计算器类
class Calculator:
    """用于完成两个数的加减乘除"""
    # ->常常出现在python函数定义的函数名后面，为函数添加元数据,描述函数的返回类型，
    # 从而方便开发人员使用。
    def __init__(self,a,b) -> None:
        self.a = int(a)
        self.b = int(b)

    #加法
    def add(self):
        return self.a + self.b

    #减法
    def sub(self):
        return self.a - self.b
    
    #乘法
    def mul(self):
        return self.a * self.b
    
    #除法
    def div(self):
        return self.a / self.b


