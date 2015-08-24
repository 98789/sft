# sft

Implementation of FFT algorithm which allows the use of custom weights.
The base code was translated from c++ (with some pythonic additions),
later modified to handle any weight. 

Credit for both the original code and the index management algorithm belong
to professor Homero Ortega (Head researcher at RadioGIS group, Industrial
University of Santander).

fft(xcx, N=0, W=exponential)

Inputs:

xcx: vector of samples (time domain).
N: Number of outputs.
W: Weight to be used: exponential, triangular or any user defined weight function.

Outputs:

Vector Xcx of size N (frequency domain).
