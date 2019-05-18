import re


def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = (
        "Introduction 1 Lecture 01:47"
        "The Basics 4 Lectures 32:03"
        "Getting Technical!  4 Lectures 41:51"
        "Challenge 2 Lectures 27:48"
        "Afterword 1 Lecture 05:02"
    )
    pattern = r"\d{2}:\d{2}"
    course_times = re.findall(pattern, flask_course)

    return course_times


def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    tweet = (
        "New PyBites article: Module of the Week - Requests-cache "
        "for Repeated API Calls - http://pybit.es/requests-cache.html "
        "#python #APIs"
    )

    pattern = "http"
    text = tweet

    match = re.search(pattern, text)

    s = match.start()

    tweet_match = tweet[s : len(tweet)]

    txt1 = tweet_match.split("\b")
    txt2 = [line.split() for line in txt1]
    new_list = []
    for i in range(0, len(txt2)):
        l1 = txt2[i]
        for w in l1:
            new_list.append(w)
    return new_list


def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = "<p>pybites != greedy</p>" "<p>not the same can be said REgarding ...</p>"

    pattern = "<p>(.+?)</p>"
    text = html

    match = re.findall(pattern, text)
    return match[0]
