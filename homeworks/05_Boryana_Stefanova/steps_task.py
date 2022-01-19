def stepCounter(steps):

    if steps < 0:
        return 0

    if steps == 0:
        return 1

    return (stepCounter(steps-1) +
            stepCounter(steps-2))

steps = 3
print(stepCounter(steps))
