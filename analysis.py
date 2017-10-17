import numpy as np


def find_upper_outliers(data, m=1.5):
    quartile_1, quartile_3 = np.percentile(data, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * m)
    upper_bound = quartile_3 + (iqr * m)
    return np.where((data > upper_bound))


def upper_outlier_indices(data, m=1.5):
    return find_upper_outliers(data, m)[0].tolist()
