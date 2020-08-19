import datetime as dt

__author__ = 'premkumar30'


def load_data():
    from db.models import (
        User, UserEmail, UserPermission, 
        Role, Permission, Group, GroupMember, GroupPermission
    )
    from db.models.utils import Session

    session = Session()

    dev_role = Role(name='PYTHON_DEV')
    intellij_ide = Permission(name='pycharm')

    session.add_all([dev_role, intellij_ide])
    session.commit()

    prem = User(
        first_name = 'Premkumar',
        last_name = 'Chalmeti',
        username = 'premkumar30',
        avatar = 'https://avatars0.githubusercontent.com/u/22867776',
        bio = 'Software Craftsman | Python | Django | Elasticsearch | VueJS | AWS',
        role = dev_role.id,
        password = 'PBKDF2uuid5AWSPrem112'
    )

    session.add(prem)
    session.commit()

    emails = UserEmail(user_id=prem.id, primary_email='premkumar@gmail.com')

    user_rights = UserPermission(
        role_id = dev_role.id,
        permission_id = intellij_ide.id
    )

    session.add_all([emails, user_rights])
    session.commit()

    devops = Group(name='DevOps Team')
    aws_permission = Permission(name='AWS_ACCOUNT')

    session.add_all([devops, aws_permission])
    session.commit()

    devops_member = GroupMember(
        group_id = devops.id,
        user_id = prem.id
    )
    group_rights = GroupPermission(
        group_id = devops.id,
        permission_id = aws_permission.id
    )
    session.add_all([devops_member, group_rights])
    session.commit()



if __name__ == "__main__":
    from add_base_path import set_path
    set_path()
    load_data()
