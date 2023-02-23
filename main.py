from colorama import init
from colorama import Back, Fore, Style
h=''
while True:
    print(Fore.GREEN+'Доступные операции')
    print('1.Добваить машину')
    print('2.Посмотреть каталог')
    print('3.Редактировать машину')
    print('4.Удалить машину')
    print('5.Выйти')
    action=int(input('Введите операцию '))
    if action==1:
        while True:
            number=int(input('Введите номер машины '))
            if number>=10000 or number<=99:
                print('Недопустимое количество символов ')
                break
            model=input('Введите модель машины ')
            if len(model)>=21:
                print('Недопустимое количество символов')
                break
            color=input('Введите цвет машины ')
            if color.count('0')>=1 or color.count('1')>=1 or color.count('2')>=1 or color.count('3')>=1 or color.count('4')>=1 or color.count('5')>=1 or color.count('6')>=1 or color.count('7')>=1 or color.count('8')>=1 or color.count('9')>=1:
                print('Недопустимые символы ')
                break
            h=h+str(number)+'_'+model+'_'+color+'*'
            a=input('Нужно добавить еще 1 машину? yes/no ')
            if a=='no':
                break
    elif action==2:
        s=h.replace('_','\t')
        print(s.replace('*','\n'))
    elif action==3:
        while True:
            p=input('Введите машину которую хотите изменить ')
            p+='*'
            popa,iop=map(str, input('Старое/новое значение ').split('/'))
            jop=p.replace(popa,iop)
            h=h.replace(p,jop)
            dfs=input('Редактировать еще 1 элемент ')
            if dfs=='no':
                break
    elif action==4:
        while True:
            pty=input('Введите машину которую хотите удалить ')
            pty+='*'
            h=h.replace(pty,'')
            dfsu=input('Удалить еще 1 машину ')
            if dfsu=='no':
                break
    elif action==5:
        break
    elif action>=0 or action<6:
        print('Такой операции нет')
        break