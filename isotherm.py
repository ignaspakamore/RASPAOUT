#!/usr/bin/env python
import glob
import re
import sys



_input = glob.glob("*.data")



def _iso_point(_input):
    _output = open("isotherm_out.csv", "w")
    _output.write('Pressure (atm)' + ',' + 'Amount adsorbed (cm^3 (STP)/gr framework)' + ',' +'Error (+/-)'+','+'\n')
    for fle in _input:
        with open(fle) as f:
              for line in f:
                  if 'Average loading absolute [cm^3 (STP)/gr framework]' in line:
                      amount_adsorbed = line.split('Average loading absolute [cm^3 (STP)/gr framework]')[1]
                      amount_adsorbed = amount_adsorbed.split('+/-')[0].strip()


                      error = line.split('+/-')[1]
                      error = error.split('[-]')[0].strip()

                      fle = fle.rsplit('_', 1)[1]
                      fle = fle.split(".data")[0]

                      _output.write(fle +','+ amount_adsorbed+',' + error +','+ '\n')



def _pressure(_input):
    for i in _input:
        a = str(_input)
        for s in a:
          re.findall(r'-?\d+\.?\d*', a)



def extract_points(points_string):
    for string in points_string:
        a = str(points_string)
        d = re.findall("\d+\.\d+", a)
        points.append(d)


_iso_point(_input)










