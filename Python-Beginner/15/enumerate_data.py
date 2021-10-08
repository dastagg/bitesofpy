names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries(names=names, countries=countries):
    """Outputs:
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico"""

    names_countries = list(zip(names, countries))
    for count, n_c in enumerate(names_countries, start=1):
        print(f"{count}. {n_c[0]:<10} {n_c[1]}")


if __name__ == "__main__":
    enumerate_names_countries(names, countries)
