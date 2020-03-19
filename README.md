# simplicate-delete-org-by-relationtype

## Sample usage:

    (all) $ python 001-get_organizations_by_relationtype.py 
    organization:3adfb72be3bb7af2
    {"data":null,"errors":null,"debug":null}
    organization:30b5b872f0ee2679

## Variables:
- subdomain

type: string, from https://{subdomain}.simplicate.nl
- relation_type_id

type: string, from https://{subdomain}.simplicate.nl/api/v2/crm/relationtype -> {.data.id}
- authentication_key

type: string, from https://{subdomain}.simplicate.nl/environmentmanagement/api
- authentication_secret

type: string, from https://{subdomain}.simplicate.nl/environmentmanagement/api

## Contribute
Roadmap:
- More complex queries
    