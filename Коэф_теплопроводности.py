import string_calculation
txt = string_calculation.Calc()
name_file = 'Коэф_теплопроводности_5 произв'
t='''Определение градусо-отопительного периода в сутках:
Для стен
xx=(6+5.4)*239
x1=2000
x2=4000
y1=1,4
y2=1,8
yy=y1+(y2-y1)/(x2-x1)*(xx-x1)=2.8+(3.5-2.8)
yy=yy*0,63
Для покрытий
y1=2,0
y2=2,5
yy=y1+(y2-y1)/(x2-x1)*(xx-x1)=2.8+(3.5-2.8)
yy=yy*0,8
для чердаков
y1=1,4
y2=1,8
yy=y1+(y2-y1)/(x2-x1)*(xx-x1)=2.8+(3.5-2.8)
yy=yy*0,8
'''
txt.c1(t)
p = txt.finish(name = name_file)