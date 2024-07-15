from scipy.integrate import solve_ivp

class NumericalMethods:
    @staticmethod
    def integrate_ode(ode_func, t_span, y0, method='RK45'):
        return solve_ivp(ode_func, t_span, y0, method=method)
