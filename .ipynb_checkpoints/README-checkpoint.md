# Capturing and Analyzing Transistor Curves for OFET Mobility

### Keithley-IV-Sweep
Python (PyVisa) script for IV (Current-Voltage) measurements on a Keithley 2400 (GPIB/SCIP communication).

Instructions:

  1. Install the necessary Python libraries and drivers (list below)

  2. Place the KeithleyIVSweep.py, KeithleyIVSweepFixedGate.py, and/or KeithleyGateSweepFixedGate.py files in your home (or current Python) directory.
  
  3. From the command line, run one of the following commands (depending on file):
  
    a. 'python KeithleyIVSweep.py startV stopV stepV outputfile direction' 
    b. 'python KeithleyIVSweepFixedGate.py startV stopV stepV gateV outputfile direction'
    c. 'python KeithleyGateSweepFixedDrain.py startgateV stopgateV stepgateV drainV outputfile direction'
  
  4. For example, a gate from -20 V to 20 V with a step voltage of 1 V and drain voltage of 0.5 V would be obtained by running 'python KeithleyGateSweepFixedDrain.py -20 20 1 0.5 Hello.txt up' where the output text file named Hello.txt would be created and stored in your home (or current Python) directory.
  
  5. you can also use the jupyter notebook file: "2400 Keithley Mobility.ipynb" which has built in plotting and analysis features. 
  

### List of all the required programs, drivers and packages required for the succesful communication and control of the Keithley 2400 Duo in order to conduct Semiconductor mobility measurements.

    1. python installation and the following packages. These are easily installed with "pip install package"
        a. pyvisa
        b. scipy
        c. matplotlib
        d. numpy
    3. VISA implementation: https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html#346210
    4. NI GBIP driver: https://www.ni.com/en-us/support/downloads/drivers/download.ni-488-2.html#345631
    
### Changing parameters and controlling the Keithley from the command line

You can modify your version of the python scripts to do different things and even run the instruments from the command line. Start by taking a look at the existing scripts and understanding how the instruments and the VISA driver communicate. Then, read through the this manual (http://research.physics.illinois.edu/bezryadin/labprotocol/Keithley2400Manual.pdf) which will indicate other commands that the keithley will accept and in the form to deliver them. 
    
### Design for automated characteristic curves capture!

The system should take a simple input involving the material and the particular information about the transitor fabrication including:

    1. active layer thickness
    2. channel size (shouldnt change)
    3. Self-assembled monoalyer material
    4. annealing time and temperature
    5. Casting solvent
    
The system should take in these variables, and then initialize a program that generates the requireed curves and saves them in a folder along with a text file that contains the transistor information. The raw data will sit in .txt files titled only by the number of trial and the type of curve that it is, along with voltage parameters. The anakysis will be performed with another program. 

### triggering

Upon entering the information and initializing the system, each curve is triggered externally somehow, and terminated with a command!
    
