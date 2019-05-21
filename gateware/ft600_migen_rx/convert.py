import sys
import struct
import binascii
import numpy as np

in_file = sys.argv[1]

# Read raw 1bit samples stored as a stream of two uint8
# bytes containing I and Q samples as bits.
# I0 I1 I2 I3 I4 I5 I6 I7 Q0 Q1 Q2 Q3 Q4 Q5 Q6 Q7 ...
Bytes = np.fromfile(in_file, dtype = np.uint8)
IQ = Bytes.reshape(len(Bytes) // 2, 2)
I = np.unpackbits(IQ[:,0]).astype(np.int8) * 2 - 1
Q = np.unpackbits(IQ[:,1]).astype(np.int8) * 2 - 1

#nsamples = 100000
nsamples = (len(IQ) // 2) * 8

# Proudly copy-pasted from the docs...
#------------------------------------------------
# Create a FIR filter and apply it
#------------------------------------------------

from scipy.signal import kaiserord, lfilter, firwin, freqz, decimate
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show

sample_rate = 36000000

# The Nyquist rate of the signal.
nyq_rate = sample_rate / 2.0

# The desired width of the transition from pass to stop,
# relative to the Nyquist rate.  We'll design the filter
# with a 1 kHz transition width.
width = 1000e3 / nyq_rate

# The desired attenuation in the stop band, in dB.
ripple_db = 60.0

# Compute the order and Kaiser parameter for the FIR filter.
N, beta = kaiserord(ripple_db, width)

# The cutoff frequency of the filter.
cutoff_hz = sample_rate // 32

# Use firwin with a Kaiser window to create a lowpass FIR filter.
taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

# Use lfilter to filter the iq samples with the FIR filter.
filtered_i = lfilter(taps, 1.0, I[:nsamples])
filtered_q = lfilter(taps, 1.0, Q[:nsamples])


############


# Decimate with a factor of 32
filtered_i = decimate(filtered_i, 32)
filtered_q = decimate(filtered_q, 32)

# Arrange data so we get a stream of interwoven float32 IQ samples (I0 Q0 I1 Q1 ...)
out = np.empty((len(filtered_i) * 2,),).astype(np.float32)
out[0::2] = filtered_i / 32
out[1::2] = filtered_q / 32

out.tofile("out.raw")
