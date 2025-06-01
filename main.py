import numpy as np
import time
import json

from make_path import make_path
from regression_module import polynomial_regression, polynomial_regression_value

with open('config.json', 'r') as f:
    config = json.load(f)
print(config)

S = config['LSM_parameters']['S']
K = config['LSM_parameters']['K']
T = config['LSM_parameters']['T']
r = config['LSM_parameters']['r']
sig = config['LSM_parameters']['sig']
N = config['LSM_parameters']['N']
M = config['LSM_parameters']['M']
degree = config['LSM_parameters']['degree']
seed = config['LSM_parameters']['seed']
antithetic = config['LSM_parameters']['antithetic']



def price_american_put_LSM(S, K, T, r, sig, N, M, degree = 3, seed = None, antithetic = False):# S: Initial stock price, K: Strike price, T: Time to maturity, r: Risk-free interest rate, sig: Volatility, N: Number of time steps, M: Number of simulation paths
    
    dt = T/N
    disc = np.exp(-r*dt)
    S_path = make_path(S, T, N, r, sig, M, seed, antithetic)
    V = np.maximum(K - S_path[:, N], 0)
    
    # Calculate holding value in backward steps
    for t in range(N-1, 0, -1):
        S_t = S_path[:, t] # Stock price at time t
        discounted_value = disc * V # Discounted future value (value of holding)
        V = discounted_value.copy()
        exercise_value = np.maximum(K - S_t, 0) # Value if exercised at time t (exercise value)
        
        # Select in-the-money paths
        path_itm_indices = np.where(exercise_value > 0)[0]
        S_t_itm = S_t[path_itm_indices]
        
        # Polynomial regression
        if len(S_t_itm) > 0:
            X = S_t_itm
            Y = discounted_value[path_itm_indices]
            coef = polynomial_regression(X, Y, degree)
            if coef is None:
                estimated_value = np.zeros(len(S_t_itm))
            else:
                estimated_value = polynomial_regression_value(X, coef)
                exercise_value_itm = exercise_value[path_itm_indices]
                path_to_exercise = (exercise_value_itm > estimated_value)
                V[path_itm_indices[path_to_exercise]] = exercise_value_itm[path_to_exercise]
        else:
            V = discounted_value.copy()
    return np.mean(disc * V)

start_time = time.time()
print('calculated price:',price_american_put_LSM(S, K, T, r, sig, N, M, degree, seed, antithetic))
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")