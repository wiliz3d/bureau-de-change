from companies.services.company_service import get_user_membership


def is_company_admin(user):

    membership = get_user_membership(user)

    if not membership:
        return False

    return membership.role == "ADMIN"


def is_company_editor(user):

    membership = get_user_membership(user)

    if not membership:
        return False

    return membership.role == "EDITOR"


def is_company_viewer(user):

    membership = get_user_membership(user)

    if not membership:
        return False

    return membership.role == "VIEWER"