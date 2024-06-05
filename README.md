# QKD-A-simulation-study


Welcome to the QKD - A Simulation Study repository! This project provides a Python-based simulation of the BB84 protocol, one of the foundational protocols for Quantum Key Distribution (QKD). The BB84 protocol uses principles from quantum mechanics to enable secure key exchange between two parties, Alice and Bob, with the ability to detect any eavesdropping attempts by a third party, Eve.

## Features
* Random Bit String Generation: Generate random binary strings to simulate the initial secret key.

* Random Basis Selection: Simulate the random selection of measurement bases (rectilinear and diagonal) for both Alice and Bob.

* Photonic State Transmission: Model the transmission of qubits (photonic states) based on the chosen bases.

* Qubit Measurement: Simulate the measurement of qubits by Bob using his randomly chosen bases.

* Basis Comparison: Publicly compare the bases used by Alice and Bob to determine which qubits can be used for the final key.

* Eavesdropping Detection: Simulate the presence of an eavesdropper (Eve) and detect discrepancies introduced by eavesdropping attempts.



## Table of contents

* [Project Structure](##Project-Structure)
* [Usage](##Usage)
* [Examples](##Examples)
* [Contributing](##Conributing)


## Project-Structure
* ```QKD_Sim.py```: Main script containing the implementation of the BB84 protocol simulation.

* ```README.md```: Documentation and description of the project.


## Usage
* Clone the repository 
  ```bash
    git clone https://github.com/your-username/qkd-simulation-study.git
    cd qkd-simulation-study

  ```

* Run the simulation
 ```bash
        python qkd_simulation.py

 ```

* Follow the Prompts 
    Enter the desired length of the bit string when prompted and observe the output to see the key generation process, measurement, and eavesdropping detection.




## Contributing 
Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.






## Acknowledgements

 - [QKD](https://pages.vassar.edu/magnes/files/2018/12/Systems-and-Photon-Polarization.pdf)
 - [Polarization-States](https://mpl.mpg.de/fileadmin/user_upload/Chekhova_Research_Group/Lecture_4_10.pdf)













