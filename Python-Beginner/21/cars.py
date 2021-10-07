cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    seperator = ', '
    return seperator.join(cars["Jeep"])



def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    model_list = []
    for make, model in cars.items():
        model_list.append(model[0])
    return model_list


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    model_list = []
    find_list = []
    for models in cars.values():
        for model in models:
            model_list.append(model)
    for item in model_list:
        if grep.lower() in item.lower():
            find_list.append(item)
    return sorted(find_list)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted_models = {}
    for make, models in cars.items():
        sorted_models[make] = sorted(models)

    return sorted_models
