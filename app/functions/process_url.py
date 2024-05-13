import pandas as pd
from urllib.parse import urlparse


def extract_features(url):
    parsed_url = urlparse(url)
    url_length = len(url)
    num_dots = url.count('.')
    subdomain_level = url.count('.') - 1
    path_level = url.count('/')
    num_dash = url.count('-')
    num_dash_in_hostname = parsed_url.netloc.count('-')
    at_symbol = '@' in url
    tilde_symbol = '~' in url

    return pd.Series({
        'NumDots': num_dots,
        'SubdomainLevel': subdomain_level,
        'PathLevel': path_level,
        'UrlLength': url_length,
        'NumDash': num_dash,
        'NumDashInHostname': num_dash_in_hostname,
        'AtSymbol': at_symbol,
        'TildeSymbol': tilde_symbol
    })
