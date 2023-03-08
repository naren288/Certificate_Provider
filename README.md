# Usage of Self-signed certificate provider

This python script simplifies the generation of self-signed certificates that we use in our development environments

## Prerequisites

The script expects that you have already generated your CA certificate and is placed in the same directory as that of main.py <br>
The name of the CA key to be ca.key <br>
The name of the CA cert to be cacert.crt <br> <br>

Update the server.cnf with the default values for Company, department, Country etc., except for Common Name. A placeholder - <COMMON_NAME> is added for the script to find and replace depending upon the provided value. <br>
**NOTE:** Once the script is executed, it will take the default values provided in the server.cnf

The script should also be executed in an environment that has openssl installed.

### Using the python script

Run the command **python main.py** and you will be prompted to enter the Common name for your certificate. <br>
Enter the CN and press enter. <br>
The certificates will be generated in a new directory with the same name as that of your Common name.

### Verification of the certificates

Run the command **openssl x509 -text -noout -in server.crt**
