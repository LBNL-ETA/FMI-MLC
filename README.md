# FMI-MLC
#### Functional Mock-up Interface - Machine Learning Center
---

This package simplifies the use of Functional Mock-Up Interface compliant models for Machine Learning and Simulation purposes.

## General
The interfacing of simulation models with machine learning algorithms such as [reinforcement learing](https://en.wikipedia.org/wiki/Reinforcement_learning) is complex and requires custom software bindings. FMI-MLC seeks to bridge this gap by employing the [Funcitional Mock-Up Interface (FMI)](https://fmi-standard.org/), an industry standard to export and interface with simulation models, and [OpenAI's Gym](https://fmi-standard.org/), a standard Python interface for machine learning.

*Please note that the FMI-MLC package is still under active development. Please open an issue for specific questions*

## Getting Started
The following link permits users to clone the source directory containing the [FMI-MLC](https://github.com/LBNL-ETA/FMI-MLC) package. The package can then be installed using `pip install .` within the directory. While a user can provide a custom FMU handler, it is recommended to also install [PyFMI](https://github.com/modelon-community/PyFMI). FMI-MLC will default to PyFMI if no custom handler is provided.

## Example
To illustrate the functionality of FMI-MLC, example Jupyter notebooks can be found [here](examples).

[Exmaple of fmi_gym](examples/Test_fmi_gym.ipynb)

COMING SOON: [Reinforcement Learning with FMI-MLC](examples/COMINGSOON.ipynb)

## License
Functional Mock-up Interface - Machine Learning Center (FMI-MLC) Copyright (c) 2021, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.

If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at IPO@lbl.gov.

NOTICE. This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit others to do so.

## Cite
To cite the FMI-MLC package, please use:

*Gehbauer, Christoph, Rippl, Andreas and Lee, Eleanor. 2021. Advanced Control of Dynamic Facades and HVAC with Reinforcement Learning based on standardized co-Simulation. Building Simulation 2021.*