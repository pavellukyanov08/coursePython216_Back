import os

from sqlalchemy import not_, or_, text
from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.students import Student
from models.groups import Group
from models.lessons import Lesson, association_table

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    # print(session.query(Lesson).all())

    # for group in session.query(Group).all():
    #     print(group.group_name, group.lessons)

    # print(session.get(Lesson, 3))
    # for lesson in session.query(Lesson).filter(or_(Lesson.id < 3, Lesson.lesson_title.like('Ф%'))):
    #     print(lesson)

    # for lesson, gr in session.query(Lesson.lesson_title, Group.group_name).all():
    #     print(lesson, gr)
    # print(session.query(Lesson).filter(Lesson.id.in_([1, 2, 3])).all())
    # print(session.query(Lesson).filter(Lesson.id.in_([1, 2, 3])).all())

    # print(session.query(Student).filter(not_(Student.age.between(18, 20))).all())
    # for it in session.query(Student).filter(text('surname like "М%"')):
    #     print(it)