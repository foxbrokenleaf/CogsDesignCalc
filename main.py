import math

CN_A = math.pi / 9
CN_Ha = 1
CN_C = 0.25

def Calc(M, Z, T = 0, A = CN_A, HA = CN_Ha, C = CN_C,):
    print(f"压力角 a={A}")
    print(f"齿顶高系数ha*={HA}")
    print(f"顶隙系数c*={C}")
    print("-".center(20,'-'))
    d = M * Z
    ha = (Z + 2 * HA) * M
    hr = (Z - 2 * HA - 2 * C) * M
    d_base = d * math.cos(A)    
    r_base = d_base / 2    
    print(f"分度圆直径：d={M}*{Z}={d}")
    print(f"齿顶圆直径：ha=({Z}+2*{HA})*{M}={ha}")
    print(f"齿根圆直径：hr=({Z}-2*{HA}-2*{C})*{M}={hr}")
    print(f"基圆直径：db={M}*{Z}*cos(pi/9)={d}*cos({A})={d_base}")
    print(f"基圆半径：dr={M}*{Z}*cos(pi/9)/2={d_base}/2={r_base}")
    print("-".center(20,'-'))
    print("渐开线方程(t取0~PI/3)".center(20 - "渐开线方程(t取0~PI/3)".__len__(),'-'))
    x_t = r_base * math.sin(T) - r_base * T * math.cos(T)
    y_t = r_base * math.cos(T) + r_base * T * math.sin(T)
    print(f"x_t={M}*{Z}*cos(pi/9)/2*sin(t)-{M}*{Z}*cos(pi/9)/2*t*cos(t)={r_base}*sin({T})-{r_base}*{T}*cos({T})={round(x_t,2)}")
    print(f"y_t={M}*{Z}*cos(pi/9)/2*cos(t)+{M}*{Z}*cos(pi/9)/2*t*sin(t)={r_base}*cos({T})+{r_base}*{T}*sin({T})={round(y_t,2)}")
    print("-".center(20,'-'))
    print("中心距".center(20 - "中心距".__len__(),'-'))
    a = M
    
    print(f"镜像轴偏移角度_1\n{360/Z/4}")
    print(f"镜像轴偏移角度_2\n{360/Z/4*3}")
    pass

if __name__ == "__main__":
    Cogs_M = int(input("齿轮的模数 m = "))
    Cogs_Z = int(input("齿轮的齿数 z = "))
    Calc(Cogs_M, Cogs_Z)