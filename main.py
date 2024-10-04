import tkinter as tk
import math

CN_A = math.pi / 9
CN_Ha = 1
CN_C = 0.25

def Calc(M, Z, T = 0, A = CN_A, HA = CN_Ha, C = CN_C,):
    output_str = f"压力角 a={A}" + '\n'
    output_str += f"齿顶高系数ha*={HA}" + '\n'
    output_str += f"顶隙系数c*={C}" + '\n'
    output_str += "-".center(50,'-') + '\n'
    d = M * Z
    ha = (Z + 2 * HA) * M
    hr = (Z - 2 * HA - 2 * C) * M
    d_base = d * math.cos(A)    
    r_base = d_base / 2    
    output_str += f"分度圆直径：d={M}*{Z}={d}" + '\n'
    output_str += f"齿顶圆直径：ha=({Z}+2*{HA})*{M}={ha}" + '\n'
    Exmple_Show_Canvas.delete(tk.ALL)
    Exmple_Show_Canvas.create_oval(10,10,10 + ha,10 + ha,outline="RED")
    output_str += f"齿根圆直径：hr=({Z}-2*{HA}-2*{C})*{M}={hr}" + '\n'
    Exmple_Show_Canvas.create_oval(10 + (ha - hr) / 2,10 + (ha - hr) / 2,10 + (ha - hr) / 2 + hr,10 + (ha - hr) / 2 + hr,outline="BLUE")
    output_str += f"基圆直径：db={M}*{Z}*cos(pi/9)={d}*cos({A})={d_base}" + '\n'
    temp = 10 + ((hr - d_base) / 2) + ((ha - hr) / 2)
    Exmple_Show_Canvas.create_oval(temp,temp,temp + d_base,temp + d_base,outline="#000000")
    output_str += f"基圆半径：dr={M}*{Z}*cos(pi/9)/2={d_base}/2={r_base}" + '\n'
    output_str += "-".center(50,'-')
    output_str += "渐开线方程(t取0~PI/3)".center(50 - "渐开线方程(t取0~PI/3)".__len__(),'-') + '\n'
    x_t = r_base * math.sin(T) - r_base * T * math.cos(T)
    y_t = r_base * math.cos(T) + r_base * T * math.sin(T)
    output_str += f"x_t={M}*{Z}*cos(pi/9)/2*sin(t)-{M}*{Z}*cos(pi/9)/2*t*cos(t)={r_base}*sin({T})-{r_base}*{T}*cos({T})={round(x_t,2)}" + '\n'
    output_str += f"y_t={M}*{Z}*cos(pi/9)/2*cos(t)+{M}*{Z}*cos(pi/9)/2*t*sin(t)={r_base}*cos({T})+{r_base}*{T}*sin({T})={round(y_t,2)}" + '\n'
    output_str += "-".center(50,'-') + '\n'
    output_str += "中心距".center(50 - "中心距".__len__(),'-') + '\n'
    a = M
    
    output_str += f"镜像轴偏移角度_1\n{360/Z/4}" + '\n'
    output_str += f"镜像轴偏移角度_2\n{360/Z/4*3}" + '\n'
    print(output_str)
    return output_str
    pass

def Button_CallBack():
    #output_str = "你按下了按钮")
    try:
        Show_Result.configure(state=tk.NORMAL)
        Show_Result.delete(0.0,tk.END)
        Show_Result.insert(0.0,Calc(int(M_InputBox.get()),int(Z_InputBox.get())))
        Show_Result.configure(state=tk.DISABLED)
    except ValueError:
        Show_Result.configure(state=tk.NORMAL)
        Show_Result.delete(0.0,tk.END)
        Show_Result.insert(0.0,"请输入正确的内容")
        Show_Result.configure(state=tk.DISABLED)
    
def Enter_Event(event):
    Button_CallBack()

def Escape_Event(event):
    base_window.destroy()

base_window = tk.Tk( )
base_window.title("CogsDesignCalculator")

Top_Frame = tk.Frame(base_window)
Top_Frame.pack()

Middle_Frame = tk.Frame(base_window)
Middle_Frame.pack()

Bottom_Frame = tk.Frame(base_window)
Bottom_Frame.pack()

#顶部

tk.Label(Top_Frame,text="模数 = ").pack(side=tk.LEFT,padx=5,pady=5)
M_InputBox = tk.Entry(Top_Frame)
M_InputBox.pack(side=tk.LEFT,padx=5,pady=5)
tk.Label(Top_Frame,text="齿数 = ").pack(side=tk.LEFT,padx=5,pady=5)
Z_InputBox = tk.Entry(Top_Frame)
Z_InputBox.pack(side=tk.LEFT,padx=5,pady=5)



Calc_Button = tk.Button(Top_Frame,text="计算",command=Button_CallBack).pack(side=tk.LEFT,padx=5,pady=5)

#中部


Show_Result = tk.Text(Middle_Frame,width=125,height=19)
Show_Result.configure(state=tk.DISABLED)
Show_Result.pack()

#底部
Exmple_Show_Canvas = tk.Canvas(Bottom_Frame, width=500, height=500)
Exmple_Show_Canvas.pack(padx=5,pady=5)

base_window.bind("<Return>",Enter_Event)
base_window.bind("<Escape>",Escape_Event)

base_window.mainloop()