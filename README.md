# User Access Management (UAM), Role-Based (RBAC) Models [SQLAlchemy | Flask-SQLAlchemy Ready]

## Data Models:
  - ##### User
  - ##### UserEmail
  - ##### Role
  - ##### Permission
  - ##### UserPermission
  - ##### Group
  - ##### GroupMember
  - ##### GroupPermission

## Craft Data Clean (*Object-Oriented*) Way
    from db.models import (
        User, UserEmail, UserPermission, Role, Permission
    )
    from db.models.utils import Session

    session = Session()

    dev_role = Role(name='PYTHON_DEV')
    aws_permission = Permission(name='AWS_ACCOUNT')

    session.add_all([dev_role, aws_permission])
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
        permission_id = aws_permission.id
    )

    session.add_all([emails, user_rights])
    session.commit()

## Flexible and Powerful  Querying

### 1. *RBAC*
    In [1]: session = Session()

    In [2]: session.query(
             User.first_name, User.last_name, User.username, User.avatar, 
             User.bio, Role.name, User.last_login, UserEmail.primary_email
          ).join(UserEmail).join(Role).filter(
             User.username=='premkumar30'
          ).first()._asdict()
    Out[3]: 
    {'first_name': 'Premkumar',
     'last_name': 'Chalmeti',
     'username': 'premkumar30',
     'avatar': 'https://avatars0.githubusercontent.com/u/22867776',
     'bio': 'Software Craftsman | Python | Django | Elasticsearch | VueJS | AWS',
     'name': 'PYTHON_DEV',
     'last_login': None,
     'primary_email': 'premkumar@gmail.com'}

### 2. *Group UAM*
    In [1]: from sqlalchemy import func
    
    In [2]: from db.models import Group, GroupMember
    
    In [3]: from db.models.utils import Session
    
    In [4]: session = Session()
    
    In [5]: session.query(
        Group.name, func.count(GroupMember.id).label('member_count')
    ).join(GroupMember).group_by(Group.name).first()._asdict()
    Out[5]: {'name': 'DevOps Team', 'member_count': 1}