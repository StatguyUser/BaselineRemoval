What is it?
===========

BaselineRemoval is a Python package providing baseline removal. There
are 2 main methods for baseline removal. - **Modpoly** in the paper
titled Automated Method for Subtraction of Fluorescence from Biological
Raman Spectra, by Lieber & Mahadevan-Jansen (2003) - **IModPoly**, which
is an enhancement on existing Modpoly algorithm, taken from paper titled
Automated Autofluorescence Background Subtraction Algorithm for
Biomedical Raman Spectroscopy, by Zhao, Jianhua, Lui, Harvey, McLean,
David I., Zeng, Haishan (2007)

How to use is it?
=================

.. code:: python

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
    Modpoly output: [-1.98455800e-04  1.61793368e+01  1.08455179e+00  5.21544654e+00
      7.20210508e-02  2.15427531e+00  8.44622093e+01 -4.17691125e-03
      8.75511661e+00]
    Imodpoly output: [-0.84912125 15.13786196 -0.11351367  3.89675187 -1.33134142  0.70220645
     82.99739548 -1.44577432  7.37269705]

Where to get it?
================

``pip install BaselineRemoval``

Dependencies
============

-  `numpy <https://www.numpy.org/]>`__
-  `scikit-learn <https://scikit-learn.org/>`__

