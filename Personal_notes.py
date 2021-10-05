import time

act=''
note=[]

print('Приложение "Заметки"')

def show():
    if note==[]:
        print('Заметок нет')
    else:
        for i,v in enumerate(note,1):
            print(i,v,sep='. ',end='')

def rewr():
    with open('zametki.txt','w') as f:
        for i in note:
            f.write(i)

def pause():
    time.sleep(0.6)

try:
    with open('zametki.txt','r') as r:
        for i in r:
            note.append(i)
except:
    rewr()

while act!='выход':
    act=input('Что нужно?\nПосмотреть/Создать/Редактировать/Поменять местами/Отметить выполненной/Изменить положение/Удалить/Очистить/Выход ')
    act=act.lower()
    if act=='создать':
        rep=''
        while rep!='всё':
            z=input('Вводи заметку: ')
            note.append(z+'\n')
            if len(note)>1:
                doneK=-2
                doneCheck=note[doneK]
                if '|' in doneCheck:
                    while '|' in doneCheck:
                        doneK=doneK-1
                        doneCheck=note[doneK]
                    note.insert(doneK+1,note[-1])
                    note.pop(-1)
            rewr()
            rep=input('Ещё/Всё? ')
            rep=rep.lower()
        show()
    elif act=='посмотреть':
        show()
    elif act=='удалить':
        try:
            del note[int(input('Какую по счёту заметку удалить? '))-1]
            rewr()
            print('Заметка удалена')
            pause()
            show()
        except:
            print('У тебя не так много заметок')
    elif act=='очистить':
        note.clear()
        o=open('zametki.txt','w')
        o.close()
        print('Все заметки удалены')
        pause()
    elif act=='редактировать':
        try:
            editInd=int(input('Какую по счёту заметку хочешь изменить? '))-1
            note[editInd]=input('Вводи новый текст заметки: ')+'\n'
            rewr()
            print('Заметка изменена')
            pause()
            show()
        except:
            print('У тебя не так много заметок')
    elif act=='поменять местами':
        try:
            p1=int(input('Номер первой заметки для замены положения: '))-1
            p2=int(input('Номер второй заметки для замены положения: '))-1
            note[p1],note[p2]=note[p2],note[p1]
            rewr()
            print('Положение изменено')
            pause()
            show()
        except:
            print('Кажется, ты где-то ошибся с номером')
    elif act=='изменить положение':
        try:
            p1=int(input('Номер заметки для замены положения: '))-1
            p2=int(input('На какое место? '))-1
            if p1>p2:
                note.insert(p2,note[p1])
                note.pop(p1+1)
            elif p1<p2:
                note.insert(p2+1,note[p1])
                note.pop(p1)
            rewr()
            print('Положение изменено')
            pause()
            show()
        except:
            print('Кажется, ты где-то ошибся с номером')
    elif act=='отметить выполненной':
        try:
            ov=int(input('Номер заметки для отметки "Выполнено": '))-1
            sl=''
            for i in range(len(note[ov])-1):
                sl=sl+note[ov][i]
            if len(note)==ov+1:
                dubl=note[-1]
                if not '|' in note[-1]:
                    note[-1]=sl+' | ВЫПОЛНЕНО\n'
                    print('Отмечено')
                else:
                    print('Заметка и так отмечена')
            else:
                if not '|' in note[ov]:
                    note[ov]=sl+' | ВЫПОЛНЕНО\n'
                    note.append(note[ov])
                    note.pop(ov)
                    print('Отмечено')
                else:
                    print('Заметка и так отмечена')
            rewr()
            pause()
            show()
        except:
            print('У тебя не так много заметок')
    else:
        print('Ответ неясен')
        
print('До скорой встречи!')
time.sleep(1.3)
