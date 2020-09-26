from email.policy import default

from sqlalchemy import Column, types

from platform_actions.models import BASE, CreatedAtMixin


class HistoricalLogs(BASE, CreatedAtMixin):
    __tablename__ = "historical_logs"

    id = Column(types.Integer(), autoincrement=True, primary_key=True)
    date = Column(types.Date(), nullable=False)
    state = Column(types.Unicode(255), nullable=False)
    data_quality = Column(types.Unicode(255), nullable=True)

    deaths = Column(types.Integer(), nullable=False, default=0)
    deaths_confirmed = Column(types.Integer(), nullable=False, default=0)
    deaths_increase = Column(types.Integer(), nullable=False, default=0)
    deaths_probable = Column(types.Integer(), nullable=False, default=0)

    hospitalized = Column(types.Integer(), nullable=False, default=0)
    hospitalized_cumulative = Column(types.Integer(), nullable=False, default=0)
    hospitalized_currently = Column(types.Integer(), nullable=False, default=0)
    hospitalized_increase = Column(types.Integer(), nullable=False, default=0)

    in_icu_cumulative = Column(types.Integer(), nullable=False, default=0)
    in_icu_currently = Column(types.Integer(), nullable=False, default=0)

    negative = Column(types.Integer(), nullable=False, default=0)
    negative_increase = Column(types.Integer(), nullable=False, default=0)
    negative_testsAntibody = Column(types.Integer(), nullable=False, default=0)
    negative_testsPeopleAntibody = Column(types.Integer(), nullable=False, default=0)
    negative_testsViral = Column(types.Integer(), nullable=False, default=0)

    on_ventilator_cumulative = Column(types.Integer(), nullable=False, default=0)
    on_ventilator_currently = Column(types.Integer(), nullable=False, default=0)

    pending = Column(types.Integer(), nullable=False, default=0)
    positive = Column(types.Integer(), nullable=False, default=0)
    positive_cases_viral = Column(types.Integer(), nullable=False, default=0)
    positive_increase = Column(types.Integer(), nullable=False, default=0)
    positive_score = Column(types.Integer(), nullable=False, default=0)
    positive_tests_antibody = Column(types.Integer(), nullable=False, default=0)
    positive_tests_antigen = Column(types.Integer(), nullable=False, default=0)
    positive_tests_people_antibody = Column(types.Integer(), nullable=False, default=0)
    positive_tests_people_antigen = Column(types.Integer(), nullable=False, default=0)
    positive_tests_viral = Column(types.Integer(), nullable=False, default=0)
    recovered = Column(types.Integer(), nullable=False, default=0)

    total_test_encounters_viral = Column(types.Integer(), nullable=False, default=0)
    total_testEncounters_viral_increase = Column(types.Integer(), nullable=False, default=0)
    total_test_results = Column(types.Integer(), nullable=False, default=0)
    total_test_results_increase = Column(types.Integer(), nullable=False, default=0)
    total_tests_antibody = Column(types.Integer(), nullable=False, default=0)
    total_tests_antigen = Column(types.Integer(), nullable=False, default=0)
    total_tests_people_antibody = Column(types.Integer(), nullable=False, default=0)
    total_tests_people_antigen = Column(types.Integer(), nullable=False, default=0)
    total_tests_people_viral = Column(types.Integer(), nullable=False, default=0)
    total_tests_people_viral_increase = Column(types.Integer(), nullable=False, default=0)
    total_tests_viral = Column(types.Integer(), nullable=False, default=0)
    total_tests_viral_increase = Column(types.Integer(), nullable=False, default=0)
