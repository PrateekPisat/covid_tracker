"""Add historical_logs table.

Revision ID: 0e8bc3970388
Revises: 
Create Date: 2020-09-26 12:30:42.001562

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0e8bc3970388"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "historical_logs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("state", sa.Unicode(length=255), nullable=False),
        sa.Column("data_quality", sa.Unicode(length=255), nullable=True),
        sa.Column("deaths", sa.Integer(), nullable=False, default=0),
        sa.Column("deaths_confirmed", sa.Integer(), nullable=False, default=0),
        sa.Column("deaths_increase", sa.Integer(), nullable=False, default=0),
        sa.Column("deaths_probable", sa.Integer(), nullable=False, default=0),
        sa.Column("hospitalized", sa.Integer(), nullable=False, default=0),
        sa.Column("hospitalized_cumulative", sa.Integer(), nullable=False, default=0),
        sa.Column("hospitalized_currently", sa.Integer(), nullable=False, default=0),
        sa.Column("hospitalized_increase", sa.Integer(), nullable=False, default=0),
        sa.Column("in_icu_cumulative", sa.Integer(), nullable=False, default=0),
        sa.Column("in_icu_currently", sa.Integer(), nullable=False, default=0),
        sa.Column("negative", sa.Integer(), nullable=False, default=0),
        sa.Column("negative_increase", sa.Integer(), nullable=False, default=0),
        sa.Column("negative_testsAntibody", sa.Integer(), nullable=False, default=0),
        sa.Column("negative_testsPeopleAntibody", sa.Integer(), nullable=False, default=0),
        sa.Column("negative_testsViral", sa.Integer(), nullable=False, default=0),
        sa.Column("on_ventilator_cumulative", sa.Integer(), nullable=False, default=0),
        sa.Column("on_ventilator_currently", sa.Integer(), nullable=False, default=0),
        sa.Column("pending", sa.Integer(), nullable=False, default=0),
        sa.Column("positive", sa.Integer(), nullable=False, default=0),
        sa.Column("positive_cases_viral", sa.Integer(), nullable=False, default=0),
        sa.Column("positive_increase", sa.Integer(), nullable=False, default=0),
        sa.Column("positive_score", sa.Integer(), nullable=False, default=0),
        sa.Column("positive_tests_antibody", sa.Integer(), nullable=False, default=0),
        sa.Column("positive_tests_antigen", sa.Integer(), nullable=False, default=0),
        sa.Column("positive_tests_people_antibody", sa.Integer(), nullable=False, default=0),
        sa.Column("positive_tests_people_antigen", sa.Integer(), nullable=False, default=0),
        sa.Column("positive_tests_viral", sa.Integer(), nullable=False, default=0),
        sa.Column("recovered", sa.Integer(), nullable=False, default=0),
        sa.Column("total_test_encounters_viral", sa.Integer(), nullable=False, default=0),
        sa.Column("total_testEncounters_viral_increase", sa.Integer(), nullable=False, default=0),
        sa.Column("total_test_results", sa.Integer(), nullable=False, default=0),
        sa.Column("total_test_results_increase", sa.Integer(), nullable=False, default=0),
        sa.Column("total_tests_antibody", sa.Integer(), nullable=False, default=0),
        sa.Column("total_tests_antigen", sa.Integer(), nullable=False, default=0),
        sa.Column("total_tests_people_antibody", sa.Integer(), nullable=False, default=0),
        sa.Column("total_tests_people_antigen", sa.Integer(), nullable=False, default=0),
        sa.Column("total_tests_people_viral", sa.Integer(), nullable=False, default=0),
        sa.Column("total_tests_people_viral_increase", sa.Integer(), nullable=False, default=0),
        sa.Column("total_tests_viral", sa.Integer(), nullable=False, default=0),
        sa.Column("total_tests_viral_increase", sa.Integer(), nullable=False, default=0),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("historical_logs")
