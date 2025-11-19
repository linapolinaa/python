#структура в которой вамилия сотрудника, должность и зп ю можно добав, удалить, поменять должность и зп.
sotrudniki=[{"username":"иванов","dolzhnost":"продавец","zp":"1000"},
            {"username":"петров","dolzhnost":"кассир","zp":"1500"},
            {"username":"сидоров","dolzhnost":"менеджер","zp":"1030"},
            {"username":"соколов","dolzhnost":"директор","zp":"4000"},
            {"username":"игнатьев","dolzhnost":"консультант","zp":"1500"}]

def add():
    new_username=input("введите фамилию нового сторудника ")
    new_dolzhnost=input("введите его должность ")
    new_zp=input("введите его зп ")
    sotrudnik={"username": new_username,"dolzhnost": new_dolzhnost,"zp": new_zp}
    sotrudniki.append(sotrudnik)

def ydalit():
    ydalit=str(input("введите фамилию для удаления "))
    for sotrudnik in sotrudniki:
        if ydalit in sotrudnik:
            del(sotrudnik[ydalit])

def ndolzh():
    usernamed=input("введите фамилию для изменения должности ")
    new_dolzhnost=input("введите новую должность ")
    for sotrudnik in sotrudniki:
         if usernamed in sotrudnik:
             sotrudnik[usernamed]=new_dolzhnost

def nzp():
    usernamez=input("введите фамилию для изменения зп ")
    new_zp=input("введите новую зп ")
    for sotrudnik in sotrudniki:
         if usernamez in sotrudnik:
             sotrudnik[usernamez]=new_zp            


while True:
    choise=input("выберите действие:" \
    " 1-добавить нового" \
    " 2-удалить" \
    " 3-изменить должность" \
    " 4-изменить зп" \
    " 5-вывести всех" \
    " 6-выход")     

    if choise=="1":
        add()

    elif choise=="2":
        ydalit()

    elif choise=="3":  
        ndolzh()

    elif choise=="4": 
        nzp()

    elif choise=="5":  
        for sotrudnik in sotrudniki:
            print(f"{sotrudnik['username']} {sotrudnik['dolzhnost']},{sotrudnik['zp']}")  

    elif choise=="6":  
        break           
