import pymysql

Database = pymysql.connect(host="localhost", user="root",
                           password="123456", charset="utf8")

cursor = Database.cursor()

# cursor.execute('CREATE DATABASE manager;')

cursor.execute('USE manager;')

# cursor.execute('CREATE TABLE member('
#                'id INT(100) NOT NULL AUTO_INCREMENT,'
#                'email VARCHAR(30) NOT NULL,'
#                'password VARCHAR(16) NOT NULL,'
#                'name VARCHAR(20) NOT NULL,'
#                'age INT(100) NOT NULL,'
#                'information VARCHAR(100) NULL,'
#                'PRIMARY KEY(id)); ')

# add = "INSERT INTO member(email, password, name, age, information) VALUES('NONE@gmail.com', 'NONE', 'NONE', 0,'NONE');"
# for i in range(20):
#     cursor.execute(add)


def administrator():
    check_sql2 = "SELECT * FROM member;"
    cursor.execute(check_sql2)
    result2 = cursor.fetchall()

    print("!관리자페이지!")
    print("DATABASE(manager)-TABLE(member)-DATA값 : ")
    for i in result2:
        print(i)

    exit(0)


email = ""
password = ""
name = ""
age = ""
information = ""
sl = "INSERT INTO member(email, password, name, age, information) VALUES(%s, %s, %s, %d, %s)".format(email, password,
                                                                                                     name, age,
                                                                                                     information)


def check(hl):
    check_sql = "SELECT * FROM member;"
    cursor.execute(check_sql)

    result = cursor.fetchall()

    if hl == "login":
        for data in result:
            if email == data[1] and password == data[2]:
                return "1"
            else:
                pass

    elif hl == "email":
        for data in result:
            if email == data[1]:
                return "1"
            else:
                pass

    elif hl == "name":
        for data in result:
            if name == data[3]:
                return "1"
            else:
                pass

    return "0"


while True:
    print("종료하려면 exit를 입력하세요")
    login = input("로그인 하시겠습니까? [ y / n ] : ")
    if login == 'y':
        while True:
            email = input("email을 입력하세요 : ")
            if email == "":
                pass
            elif email != "":
                break

        while True:
            password = input("password를 입력하세요 : ")
            if email == "":
                pass
            elif email != "":
                break

        h = "login"
        duplication = check(h)
        if duplication == "1":
            print("로그인 완료!")
            administrator()

        elif duplication == "0":
            print("로그인 실패!")
            pass

    elif login == 'n':
        while True:
            select = input("회원가입 하시겠습니까? [ y / n ] : ")
            if select == 'y':
                while True:
                    email = input("email을 입력하세요(필수) : ")
                    email2 = email
                    if email == "":
                        pass
                    elif email != "":
                        h1 = "email"
                        duplication = check(h1)
                        if duplication == "0":
                            break
                        elif duplication == "1":
                            print("이메일 중복")
                            pass

                while True:
                    password = input("password를 입력하세요(필수) : ")
                    password2 = password
                    if password == "":
                        pass
                    elif password != "":
                        break

                while True:
                    name = input("name을 입력하세요(필수) : ")
                    name2 = name
                    if name == "":
                        pass
                    elif name != "":
                        h2 = "name"
                        duplication = check(h2)
                        if duplication == "0":
                            break
                        elif duplication == "1":
                            print("닉네임 중복")
                            pass

                while True:
                    age = input("나이를 입력하세요(필수) : ")
                    age2 = age
                    if age == "":
                        pass
                    elif age != "":
                        break

                information = input("정보: ")
                if information == "":
                    information = "NONE"

                add_peopel = "INSERT INTO member(email,password,name,age,information) VALUES('{0}','{1}','{2}',{3},'{4}');".format(email2, password2, name2, age2, information)
                cursor.execute(add_peopel)
                Database.commit()

                print("회원가입 완료!")
                break

            elif select == 'n':
                break

            else:
                pass
    elif login == 'exit':
        exit(0)
    else:
        pass


Database.commit()
Database.close()
