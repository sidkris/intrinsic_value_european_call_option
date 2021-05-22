import numpy as np
import matplotlib.pyplot as plt

# option strike price
K = 1000
S = np.linspace(700, 1200, num = 10)
holder_value = np.maximum(S-K, 0) # intrinsic/inner value of the european call option

plt.plot(S, holder_value, lw = 2.5) # lw = line width
plt.xlabel("value at option expiry")
plt.ylabel("Intrinsic value of the call option (European)")
plt.grid(True)

