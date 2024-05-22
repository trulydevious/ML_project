import itertools

import numpy as np
import pandas as pd
from urllib.parse import urlparse


def extract_features(url):
    parsed_url = urlparse(url)
    url_length = len(url)
    num_dots = url.count('.') #TODO czy można to usunąć korelacja=1 z subdomain_level
    #subdomain_level = url.count('.') - 1
    path_level = url.count('/')
    num_dash = url.count('-')
    num_dash_in_hostname = parsed_url.netloc.count('-')
    at_symbol = '@' in url
    tilde_symbol = '~' in url

    num_underscore = url.count('_')
    num_underscore_in_hostname = parsed_url.netloc.count('_')
    num_percent = url.count('%')
    num_query_params = url.count('?')
    num_ampersand = url.count('&')
    num_hash = url.count('#')
    num_numeric_chars = sum(c.isdigit() for c in url)
    path_length = len(parsed_url.path)
    double_slash_in_path = '//' in parsed_url.path

    #sugerowane rozszerzenie
    entropy = -sum(np.log2((url.count(char) / url_length) * (url.count(char) / url_length)) for char in set(url))
    scheme_https = parsed_url.scheme == 'https'

    domain_length = len(parsed_url.netloc.split('.')[-2]) if len(parsed_url.netloc.split('.')) > 1 else len(parsed_url.netloc)
    path_segments = [len(segment) for segment in parsed_url.path.split('/') if segment]
    avg_path_segment_length = np.mean(path_segments) if path_segments else 0
    specific_tlds = ['.tk', '.xyz']
    presence_specific_tlds = any(tld in parsed_url.netloc for tld in specific_tlds)
    sensitive_words = ['update', 'verify', 'secure', 'login', 'bank']
    count_sensitive_words = sum(word in url for word in sensitive_words)
    num_alpha_chars = sum(c.isalpha() for c in url)
    proportion_alpha_chars = num_alpha_chars / url_length if url_length > 0 else 0
    subdomain_length = len(parsed_url.netloc.split('.')[0]) if '.' in parsed_url.netloc else 0
    position_last_dot = url.rfind('.')

    uppercase_count = sum(1 for c in url if c.isupper())
    special_chars_proportion = sum(1 for c in url if not c.isalnum()) / url_length if url_length > 0 else 0
    non_latin_chars = sum(1 for c in url if not c.isascii())
    file_extension_length = len(parsed_url.path.split('.')[-1]) if '.' in parsed_url.path else 0
    url_encoding = '%20' in url or '%21' in url or '%2E' in url

    return pd.Series({
        'NumDots': num_dots,
        #'SubdomainLevel': subdomain_level,
        'PathLevel': path_level,
        'UrlLength': url_length,
        'NumDash': num_dash,
        'NumDashInHostname': num_dash_in_hostname,
        'AtSymbol': at_symbol,
        'TildeSymbol': tilde_symbol,
        'NumUnderscore': num_underscore,
        'NumUnderscoreInHostname': num_underscore_in_hostname,
        'NumPercent': num_percent,
        'NumQueryComponents': num_query_params,
        'NumAmpersand': num_ampersand,
        'NumHash': num_hash,
        'NumNumericChars': num_numeric_chars,
        'PathLength': path_length,
        'DoubleSlashInPath': double_slash_in_path,

        'Entropy': entropy,
        'SchemeHTTPS': scheme_https,
        'DomainLength': domain_length,
        'PathSegmentsLength': avg_path_segment_length,
        'PresenceSpecificTLDs': presence_specific_tlds,
        'CountSensitiveWords': count_sensitive_words,
        'ProportionAlphaChars': proportion_alpha_chars,
        'SubdomainLength': subdomain_length,
        'PositionLastDot': position_last_dot,
        'UppercaseCount': uppercase_count,
        'SpecialCharsProportion': special_chars_proportion,
        'NonLatinChars': non_latin_chars,
        'FileExtensionLength': file_extension_length,
        'URLEncoding': url_encoding
    })
