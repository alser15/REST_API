from entity.agencies import Agencies
from entity.arrival_estimates import ArrivalEstimates
import json


class TestSuiteAgencies:

    with open('C:/Users/alser15/PycharmProjects/pythonProject/data/data_agencies.json') as f:
        file = json.load(f)

    def test_success_response_code(self):
        test = Agencies(TestSuiteAgencies.file['urls']["url"],
                        TestSuiteAgencies.file["header"], TestSuiteAgencies.file["params"])
        test.validate_response_status_code()

    def test_validate_response_json(self):
        test = Agencies(TestSuiteAgencies.file['urls']["url"],
                        TestSuiteAgencies.file["header"], TestSuiteAgencies.file["params"])
        test.validate_response_json()


class TestArrivalEstimates:

    with open('C:/Users/alser15/PycharmProjects/pythonProject/data/data_arrival_estimates.json') as f:
        file = json.load(f)

    def test_success_response_code(self):
        test = ArrivalEstimates(TestArrivalEstimates.file['urls']["url"],
                                TestArrivalEstimates.file["header"], TestArrivalEstimates.file["params"])
        test.validate_response_status_code()

    def test_validate_response_json(self):
        test = ArrivalEstimates(TestArrivalEstimates.file['urls']["url"],
                                TestArrivalEstimates.file["header"], TestArrivalEstimates.file["params"])
        test.validate_response_json()