def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
    strip newlines and return a list of the last n lines"""
    with open(filepath) as f:
        return [line.strip() for line in f.readlines()[-n:]]
