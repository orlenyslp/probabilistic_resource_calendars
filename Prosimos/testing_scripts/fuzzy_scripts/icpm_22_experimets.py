from enum import Enum

from testing_scripts.fuzzy_scripts.bayesian_optimizer import bayesian_optimization
from testing_scripts.fuzzy_scripts.event_log_operations import experiment_operations, SimulationModel


def execute_scipt():
    model = SimulationModel.BPIC12
    # model = SimulationModel.BPIC17
    # model = SimulationModel.AC_CRE
    # model = SimulationModel.CALL
    # model = SimulationModel.Loan_B
    # model = SimulationModel.Loan_U

    experiment_operations(model)
    bayesian_optimization(model)


if __name__ == "__main__":
    execute_scipt()
