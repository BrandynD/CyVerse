#!/bin/bash

input_ped="${inputPed}"
output_ped="${outputPed}"

echo $input_ped

python ./RidgeRegression/RidgePredict.py --input $input_ped --output $output_ped
