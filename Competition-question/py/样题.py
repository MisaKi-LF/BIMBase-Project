from pyp3d import *
class 桌面茶几(Component):
    def __init__(self):
        # 模型参数
        Component.__init__(self)
        self['茶几长度'] = Attr(1000.0, obvious=True)
        self['茶几宽度'] = Attr(550.0,obvious=True)
        self['茶几高度'] = Attr(330.0,obvious=True)
        self['茶几模型'] = Attr(None, show=True)
        self.replace()
    @export
    # 生成模型
    def replace(self):
        # 设置变量，同时调用参数(简化书写过程)
        # 绘制模型
        C = self['茶几长度']
        W = self['茶几宽度']
        H = self['茶几高度']

        ZM1 = Section(Vec2(0,0),Vec2(C,0),Vec2(C,W),Vec2(0,W))
        ZT1 = Section(Vec2(0,0),Vec2(20,0),Vec2(20,25),Vec2(0,25))
        testsweep1 = Loft(ZM1,translate(0,0,15) * ZM1).color(1,1,1,0.3)
        ZT1 = Loft(ZT1,translate(0,0,315) * ZT1)
        ZT2 = trans(0,0,315) * rotx(-pi/2) * ZT1
        ZT3 = trans(0,315,0) * ZT1 
        ZT4 = trans(0,0,-290) * ZT2
        ZT5 = ZT1 + ZT2 + ZT3 + ZT4 
        ZT6 = Section(Vec2(0,0),Vec2(C-400,0),Vec2(C-400,20),Vec2(0,20))
        ZT6 = trans(0,315/2,295) * Loft(ZT6, translate(0,0,20)*ZT6)
        ZT7 = trans(C-400,0,0) * ZT5
        ZTH = ZT5+ZT6+ZT7
        ZTH = trans(200,W/2-76-76-20,-315) * ZTH
        self['茶几模型'] =Combine(ZTH,testsweep1)
        # create_geometry(testection)

class 电视柜(Component):
    def __init__(self):
        Component.__init__(self)
        self['电视柜高度'] = Attr(535.0,obvious=True)
        self['电视柜宽度'] = Attr(450.0,obvious=True)
        self['电视柜长度'] = Attr(1200.0,obvious=True)
        self['电视柜'] = Attr(None, show=True)
        self.replace()
    @export
    # 生成模型
    def replace(self):
        H = self['电视柜高度']
        W = self['电视柜宽度']
        w = self['电视柜长度']
        # 后板
        HBT = Box(Vec3(19,0,0),Vec3(0,0,19),Vec3(1,0,0),Vec3(0,1,0),1162,W,w,W)
        HBB = translate(0,W,-H+38) * rotx(pi) * HBT
        HBL = roty(pi/2) * Box(Vec3(0,0,0),Vec3(19,0,19),Vec3(1,0,0), Vec3(0,1,0),H,W,H-19-19,W)
        HBR = trans(w,0,-H+19) * roty(pi) * HBL
        HBL = trans(0,0,19) * HBL
        HBH = trans(0,W-19,19) * rotx(-pi/2) * Box(Vec3(19,0,0),Vec3(0,0,19),Vec3(1,0,0),Vec3(0,1,0),1162,H,w,H)
        BLB1 = Box(Vec3(0,0,0),Vec3(0,0,H-19-19),Vec3(1,0,0),Vec3(0,1,0),w/3,19,w/3,19)
        BLB2 = translate(19,10,-H+36) * BLB1
        BLB3 = translate(w/3+20,5,-H+38) * BLB1
        BLB4 = translate(w/2+220,0,-H+38) * Box(Vec3(0,0,0),Vec3(0,0,H-19-19),Vec3(1,0,0),Vec3(0,1,0),375,19,375,19)
        HBZ = HBT + HBB + HBL + HBR + HBH
        BLBT = BLB2+BLB3
        YJ1 = Cone(Vec3(0,0,0),Vec3(19,0,135),10,10)
        YJ2 = translate(19,19,-H-115) * YJ1
        YJ3 = translate(19,450-19,-H-115) * YJ1
        YJ4 = Cone(Vec3(0,0,0),Vec3(-19,0,135),10,10)
        YJ5 = translate(w-19,19,-H-115) * YJ4
        YJ6 = translate(w-19,450-19,-H-115) * YJ4
        YJ7 = YJ2+YJ3+YJ5+YJ6
        self['电视柜'] = Combine(HBZ,BLBT,BLB4,YJ7)

class 吊灯构件(Component):
    def __init__(self):
        Component.__init__(self)
        self['吊灯高度'] = Attr(1000.0,obvious=True)
        self['灯体半径'] = Attr(300.0,obvious=True)
        self['吊灯构件'] = Attr(None, show=True)
        self.splace()
    @export

    def splace(self):
        # 生成模型
        H = self['吊灯高度']
        R = self['灯体半径']
        qiu = Sphere(Vec3(0,0,0),R)
        DD1 = trans(0,0,R) * Cone(Vec3(0,0,0),Vec3(0,0,H),9,9)
        DZ1 = Cone(Vec3(0,0,0),Vec3(0,0,-50),78,47)
        DZ2 = Cone(Vec3(0,0,-50),Vec3(0,0,-70),5,5)
        DZ3 = trans(-15,0,0) * DZ2
        DZ4 = trans(15,0,0) * DZ2
        DZ = DZ1+DZ3+DZ4
        DZ = trans(0,0,H+R) * DZ
        self['吊灯构件'] = Combine(qiu,DD1, DZ)
        



# 生成模型
if __name__ == "__main__":
    FinalGeometry = 桌面茶几()
    FinalGeometry1 = 电视柜()
    FinalGeometry2 = 吊灯构件()
    place(FinalGeometry)
    # place(FinalGeometry1)
    # place(FinalGeometry2)