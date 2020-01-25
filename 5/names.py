NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names_set = list(set(names))
    new_list = []
    for name in names_set:
        new_list.append(name.title())

    return new_list


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, reverse=True, key=lambda x: x.split(" ")[-1])


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    short_name = ""
    first_name_length = 999999
    for name in names:
        f_name, _ = name.split(" ")
        if len(f_name) < first_name_length:
            first_name_length = len(f_name)
            short_name = f_name

    return short_name
