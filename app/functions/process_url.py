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

    num_underscore = url.count('_')
    num_underscore_in_hostname = parsed_url.netloc.count('_')
    num_percent = url.count('%')
    num_query_parts = url.count('&')
    num_query_params = url.count('?')
    num_ampersand = url.count('&')
    num_hash = url.count('#')
    num_numeric_chars = sum(c.isdigit() for c in url)
    hostname_length = len(parsed_url.netloc)
    path_length = len(parsed_url.path)
    double_slash_in_path = '//' in parsed_url.path

    return pd.Series({
        'NumDots': num_dots,
        'SubdomainLevel': subdomain_level,
        'PathLevel': path_level,
        'UrlLength': url_length,
        'NumDash': num_dash,
        'NumDashInHostname': num_dash_in_hostname,
        'AtSymbol': at_symbol,
        'TildeSymbol': tilde_symbol,
        'NumUnderscore': num_underscore,
        'NumUnderscoreInHostname': num_underscore_in_hostname,
        'NumPercent': num_percent,
        'NumQueryParts': num_query_parts,
        'NumQueryComponents': num_query_params,
        'NumAmpersand': num_ampersand,
        'NumHash': num_hash,
        'NumNumericChars': num_numeric_chars,
        'HostnameLength': hostname_length,
        'PathLength': path_length,
        'DoubleSlashInPath': double_slash_in_path

    })
