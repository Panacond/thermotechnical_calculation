# файл дополнительных формул
import string_calculation
txt = string_calculation.Calc()
name_file = 'Проверка сопротивления'
def func(t ):
    t = t.replace('\t', '/')
    summ = '''Сумма сопротивлений составит (м^2 \\times °C):
\sumR_s='''
    text_list = t.split('\n')
    n = 1
    check = 'Термическое сопротивление отдельных элементов (м^2 \\times°C):'
    numer_i = len(text_list)
    for i in range(len(text_list)):
        
        if text_list[i] == check:
            numer_i = i
        if i > numer_i and i < len(text_list)-1:
            text_list[i]= 'R_s'+ str(n) +'=' + text_list[i]
            if n != 1:
                summ += '+'
            summ += 'R_s'+ str(n)
            n +=1
    t = '\n'.join(text_list)
    t += summ
    txt.c1(t, 60)
    p = txt.finish(name = name_file)
    t = '''
Общее термическое сопротивление составит (м^2 \\times°C):
R_0=1/8.7+\sumR_s+1/23
k=R_tr/R_0
'''
    txt.c1(t)
    if txt.numer['k'] < 1:
        text_i='''R_0={0} > R_0^тр = {1} (м^2 \\times °С)/Вт
Условие выполняется.
ВЫВОД. Наружные ограждающие конструкции удовлетворяют требованиям в части тепловой защиты. Коэффициент использования k={2}'''
    else:
        text_i='''R_0={0} < R_0^тр = {1} (м^2 \\times °С)/Вт
Условие не выполняется.
ВЫВОД. Наружные ограждающие конструкции не удовлетворяют требованиям в части тепловой защиты. Коэффициент использования k={2}'''
    text_i = text_i.format(str(txt.numer['R_0']),str(txt.numer['R_tr']),str(txt.numer['k']))
    txt.rezult += text_i
    return txt
def file_revrite():
    t = string_calculation.read_file(name_file)
    t = t.replace('\tR_s',';\tR_s')
    t = t.replace('\nR_s',';\tR_s')
    t = t.replace(';\tR_s1','\nR_s1')
    t = t.replace('\t','    ')
    string_calculation.write_file(name_file, t)