# siML
# Copyright 2016-2017 Ahmet Taspinar
# See LICENSE for details.

"""
Library implementing Machine Learning algorithms from scratch
"""
__version__ = '0.3.0'
__author__ = 'Ahmet Taspinar'
__license__ = 'MIT'

from siml.signal_analysis_utils import (
    detect_peaks,
    get_values,
    get_fft_values,
    get_psd_values,
    autocorr,
    get_autocorr_values,
    get_first_n_peaks,
    get_features,
    extract_features_labels
)
