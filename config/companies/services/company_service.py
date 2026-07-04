from companies.models import CompanyMembership


def get_user_membership(user):
    """
    Returns the user's company membership.
    """

    return (
        CompanyMembership.objects
        .select_related("company")
        .filter(user=user)
        .first()
    )


def get_user_company(user):
    """
    Returns the company the user belongs to.
    """

    membership = get_user_membership(user)

    if membership:
        return membership.company

    return None