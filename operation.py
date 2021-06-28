def check_login(db_obj, email, password):
    for i in range(len(db_obj)):
        db_str = str(db_obj[i])
        db_list = db_str.split(':')
        print(db_list)
        if (email == db_list[1]):
            if(password == db_list[2]):
                return 1,db_list[0]
            return 2,""
    return 0,""

def get_history(db_obj, email):
    for i in range(len(db_obj)):
        db_str = str(db_obj[i])
        db_list = db_str.split(':')
        if (db_list[1] == email):
            temp = db_list[3]
    print(temp)
    if temp == 'NULL':
        return None
    else:
        data = []
        temp = temp.split(":")
        for i in temp:
            kv = i.split('-')
            
        return data
