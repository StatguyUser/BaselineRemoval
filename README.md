# What is it?
Python package for baseline correction. It has below 2 methods for baseline removal from spectra.
  - **Modpoly** Modified multi-polynomial fit [1] 
  - **IModPoly** Improved ModPoly, which addresses noise issue in ModPoly [2]
We can use the python library to process spectral data through either ModPoly or IModPoly algorithm for baseline subtraction. The functions will return baseline-subtracted spectrum.

# How to use it?
```python
from BaselineRemoval import BaselineRemoval

input_array=[10,20,1.5,5,2,9,99,25,47]
polynomial_degree=2

baseObj=BaselineRemoval(input_array,polynomial_degree)
Modpoly_output=baseObj.ModPoly()
Imodpoly_output=baseObj.IModPoly()

print('Original input:',input_array)
print('Modpoly base corrected values:',Modpoly_output)
print('IModPoly base corrected values:',Imodpoly_output)

Original input: [10, 20, 1.5, 5, 2, 9, 99, 25, 47]
Modpoly base corrected values: [-1.98455800e-04  1.61793368e+01  1.08455179e+00  5.21544654e+00
  7.20210508e-02  2.15427531e+00  8.44622093e+01 -4.17691125e-03
  8.75511661e+00]
IModPoly base corrected values: [-0.84912125 15.13786196 -0.11351367  3.89675187 -1.33134142  0.70220645
 82.99739548 -1.44577432  7.37269705]

```
# Where to get it?
`pip install BaselineRemoval`

# Dependencies
 - [numpy](https://www.numpy.org/])
 - [scikit-learn](https://scikit-learn.org/)

# References
1. [Automated Method for Subtraction of Fluorescence from Biological Raman Spectra](https://www.researchgate.net/publication/8974238_Automated_Method_for_Subtraction_of_Fluorescence_from_Biological_Raman_Spectra) by Lieber & Mahadevan-Jansen (2003)
2. [Automated Autofluorescence Background Subtraction Algorithm for Biomedical Raman Spectroscopy](https://www.researchgate.net/publication/5818031_Automated_Autofluorescence_Background_Subtraction_Algorithm_for_Biomedical_Raman_Spectroscopy) by Zhao, Jianhua, Lui, Harvey, McLean, David I., Zeng, Haishan (2007)