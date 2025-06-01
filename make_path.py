import numpy as np

def make_path(S, T, N, r, sig, M, seed = None, antithetic = False):# S: Initial value, T: Maturity, N: Number of steps, r: Interest rate, sig: Volatility, M: Number of simulations
    if seed is not None:
        np.random.seed(seed)
    
    dt = T/N
    if antithetic:
        if M % 2 == 1:
            print(f'M must be an even number to use antithetic variates. Using M + 1 = {M + 1} instead.')
            M += 1
        M_half = M // 2
        log_S_path  = np.ones((M, N+1)) * np.log(S)
        eps = np.random.standard_normal((M_half, N))
        increment_1 = (r - 0.5*sig**2) * dt + sig * np.sqrt(dt) * eps
        increment_2 = (r - 0.5*sig**2) * dt - sig * np.sqrt(dt) * eps
        log_S_path[:M_half, 1:] += np.cumsum(increment_1, axis=1)
        log_S_path[M_half:M, 1:] += np.cumsum(increment_2, axis=1)
        S_path = np.exp(log_S_path)
        return S_path
    else:
        log_S_path = np.ones((M, N+1)) * np.log(S)
        increment = (r - 0.5*sig**2) * dt + sig * np.sqrt(dt) * np.random.standard_normal((M, N))
        log_S_path[:, 1:] += np.cumsum(increment, axis=1)
        S_path = np.exp(log_S_path)
        return S_path