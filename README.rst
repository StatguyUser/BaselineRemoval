What is it?
===========

BaselineRemoval is a Python package providing baseline removal.
There are 2 main methods for baseline removal. - **Modpoly** in the
paper titled Automated Method for Subtraction of Fluorescence from
Biological Raman Spectra, by Lieber & Mahadevan-Jansen (2003) -
**IModPoly**, which is an enhancement on existing Modpoly algorithm,
taken from paper titled Automated Autofluorescence Background
Subtraction Algorithm for Biomedical Raman Spectroscopy, by Zhao,
Jianhua, Lui, Harvey, McLean, David I., Zeng, Haishan (2007)

How to use is it?
=================

::

    from BaselineRemoval import BaselineRemoval

    input_array=[10,20,1.5,5,2,9,99,25,47]

    baseObj=BaselineRemoval(input_array,2)
    Modpoly_output=baseObj.ModPoly()
    Imodpoly_output=baseObj.IModPoly()

    print('Original input:',input_array)
    print('Modpoly base corrected values:',Modpoly_output)
    print('IModPoly base corrected values:',Imodpoly_output)

Where to get it?
================

``pip install BaselineRemoval``

Dependencies
============

-  `numpy <https://www.numpy.org/]>`__
-  `scikit-learn <https://scikit-learn.org/>`__

