from sqlalchemy.orm import Session

from app.models.user_model import RoleModel, PermissionModel
from app.services.user_service import create_user
from app.schemas.user_schema import UserCreateSchema


def seed_db(db: Session):
    # add permissions
    print("adding permissions..")
    create_event = PermissionModel(name="create_event")
    update_event = PermissionModel(name="update_event")
    delete_event = PermissionModel(name="delete_event")
    db.add_all([create_event, update_event, delete_event])
    print("[OK] permissions added..")

    # add roles
    print("adding roles..")
    admin_role = RoleModel(name="admin")
    user_role = RoleModel(name="user")
    db.add_all([admin_role, user_role])
    print("[OK] roles added..")

    # assign permissions to roles
    print("assigning permissions to roles..")
    admin_role.permissions.extend([create_event, update_event, delete_event])
    print("[OK] permissions assigned to roles..")

    db.commit()


def add_user(db: Session, role: str, user: UserCreateSchema):
    print(f"adding user - role: {role}, user: {user}")
    create_user(db, user, role)
    db.commit()
