def city_formatter(city_name, country_name, population=''):
    if population:
        return "{}, {} - population {}".format(city_name, country_name, population).title()
    else:
        return "{}, {}".format(city_name, country_name).title()