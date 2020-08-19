market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # if the assertion statement (before the comma) is untrue, python will throw an error
    # make sure that one light is red at all times
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

switchLights(market_2nd)
print('hello')
