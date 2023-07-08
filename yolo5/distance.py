foc = 740.0        # 镜头焦距
real_hight_tank = 4.5   # tank高度
real_hight_plane = 4.5   # plane高度

# 自定义函数，单目测距
def tank_distance(h):
    dis_inch = (real_hight_tank * foc) / (h - 2)
    dis_cm = dis_inch * 2.54
    dis_cm = int(dis_cm)
    dis_m = dis_cm/100
    return dis_m
def plane_distance(h):
    dis_inch = (real_hight_plane * foc) / (h - 2)
    dis_cm = dis_inch * 2.54
    dis_cm = int(dis_cm)
    dis_m = dis_cm/100
    return dis_m