# disasters
# DisasterModel.py

"""
A model for coal mining disaster time series with a changepoint

switchpoint: s ~ U(0,111)
early_mean: e ~ Exp(1.)
late_mean: l ~ Exp(1.)
disasters: D[t] ~ Poisson(early if t <= s, l otherwise)
"""

import pymc
import numpy as np

disasters_array =\
                np.array([ 4, 5, 4, 0, 1, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6,
                           3, 3, 5, 4, 5, 3, 1, 4, 4, 1, 5, 5, 3, 4, 2, 5,
                           2, 2, 3, 4, 2, 1, 3, 2, 2, 1, 1, 1, 1, 3, 0, 0,
                           1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1,
                           0, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 2,
                           3, 3, 1, 1, 2, 1, 1, 1, 1, 2, 4, 2, 0, 0, 1, 4,
                           0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1])

# priors on s, e, l
s = pymc.DiscreteUniform('s', lower=0, upper=110, doc='Switchpoint[year]')
e = pymc.Exponential('e', beta=1)
l = pymc.Exponential('l', beta=1)

@pymc.deterministic(plot=False)
def r(s=s, e=e, l=l):
    """Concatenate Poisson means"""
    out = np.empty(len(disasters_array))
    out[:s] = e
    out[s:] = l
    return out

# likelihood
D = pymc.Poisson('D', mu=r, value=disasters_array, observed=True)

