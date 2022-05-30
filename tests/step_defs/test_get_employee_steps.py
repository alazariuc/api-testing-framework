import requests
import logging
from pytest_bdd import scenarios, given, when, then, parsers

from tests.step_defs.conftest import EMPLOYEE_API_BASE_URL

scenarios('../features/get_employee.feature')
logger = logging.getLogger(__name__)


@given(parsers.parse('user sends "{method}" request to endpoint "{endpoint}"'), target_fixture='response')
def user_sends_request(method, endpoint):
    url = EMPLOYEE_API_BASE_URL + endpoint
    logger.debug('Sending "%s" request to url: "%s"', method, url)

    response = requests.request(method, url)
    return response


@then(parsers.parse('response code "{code:d}" is received'))
def receive_response_code(code, response):
    assert response.status_code == code
