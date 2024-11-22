import integrate
estimate = integrate.integrate(integrate.f, 0, 1, 100000000)
error = abs(estimate - 1/3.0)
print(estimate, error)
