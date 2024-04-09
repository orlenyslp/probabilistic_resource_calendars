# probabilistic_resource_calendars

This repository serves as a reproducibility package, enabling the execution of experiments outlined in the research papers: I) "Discovery and Simulation of Business Processes with Probabilistic Resource Availability Calendars" and II) "Business Process Simulation: Probabilistic Modeling of Intermittent Resource Availability and Multitasking Behavior"

It includes the necessary source code, datasets, models, and execution guidelines, joining the four necessary systems/libraries into one repository for convenience. The extended systems referenced in the papers are [Simod](https://github.com/AutomatedProcessImprovement/Simod), [pix-framework](https://github.com/AutomatedProcessImprovement/pix-framework) and [Prosimos](https://github.com/AutomatedProcessImprovement/Prosimos), while the [log-distance-measures](https://github.com/AutomatedProcessImprovement/log-distance-measures) library provides the metrics used in the evaluation. For the most recent updates and full functionalities, please follow the provided links to access the source codes.

## Requirements
* Python 3.9
* Use [Poetry](https://python-poetry.org/) and [Poetry Multiproject Plugin](https://pypi.org/project/poetry-multiproject-plugin/) for building, installing, and managing Python dependencies.

## Required Steps

* Install the Poetry and Poetry Multiproject Plugin by following the instructions in the links in the Requirements subsection above. Once installed, to add the pluggin run the command: __poetry self add poetry-multiproject-plugin__.
  
* The experiments are split into two folders. The folder ``Resource_Availability`` contains the evaluation of probabilistic calendars (paper I), and the folder ``Multitasking`` corresponds to the assessment of probabilistic multitasking capacity (paper II).

* Clone this repository. Move to the folder: _/probabilistic_resource_calendars/Resource_Availability/Prosimos/_ in your command-line shell to execute the probabilistic calendars experiments or to the folder _/probabilistic_resource_calendars/Multitasking/Prosimos/_ to execute the probabilistic multitasking experiments.

* Install the dependencies by running the following commands: __poetry build-project__ and  __poetry install__. The latest will create the environment in the current folder with all the dependencies used to run the experiments script.

* Run the follwoing scripts: _/probabilistic_resource_calendars/Resource_Availability/Prosimos/testing_scripts/fuzzy_scripts
/icpm_22_experimets.py_ to execute the probabilistic calendars experiments or _/probabilistic_resource_calendars/Multitasking/Prosimos/testing_scripts/multitasking_scripts/multitasking_experiments.py_ to execute the probabilistic multitasking experiments.

## Checking the Results

### Probabilistic Calendars Results

The script first splits the event log and displays, respectively, the number of traces and events in the training and testing datasets in the shell. Then, it runs the __N-Crisp__ approach, followed by the 30 iterations for tuning the hyperparameters of the methods __C-Crisp__ and __Probabilistic__ by a Bayesian Optimization approach. At each iteration, the shell displays the execution times of the discovery approach and the simulation, respectively. Besides,  it shows the assessed values of the metrics: __MMR__ (mismatch resources), __RED__ (Relative Event Distribution), and __CTD__ (Cycle Time Distribution).

In the case of the synthetic evaluation, the script runs the execution of the four calendar types for each of the two models, __Loan-B__ and __Loan-U__. If the selected dataset is __Loan-B__, the script will run the experiments for logs B-24, B-8, B-8/4, and B-24/A, in that order. If the selected dataset is __Loan-U__, the script will run the experiments for logs U-24, U-8, U-8/4, and U-24/A, in that order.

Aditionally, the training, testing, and simulated event logs can be found in the folder: _/probabilistic_resource_calendars/Resource_Availability/Prosimos/testing_scripts/assets
/fuzzy_calendars/_. The script produces all the files in the folder labeled with the names of the corresponding dataset. The dataset folder will also contain the BPMN model and the JSONs with the discovered simulation parameters.

The script, by default, runs the experiments corresponding to the dataset _BPIC12_. To run any other dataset, remove the corresponding comment on lines 8-13 in the script code and re-run the script, e.g.,:

model = SimulationModel.BPIC12

\# model = SimulationModel.BPIC17

\# model = SimulationModel.AC_CRE

\# model = SimulationModel.CALL

\# model = SimulationModel.Loan_B

\# model = SimulationModel.Loan_U

```
Please note that the script only executes one dataset at a time. Therefore, if you uncomment multiple datasets, it will only perform the last one. 
```

### Probabilistic Multitasking Results

The script runs the 30 iterations for tuning the hyperparameters of the methods __S-Prob__, __G-Mult__ and __L-Mult__ by a Bayesian Optimization approach. At each iteration, the shell displays the execution times of the discovery approach and the simulation, respectively. Besides,  it shows the assessed values of the metrics: __MMR__ (mismatch resources), __RED__ (Relative Event Distribution), and __CTD__ (Cycle Time Distribution). The full experimental execution results obtained in the evaluation of the multitasking capacity can be checked in the file: _/probabilistic_resource_calendars/Multitasking/Multitasking-Experiments-Full-Execution-Log.txt_. Note that in the results, the __S-Prob__ approach is labeled as __ModelType.SEQUENTIAL__.

The script executes the datasets in the following order: __Loan-B-24__, __Loan-U-24__, __Loan-B-8__, __Loan-U-8__,  __Loan-B-8/4__, __Loan-U-8/4__, __Loan-B-24/A__, __Loan-U-24/A__, __GOV__, __POC__, __AC-CRD__, and __WK-ORD__.

Additionally, the training, testing, and simulated event logs can be found in the folder: _/probabilistic_resource_calendars/Multitasking/Prosimos/testing_scripts/assets/multitasking/_. The script produces all the files in the folder labeled with the names of the corresponding dataset. The dataset folder will also contain the BPMN model and the JSONs with the discovered simulation parameters.

