# Smithsonian Open Access

Python module to query the Smithsonian Institution Open Access API.

A project of the Digitization Program Office, OCIO, Smithsonian.

https://dpo.si.edu/

For details of the developer tools for the Open Access API: https://www.si.edu/openaccess/devtools

For details about Smithsonian Open Access: https://www.si.edu/openaccess

## Installation

To install using pip:

```bash
pip install si_openaccess
```

Or:

```bash
python3 -m pip install si_openaccess
```

## Requirements

The API requires you to provide your own 'api_key' value. Please register with https://api.data.gov/signup/ to get a key.

## Usage

### Get Content

To fetch content based on id/url of an object ([docs](https://edan.si.edu/openaccess/apidocs/#api-content-content)):

```python
content(id=[ITEM ID], api_key=[YOUR API KEY])
```

### Fetch statistics

To fetch stats for CC0 objects/media ([docs](https://edan.si.edu/openaccess/apidocs/#api-metrics-stats)):

```python
metrics_stats(api_key=[YOUR API KEY])
```

### Search contents based on category

To fetch content based on a query against a category. art_design, history_culture or science_technology ([docs](https://edan.si.edu/openaccess/apidocs/#api-search-category_search)):

```python
def category_search(q=[SEARCH TERMS], category=[CATEGORY], start=0, rows=10, sort=[SORT], api_key=[YOUR API KEY])
```

Values for `category` are:

 * `art_design`
 * `history_culture`
 * `science_technology`

Values for `sort` are:

 * `relevancy`
 * `id`
 * `newest`
 * `updated`
 * `random`

### Search

To fetch content based on a query ([docs](https://edan.si.edu/openaccess/apidocs/#api-search-search)):

```python
search(q=[SEARCH TERMS], start=0, rows=10, sort=[SORT], type=[TYPE], row_group=[ROW_GROUP], api_key=[YOUR API KEY])
```

Values for `sort` are:

 * `relevancy`
 * `id`
 * `newest`
 * `updated`
 * `random`

Values for `type` are:

 * `edanmdm`
 * `ead_collection`
 * `ead_component` 
 * `all`

Values for `row_group` are:

 * `objects`
 * `archives`

 
### Search Terms

To Fetches an array of terms based term category ([docs](https://edan.si.edu/openaccess/apidocs/#api-search-terms)):

```python
search_terms(category=[CATEGORY], starts_with=None, api_key=[YOUR API KEY])
```

Values for `category` are:

 * `culture`
 * `data_source`
 * `date`
 * `object_type`
 * `online_media_type`
 * `place`
 * `topic`
 * `unit_code`

The value for `starts_with` is optional.
