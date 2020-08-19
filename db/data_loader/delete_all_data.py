import datetime as dt

__author__ = 'premkumar30'


def clean_data():
    from db.models.utils import Session
    from db.models import (
        User, UserEmail, UserPermission, 
        Role, Permission, Group, GroupMember, GroupPermission
    )

    session = Session()

    for table in [UserEmail, UserPermission, User, GroupPermission, Permission, Role, GroupMember, Group]:
        session.query(table).delete()
        session.commit()
        print(table, 'data deleted')


if __name__ == "__main__":
    from add_base_path import set_path
    set_path()
    clean_data()
