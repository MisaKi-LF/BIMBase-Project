from pyp3d import *
# 旋转
def rot():
    return roty(-pi/2) * rotz(pi/2)

def rot1():
    return rotx(pi/2) * rotz(pi) * roty(pi)

def rot2():
    return rotx(pi/2) * rotz(pi) * roty(-pi/2)

def rot3():
    return rotx(pi/2) * roty(pi*2) * rotz(pi)

def rot4():
    return rotx(pi/2) * roty(pi*2) * rotz(pi/2)

def rot5():
    return rotx(pi) * rotz(-pi/2)

def rot6():
    return rotx(pi) * rotz(pi/2)

# 板
def DB1():
    LP_Z = Section(Vec2(0,0),Vec2(20,0),Vec2(20,10),Vec2(0,20))
    LP_Z = Loft(LP_Z,trans(0,0,20)*LP_Z)
    return LP_Z

def DB2():
    LP_J = Section(Vec2(0,0),Vec2(60,0),Vec2(60,60),Vec2(0,60))
    LP_Y = trans(45,60) * Section(scale(15)*Arc(1*pi))
    LP_O = LP_J + LP_Y
    LP_O = Loft(LP_O,trans(0,0,10)*LP_O)
    return LP_O

def DB3():
    LP_J = Section(Vec2(0,0),Vec2(60,0),Vec2(60,60),Vec2(0,60))
    LP_Y = trans(45,60) * Section(scale(15)*Arc(1*pi))
    LP_J1 = trans(60,0,0) * Section(Vec2(0,0),Vec2(30,0),Vec2(30,70),Vec2(0,70))
    LP_T = LP_J + LP_Y + LP_J1
    LP_T = Loft(LP_T,trans(0,0,10)*LP_T)
    return LP_T

def DB4():
    LR_D31 = Section(Vec2(0,0), Vec2(20,0),scale(10) * Arc(0.5*pi), Vec2(0, -20))
    LR_D32 = Section(Vec2(0,0), Vec2(20,0),scale(5) * Arc(0.5*pi), Vec2(0, -20))
    LR_D33 = Section(Vec2(0,5), Vec2(-5,5),Vec2(-5,10),Vec2(0,10))
    LR_D34 = Section(Vec2(5,0),Vec2(10,0),Vec2(10,-5),Vec2(5,-5))
    LR_D3 = LR_D31-LR_D32+LR_D33+LR_D34
    LR_D3 = Loft(LR_D3, trans(0,0,30)*LR_D3)
    return LR_D3

def DB5():
    testsection = Section(Vec2(5,-15),scale(5) * Arc(0.5*pi),Vec2(0,5),Vec2(-10,5),Vec2(-10,-15))
    LR_D4 = Loft(testsection, translate(0,0,5)*testsection)
    return LR_D4

def DB6(W):
     LR_D5 = Box(Vec3(W-10,900,0),Vec3(W-10,900,20),Vec3(1,0,0),Vec3(0,1,0),15,5,15,5)
     return LR_D5

def DB7():
    LR_D6 = Box(Vec3(0,0,0),Vec3(0,0,10),Vec3(1,0,0),Vec3(0,1,0),15,5,15,5)
    return LR_D6

def DB8(H):
    LT_D1 = Cone(Vec3(0,0,0),Vec3(0,0,H-10),8,8) - Cone(Vec3(0,0,0),Vec3(0,0,H-10),5,3) + Box(Vec3(5,-2.5,0),Vec3(5,-2.5,H-18),Vec3(1,0,0),Vec3(0,1,0),15,5,10,5) + Box(Vec3(-2.5,3,0),Vec3(-2.5,3,H-18),Vec3(1,0,0),Vec3(0,1,0),5,15,5,10) + Box(Vec3(-5,-2.5,0),Vec3(-5,-2.5,H-18),Vec3(1,0,0),Vec3(0,1,0),-15,5,-10,5)
    return LT_D1

def DB9(H,L):
    LT_D3 = Cone(Vec3(60,L-80,0),Vec3(60,L-80,H-10),10,10) - Cone(Vec3(60,L-80,0),Vec3(60,L-80,H-10),9,9)
    return LT_D3

def DB10(H,L):
    LT_D4 = Box(Vec3(0,0,H-8),Vec3(0,0,H-3),Vec3(1,0,0),Vec3(0,1,0),50,L,50,L)
    return LT_D4

def DB11(H,W):
    LT_D5 = Box(Vec3(0,0,H-8),Vec3(0,0,H-3),Vec3(1,0,0),Vec3(0,1,0),W/2,50,W/2,50)
    return LT_D5

class 路由器板(Component):
    def __init__(self):
        Component.__init__(self)
        # 设置模型参数
        self['宽度'] = Attr(300.0,obvious=True)
        self['高度'] = Attr(100.0,obvious=True)
        self['长度'] = Attr(1000.0,obvious=True)
        self['路由器板'] = Attr(None, show=True)
        self.space()

    @export
    def space(self):
        W = self['宽度']
        H = self['高度']
        L = self['长度']


        # 路由器正面
        LP = Box(Vec3(0,0,0),Vec3(0,0,H),Vec3(1,0,0),Vec3(0,1,0),W,15,W,15)
        # 路由器正面的内部构造
        LP_DB1 = rot() * DB1()
        LP_DB2 = rot() * DB2()
        LP_DB3 = rot() * DB3()
        Test_Array1 = Array(LP_DB1)
        Test_Array2 = Array(LP_DB2)
        Test_Array3 = Array(LP_DB3)
        for i in linspace(Vec3(40,15,H/2+20),Vec3(W-25,15,H/2+20),3):
            Test_Array1.append(translate(i))
        for i in linspace(Vec3(80,15,H),Vec3(230,15,H),2):
            Test_Array2.append(translate(i))
        for i in linspace(Vec3(120,15,H),Vec3(200,15,H),2):
            Test_Array3.append(translate(i))
        LP = LP + Test_Array1 + Test_Array2 + Test_Array3
        

        # 路由器左侧
        LL = Box(Vec3(0,0,0),Vec3(0,0,H),Vec3(1,0,0),Vec3(0,1,0),10,L,10,L)
        LL_D1 = rot1() * DB2()
        LL_D2 = rot1() * DB1()
        # 转为Array
        Test_Array4 = Array(LL_D1)
        Test_Array5 = Array(LL_D2)
        for i in linspace(Vec3(0,50,H),Vec3(0,L-50,H),6):
            Test_Array4.append(translate(i))
        for i in linspace(Vec3(0,100,H/2+20),Vec3(0,L-100,H/2+20),4):
            Test_Array5.append(translate(i))
        LL = LL + Test_Array4 + Test_Array5


        # 路由器右侧
        LR = Box(Vec3(W,0,0),Vec3(W,0,H),Vec3(1,0,0),Vec3(0,1,0),10,L,10,L)
        LRS = trans(0,-75,30) * Box(Vec3(W,900,0),Vec3(W,900,H-40),Vec3(1,0,0),Vec3(0,1,0),10,100,10,100)
        LRS1 = trans(0,-75,H-20) * Box(Vec3(W,900,0),Vec3(W,900,20),Vec3(1,0,0),Vec3(0,1,0),5,100,5,100)
        LRB = trans(0,-75,30) * Box(Vec3(W,150,0),Vec3(W,150,H-40),Vec3(1,0,0),Vec3(0,1,0),10,700,10,700)
        LR_D1 = rot3() * DB2()
        LR_D2 = rot3() * DB1()
        LR_D3 = rot4() * DB4()
        LR_D4 = trans(W-10,830,H-15) * rot3() * DB5()
        LR_D5 = trans(-5,0,H-20) * DB6(W)
        LR_D6 = DB7()
        Test_Array6 = Array(LR_D1)
        Test_Array7 = Array(LR_D2)
        Test_Array8 = Array(LR_D3)
        Test_Array9 = Array(LR_D6)
        for i in linspace(Vec3(W,60,H),Vec3(W,L-30,H),2):
            Test_Array6.append(translate(i))
        for i in linspace(Vec3(W,150,25),Vec3(W,L-200,25),4):
            Test_Array7.append(translate(i))
        for i in linspace(Vec3(W,250,10),Vec3(W,L-300,10),3):
            Test_Array8.append(translate(i))
        for i in linspace(Vec3(W-15,80,H-10),Vec3(W-15,765,H-10),2):
            Test_Array9.append(translate(i))
        LR = LR - LRS + LRS1 - LRB + Test_Array6 + Test_Array7 + Test_Array8 + LR_D4 + LR_D5 + Test_Array9


        # 路由器后侧
        LB = Box(Vec3(0,L,0),Vec3(0,L,H),Vec3(1,0,0),Vec3(0,1,0),W+10,10,W+10,10)
        LB_D1 = rot2() * DB1()
        LB_D2 = rot2() * DB3()
        LB_D3 = trans(W-100,L,H) * rot2() * DB2()
        Test_Array10 = Array(LB_D1)
        Test_Array11 = Array(LB_D2)
        for i in linspace(Vec3(60,L,H/2+10),Vec3(W-60,L,H/2+10),3):
            Test_Array10.append(translate(i))
        for i in linspace(Vec3(100,L,H),Vec3(200,L,H),2):
            Test_Array11.append(translate(i))
        LB = LB + Test_Array10 + Test_Array11 +LB_D3

        
        # 路由器头部
        LT = Box(Vec3(0,0,H-5),Vec3(0,0,H),Vec3(1,0,0),Vec3(0,1,0),W,L,W,L)
        LT_D1 = trans(60,100,H-3) * rot5() * DB8(H)
        LT_D2 = trans(W/2,L/2+15,H-3) * rot6() * DB8(H)
        LT_D3 = translate(0,0,9) * DB9(H,L)
        LT_D4 = trans(W/2-25,0,0) * DB10(H,L)
        LT_D5 = DB11(H,W)
        LT_D6 = translate(0,L/4+20,H-10) * Box(Vec3(W/4*3,0,0),Vec3(W/4*3,0,10),Vec3(1,0,0),Vec3(0,1,0),5,L/4*2,5,L/4*2)
        LT_D7 = Box(Vec3(W/4*3,L/4+20,0),Vec3(W/4*3,L/4+20,10),Vec3(1,0,0),Vec3(0,1,0),75,5,75,5)
        LT_D8 = Box(Vec3(W/4*3,0,H-8),Vec3(W/4*3,0,H-3),Vec3(1,0,0),Vec3(0,1,0),5,L,5,L)
        LT_D9 = Box(Vec3(W/2+35,L/4+20,H-8),Vec3(W/2+35,L/4+20,H-3),Vec3(1,0,0),Vec3(0,1,0),5,L/4*2,5,L/4*2)
        LT_D10 = Box(Vec3(W/4*3+30,L/4+30,H-8),Vec3(W/4*3+30,L/4+30,H-3),Vec3(1,0,0),Vec3(0,1,0),5,L/4*2,5,L/4*2)
        LT_D11 = Box(Vec3(60,0,H-8),Vec3(60,0,H-3),Vec3(1,0,0),Vec3(0,1,0),5,L/4*2,5,L/4*2)
        Test_Array12 = Array(LT_D5)
        Test_Array13 = Array(LT_D5)
        Test_Array14 = Array(LT_D7)
        Test_Array15 = Array(LT_D9)
        for i in linspace(Vec3(0,L/4,0),Vec3(0,L/2,0),2):
            Test_Array12.append(translate(i))
        for i in linspace(Vec3(W/2,L/4,0),Vec3(W/2,L/1.34,0),3):
            Test_Array13.append(translate(i))
        for i in linspace(Vec3(0,0,H-10),Vec3(0,L/2,H-10),4):
            Test_Array14.append(translate(i))
        for i in linspace(Vec3(0,0,0),Vec3(20,0,0),2):
            Test_Array15.append(translate(i))
        LT = LT+LT_D1 + LT_D2 + LT_D3 + LT_D4 + LT_D6 + LT_D8 + LT_D10  + Test_Array12 + Test_Array13 + Test_Array14 + Test_Array15+LT_D11
        # 路由器板 = Combine(LT)
        路由器板 = Combine(LP+LL+LR+LB+LT)
        self['路由器板'] = 路由器板

# 生成模型
if __name__ == "__main__":
    place(路由器板())
