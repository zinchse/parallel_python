def integrate_square(
        l: 'float', 
        r: 'float', 
        n_steps: 'int'
        ):
    s = 0
    h = (r - l) / n_steps
    for i in range(n_steps):
        x = l + i * h
        f = x ** 2
        s += f * h 
    return s
