# LSM American Option Pricer

## Description
This project implements the Longstaff-Schwartz Monte Carlo method to price American put options.

## Files
- `main.py`: Main script to run the pricing model.
- `make_path.py`: Module for generating stock price paths using Geometric Brownian Motion.
- `regression_module.py`: Module for polynomial regression used in estimating the continuation value.
- `config.json`: Configuration file for LSM parameters (S, K, T, r, sig, N, M, degree, etc.).
- `requirements.txt`: (Recommended) List of Python dependencies.

## Requirements
- Python 3.x
- NumPy
(Add other libraries if you use them, e.g., pytest for tests)

## Usage
1.  Ensure all required libraries are installed. If `requirements.txt` is provided:
    ```bash
    pip install -r requirements.txt
    ```
2.  Modify `config.json` with the desired option and model parameters.
3.  Run the main script:
    ```bash
    python main.py
    ```
The calculated option price and computation time will be printed to the console.

## How it Works
The program simulates multiple stock price paths and uses a backward induction algorithm. At each time step, it decides whether to exercise the option or continue holding it based on a polynomial regression of the discounted future cash flows on the current stock price for in-the-money paths."# LSM-American-Put-Pricer" 
