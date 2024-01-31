#!/usr/bin/env python3
#
# Python module to query the Smithsonian Institution Open Access API
# v 0.1.2
# 
# 31 Jan 2024
#
# Digitization Program Office,
# Office of the Chief Information Officer,
# Smithsonian Institution
# https://dpo.si.edu
#
# 
# Import modules
import requests
import json


def content(id=None, api_key=None):
    """
    Fetches content based on id/url of an object.
    """
    if id is None:
        raise ValueError("'id' value is required.")
    if api_key is None:
        raise ValueError("'api_key' value is required. Please register with https://api.data.gov/signup/ to get a key.")
    search_url = "https://api.si.edu/openaccess/api/v1.0/content/{}/?api_key={}".format(id, api_key)
    response = requests.get(search_url)
    # Check if API returned an error:
    if response.status_code != 200:
        raise Exception("API returned error: {} (code: {})".format(response.reason, response.status_code))
    res = json.loads(response.text)
    return res['response']


def metrics_stats(api_key=None):
    """
    Fetches stats for CC0 objects/media
    """
    if api_key is None:
        raise ValueError("'api_key' value is required. Please register with https://api.data.gov/signup/ to get a key.")
    search_url = "https://api.si.edu/openaccess/api/v1.0/stats?api_key={}".format(api_key)
    response = requests.get(search_url)
    # Check if API returned an error:
    if response.status_code != 200:
        raise Exception("API returned error: {} (code: {})".format(response.reason, response.status_code))
    res = json.loads(response.text)
    return res['response']


def category_search(q=None, category=None, start=0, rows=10, sort='relevancy', api_key=None):
    """
    Fetches content based on a query against a category. art_design, history_culture or science_technology.
    """
    sort_vals = ["relevancy", "id", "newest", "updated", "random"]
    if sort not in sort_vals:
        raise ValueError("Allowed values for '{}' are: {}".format("sort", ', '.join(sort_vals)))
    category_vals = ["art_design", "history_culture", "science_technology"]
    if category not in category_vals:
        raise ValueError("Allowed values for '{}' are: {}".format("category", ', '.join(category_vals)))
    if q is None:
        raise ValueError("'q' value is required.")
    start = int(start)
    rows = int(rows)
    if api_key is None:
        raise ValueError("'api_key' value is required. Please register with https://api.data.gov/signup/ to get a key.")
    search_url = "https://api.si.edu/openaccess/api/v1.0/category/{}/search?q={}&start={}&rows={}&sort={}&api_key={}".format(category, q, start, rows, sort, api_key)
    response = requests.get(search_url)
    # Check if API returned an error:
    if response.status_code != 200:
        raise Exception("API returned error: {} (code: {})".format(response.reason, response.status_code))
    res = json.loads(response.text)
    if res['response']['rowCount'] == 0:
        return None
    else:
        return res['response']['rows']


def search(q=None, start=0, rows=10, sort='relevancy', type='edanmdm', row_group='objects', api_key=None):
    """
    Fetches content based on a query
    """
    sort_vals = ["relevancy", "id", "newest", "updated", "random"]
    if sort not in sort_vals:
        raise ValueError("Allowed values for '{}' are: {}".format("sort", ', '.join(sort_vals)))
    type_vals = ["edanmdm", "ead_collection", "ead_component", "all"]
    if type not in type_vals:
        raise ValueError("Allowed values for '{}' are: {}".format("type", ', '.join(type_vals)))
    row_group_vals = ["objects", "archives"]
    if row_group not in row_group_vals:
        raise ValueError("Allowed values for '{}' are: {}".format("row_group", ', '.join(row_group_vals)))
    if q is None:
        raise ValueError("'q' value is required.")
    start = int(start)
    rows = int(rows)
    if api_key is None:
        raise ValueError("'api_key' value is required. Please register with https://api.data.gov/signup/ to get a key.")
    search_url = "https://api.si.edu/openaccess/api/v1.0/search?q={}&start={}&rows={}&sort={}&type={}&row_group={}&api_key={}".format(q, start, rows, sort, type, row_group, api_key)
    response = requests.get(search_url)
    # Check if API returned an error:
    if response.status_code != 200:
        raise Exception("API returned error: {} (code: {})".format(response.reason, response.status_code))
    res = json.loads(response.text)
    if res['response']['rowCount'] == 0:
        return None
    else:
        return res['response']['rows']


def search_terms(category=None, starts_with=None, api_key=None):
    """
    Fetches an array of terms based term category
    """
    cat_vals = ["culture", "data_source", "date", "object_type", "online_media_type", "place", "topic", "unit_code"]
    if category not in cat_vals:
        raise ValueError("Allowed values for '{}' are: {}".format("category", ', '.join(cat_vals)))
    if api_key is None:
        raise ValueError("'api_key' value is required. Please register with https://api.data.gov/signup/ to get a key.")
    search_url = "https://api.si.edu/openaccess/api/v1.0/terms/{}?api_key={}".format(category, api_key)
    if starts_with is not None:
        search_url = "{}&starts_with={}".format(search_url, starts_with)
    response = requests.get(search_url)
    # Check if API returned an error:
    if response.status_code != 200:
        raise Exception("API returned error: {} (code: {})".format(response.reason, response.status_code))
    terms = json.loads(response.text)['response']['terms']
    return terms


