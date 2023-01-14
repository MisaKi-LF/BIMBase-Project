from pyp3d import *
class 灯笼(Component):
    def __init__(self):
        Component.__init__(self)
        self['灯笼'] = Attr(None, show = True)
        self['瓣数'] = Attr(7, obvious = True, group = '灯笼')
        self['半径'] = Attr(30.0, obvious = True, group = '灯笼')
        self['端长'] = Attr(5.0, obvious = True, group = '灯笼')
        self['厚度'] = Attr(1.5, obvious = True, group = '灯笼')
        self.replace()
    @export
    def replace(self):
        
        n = self['瓣数']
        lantern_R = self['半径']
        head_length = self['端长']
        lantern_T = self['厚度']

        n1 = n/2
        n = int(n1)*2
        radio = (lantern_R-lantern_T)/lantern_R

        
        # 灯笼实体
        clove = Cone(Vec3(-50, 0, 0), Vec3(50, 0, 0), lantern_R, lantern_R)
        cloves = Combine()
        
        for i in linspace(0, pi *(int(n1)-1)/int(n1), int(n1)):
            clove_temp = rotz(i)*clove
            cloves.append(clove_temp)
        lantern_outer = clove

        for j in range(len(cloves.parts)):
            lantern_outer = Intersect(lantern_outer, cloves.parts[j])
        # 灯笼内部空心体
        lantern_inner = scale(radio)*lantern_outer
        
        # 灯笼端部平齐
        hollow_top = trans(-lantern_R, -lantern_R, lantern_R-head_length)*scale(2*lantern_R)*Cube()
        hollow_bottom = mirror('XY') * hollow_top
        lantern_outer = lantern_outer-hollow_top-hollow_bottom
        lantern_inner = lantern_inner-hollow_top-hollow_bottom
        lantern = lantern_outer-lantern_inner

        # 端头：通过计算端头截面点得到面
        R = sqrt(lantern_R**2-(lantern_R-head_length)**2)/cos(pi/n)
        r = sqrt((lantern_R*radio)**2-(lantern_R-head_length)**2)/cos(pi/n)
        point_R = Vec2(R, 0)
        point_r = Vec2(r, 0)
        points_R = []
        points_r = []
        coeff = 0
        if (n/2)%2 == 0:
            coeff = 1
        for i in linspace(0, pi*2*(n-1)/n, n):
            points_R.append(rotz(i+pi/n*coeff)*point_R)
        sec_R = to_section(trans(0, 0, lantern_R-head_length)*points_R)
        for i in linspace(0, pi*2*(n-1)/n, n):
            points_r.append(rotz(i+pi/n*coeff)*point_r)
        sec_r = to_section(trans(0, 0, lantern_R-head_length)*points_r)
        head_top = Loft(sec_R, trans(0, 0, head_length)*sec_R)-Loft(sec_r, trans(0, 0, head_length)*sec_r)
        head_bottom = mirror('XY') * head_top
        head = Combine(head_top,head_bottom)
        self['灯笼'] = Combine(lantern, head).color(1, 0, 0, 1)

if __name__ == "__main__":
    place(灯笼())