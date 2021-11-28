from urllib.parse import urlparse, urljoin


def generate_affiliation_link(url):
    front_tag = "http://www.amazon.com/dp/"
    end_tag = "/?tag=pyb0f-20"
    parsed = urlparse(url)
    directories = parsed.path.strip("/").split("/")
    new_url1 = urljoin(front_tag, str(directories[2]))
    new_url = new_url1 + end_tag
    return new_url
