import sqlite3


# написать функцию запроса списка преподавателей

def get_teachers():
    con = sqlite3.connect('timeTable.db')
    cur = con.cursor()
    result = cur.execute(
        "SELECT fullname FROM teachers"
    ).fetchall()
    result = [item[0] for item in result]
    return result


def get_groups():
    con = sqlite3.connect('timeTable.db')
    cur = con.cursor()
    result = cur.execute(
        "SELECT title FROM groups"
    ).fetchall()
    result = [item[0] for item in result]
    return result


def get_timetable_by_group(group):
    con = sqlite3.connect('timeTable.db')
    cur = con.cursor()
    id_gr = cur.execute(
        f"SELECT id FROM groups WHERE title='{group}'"
    ).fetchone()[0]
    print(id_gr)
    subjects = cur.execute(
        f'SELECT * FROM subjects WHERE "group"={id_gr}'
    ).fetchall()
    print(subjects)

# Так мы получаем все записи из БД:subjects. Нужно их преобразовать в матрицу. Там где уроков нет, можно поставить 0


get_timetable_by_group('11 ИНЖ-1')
