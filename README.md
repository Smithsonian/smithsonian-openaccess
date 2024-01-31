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

## Usage

### Get Content

To fetch content based on id/url of an object ([docs](https://edan.si.edu/openaccess/apidocs/#api-content-content)):

```python
content(id=[ITEM ID], api_key=api_key)
```

### Fetch statistics

To fetch stats for CC0 objects/media ([docs](https://edan.si.edu/openaccess/apidocs/#api-metrics-stats)):

```python
metrics_stats(api_key=api_key)
```

### Search contents based on category

To fetch content based on a query against a category. art_design, history_culture or science_technology ([docs](https://edan.si.edu/openaccess/apidocs/#api-search-category_search)):

```python
def category_search(q=[SEARCH TERMS], category=[CATEGORY], start=0, rows=10, sort='relevancy', api_key=api_key)
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
search(q=[SEARCH TERMS], start=0, rows=10, sort='relevancy', type='edanmdm', row_group='objects', api_key=api_key)
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
search_terms(category=None, starts_with=None, api_key=api_key)
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
