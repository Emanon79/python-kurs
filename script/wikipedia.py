import requests
import json
import sys

api_endpoint = "https://en.wikipedia.org/w/api.php"

def invoke_api(params):
    response = requests.get(api_endpoint, params=params)
    response.raise_for_status()
    return response

def opensearch(query):
    params = {'action': 'opensearch',
              'search': query,
              'format': 'json',
              'warningsaserror': True}
    return invoke_api(params).json()

def parse_prop(page, prop):
    params = {'action': 'parse',
              'page': page,
              'prop': prop,
              'format': 'json'}
    return invoke_api(params).json()

def get_wikipedia_page(query, lang='no'):

    search, matches, _, urls = opensearch(query)

    # Select first match
    language_data = parse_prop(matches[0], "langlinks")

    matching_language_links = filter(lambda m: m.get('lang', None) == 'no',
                                     language_data['parse']['langlinks'])
    # Select first match working (if any)
    for matching_language_link in matching_language_links:
        try:
            return requests.get(matching_language_link['url']).text
        except Exception as e:
            print(f"Failed to download {matching_language_link}: {e}", file=sys.stderr)
    return None

print(get_wikipedia_page('Halo', 'no'))
print(get_wikipedia_page('F16'))

