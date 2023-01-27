from .models import Subscription
from .selectors import get_subscription_by_case_id


def create_subscription_from_docket(docket):
    """
    Creates a new Subscription record for a given Docket from the CL API.
    Call get_case_from_cl() to get a Docket first.
    """
    docket_name = docket["case_name"]
    docket_number = docket["docket_number"]

    cl_docket_id = docket["id"]
    cl_court_id = docket["court_id"]

    pacer_court_id = docket["court_id"]
    pacer_case_id = docket["pacer_case_id"]

    case_result = get_subscription_by_case_id(case_id=pacer_case_id)

    if case_result:
        return case_result

    subscription = Subscription.objects.create(
        docket_name=docket_name,
        docket_number=docket_number,
        cl_docket_id=cl_docket_id,
        cl_court_id=cl_court_id,
        pacer_court_id=pacer_court_id,
        pacer_case_id=pacer_case_id,
    )

    return subscription
