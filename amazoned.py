from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

def amazoned(url, affiliate):
    new_url = urlparse(url)
    if not new_url.netloc:
        return None

    query_dict = parse_qs(new_url[4])
    query_dict['tag'] = affiliate
    new_url = new_url[:4] + (urlencode(query_dict, True), ) + new_url [5:]

    return urlunparse(new_url)