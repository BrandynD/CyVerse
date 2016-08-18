#!/bin/bash

input_ped="${inputPed}"
output_ped="${outputPed}"

python ./RidgeRegression/RidgePredict.py --input $input_ped --output $output_ped
