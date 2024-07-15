from scipy.optimize import minimize

class Optimization:
    @staticmethod
    def optimize_trajectory(func, initial_guess):
        result = minimize(func, initial_guess)
        return result.x, result.fun
