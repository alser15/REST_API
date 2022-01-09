from entity.agencies import Agencies
from entity.arrival_estimates import ArrivalEstimates
import pytest


class TestSuiteAgencies:

    file = 'data_agencies.json'

    @pytest.mark.parametrize('open_file', [file], indirect=True)
    def test_success_response_code(self, open_file):
        agencies = Agencies(open_file)
        agencies.validate_response_status_code()

    @pytest.mark.parametrize('open_file', [file], indirect=True)
    def test_validate_response_json(self, open_file):
        agencies = Agencies(open_file)
        agencies.validate_response_json()


class TestArrivalEstimates:

    file = 'data_arrival_estimates.json'

    @pytest.mark.parametrize('open_file', [file], indirect=True)
    def test_success_response_code(self, open_file):
        arrival_estimates = ArrivalEstimates(open_file)
        arrival_estimates.validate_response_status_code()

    @pytest.mark.parametrize('open_file', [file], indirect=True)
    def test_validate_response_json(self, open_file):
        arrival_estimates = ArrivalEstimates(open_file)
        arrival_estimates.validate_response_json()
