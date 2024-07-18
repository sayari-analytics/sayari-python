# Reference
## Attributes
<details><summary><code>client.attributes.<a href="src/sayari/attributes/client.py">post_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Adds a new Attribute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari import AddAttribute
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.attributes.post_attribute(
    request=AddAttribute(
        entity="zq04axX2dLn9tE6W6Q8Qhg",
        type="address",
        value={
            "street1": "1600 Pennsylvania Avenue NW",
            "city": "Washington DC",
            "state": "Washington DC",
            "postalCode": "20500",
            "country": "US",
        },
        to_date="2024-04-30",
        from_date="2024-01-01",
        date="2024-02-15",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `AddAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attributes.<a href="src/sayari/attributes/client.py">patch_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Updates an existing Attribute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari import UpdateAttribute
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.attributes.patch_attribute(
    attribute_id="enEwNGF4WDJkTG45dEU2VzZROFFoZ3xhZGRyZXNzfDBwbEVCMHxVNzhzN21yOUVFTThIZ3pwREM3UDFB",
    request=UpdateAttribute(
        value={
            "street1": "1600 Pennsylvania Avenue NW",
            "city": "Washington DC",
            "state": "Washington DC",
            "postalCode": "20500",
            "country": "US",
        },
        to_date="2024-04-30",
        from_date="2024-01-01",
        date="2024-02-15",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateAttribute` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.attributes.<a href="src/sayari/attributes/client.py">delete_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Delete an existing Attribute
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.attributes.delete_attribute(
    attribute_id="enEwNGF4WDJkTG45dEU2VzZROFFoZ3xhZGRyZXNzfDBwbEVCMHxVNzhzN21yOUVFTThIZ3pwREM3UDFB",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Auth
<details><summary><code>client.auth.<a href="src/sayari/auth/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Hit the auth endpoint to get a bearer token
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.auth.get_token(
    client_id="your client_id here",
    client_secret="your client_secret here",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity
<details><summary><code>client.entity.<a href="src/sayari/entity/client.py">get_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an entity from the database based on the ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.entity.get_entity(
    id="mGq1lpuqKssNWTjIokuPeA",
    attributes_name_limit=1,
    attributes_address_limit=1,
    attributes_country_limit=1,
    attributes_additional_information_limit=1,
    attributes_business_purpose_limit=1,
    attributes_company_type_limit=1,
    attributes_identifier_limit=1,
    attributes_status_limit=1,
    relationships_limit=1,
    possibly_same_as_limit=1,
    referenced_by_limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the entity
    
</dd>
</dl>

<dl>
<dd>

**attributes_additional_information_next:** `typing.Optional[str]` — The pagination token for the next page of attribute `additional_information`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_additional_information_prev:** `typing.Optional[str]` — The pagination token for the previous page of attribute `additional_information`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_additional_information_limit:** `typing.Optional[int]` — Limit total values returned for attribute `additional_information`. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**attributes_address_next:** `typing.Optional[str]` — The pagination token for the next page of attribute `address`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_address_prev:** `typing.Optional[str]` — The pagination token for the previous page of attribute `address`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_address_limit:** `typing.Optional[int]` — Limit total values returned for attribute `address`. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**attributes_business_purpose_next:** `typing.Optional[str]` — The pagination token for the next page of attribute `business_purpose`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_business_purpose_prev:** `typing.Optional[str]` — The pagination token for the previous page of attribute `business_purpose`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_business_purpose_limit:** `typing.Optional[int]` — Limit total values returned for attribute `business_purpose`. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**attributes_company_type_next:** `typing.Optional[str]` — The pagination token for the next page of attribute `company_type`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_company_type_prev:** `typing.Optional[str]` — The pagination token for the previous page of attribute `company_type`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_company_type_limit:** `typing.Optional[int]` — Limit total values returned for attribute `company_type`. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**attributes_country_next:** `typing.Optional[str]` — The pagination token for the next page of attribute `country`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_country_prev:** `typing.Optional[str]` — The pagination token for the previous page of attribute `country`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_country_limit:** `typing.Optional[int]` — Limit total values returned for attribute `country`. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**attributes_identifier_next:** `typing.Optional[str]` — The pagination token for the next page of attribute `identifier`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_identifier_prev:** `typing.Optional[str]` — The pagination token for the previous page of attribute `identifier`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_identifier_limit:** `typing.Optional[int]` — Limit total values returned for attribute `identifier`. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**attributes_name_next:** `typing.Optional[str]` — The pagination token for the next page of attribute `name`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_name_prev:** `typing.Optional[str]` — The pagination token for the previous page of attribute `name`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_name_limit:** `typing.Optional[int]` — Limit total values returned for attribute `name`. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**attributes_status_next:** `typing.Optional[str]` — The pagination token for the next page of attribute `status`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_status_prev:** `typing.Optional[str]` — The pagination token for the previous page of attribute `status`.
    
</dd>
</dl>

<dl>
<dd>

**attributes_status_limit:** `typing.Optional[int]` — Limit total values returned for attribute `status`. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**relationships_next:** `typing.Optional[str]` — The pagination token for the next page of relationship results
    
</dd>
</dl>

<dl>
<dd>

**relationships_prev:** `typing.Optional[str]` — The pagination token for the previous page of relationship results
    
</dd>
</dl>

<dl>
<dd>

**relationships_limit:** `typing.Optional[int]` — Limit total relationship values. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**relationships_type:** `typing.Optional[Relationships]` — Filter relationships to [relationship type](/sayari-library/ontology/relationships), e.g. director_of or has_shareholder
    
</dd>
</dl>

<dl>
<dd>

**relationships_sort:** `typing.Optional[str]` — Sorts relationships by As Of date or Shareholder percentage, e.g. date or -shares
    
</dd>
</dl>

<dl>
<dd>

**relationships_start_date:** `typing.Optional[dt.date]` — Filters relationships to after a date
    
</dd>
</dl>

<dl>
<dd>

**relationships_end_date:** `typing.Optional[dt.date]` — Filters relationships to before a date
    
</dd>
</dl>

<dl>
<dd>

**relationships_min_shares:** `typing.Optional[int]` — Filters relationships to greater than or equal to a Shareholder percentage
    
</dd>
</dl>

<dl>
<dd>

**relationships_country:** `typing.Optional[typing.Union[Country, typing.Sequence[Country]]]` — Filters relationships to a list of [countries](/sayari-library/ontology/enumerated-types#country)
    
</dd>
</dl>

<dl>
<dd>

**relationships_arrival_country:** `typing.Optional[typing.Union[Country, typing.Sequence[Country]]]` — Filters shipment relationships to a list of arrival [countries](/sayari-library/ontology/enumerated-types#country)
    
</dd>
</dl>

<dl>
<dd>

**relationships_arrival_state:** `typing.Optional[str]` — Filters shipment relationships to an arrival state
    
</dd>
</dl>

<dl>
<dd>

**relationships_arrival_city:** `typing.Optional[str]` — Filters shipment relationships to an arrival city
    
</dd>
</dl>

<dl>
<dd>

**relationships_departure_country:** `typing.Optional[typing.Union[Country, typing.Sequence[Country]]]` — Filters shipment relationships to a list of departure [countries](/sayari-library/ontology/enumerated-types#country)
    
</dd>
</dl>

<dl>
<dd>

**relationships_departure_state:** `typing.Optional[str]` — Filters shipment relationships to a departure state
    
</dd>
</dl>

<dl>
<dd>

**relationships_departure_city:** `typing.Optional[str]` — Filters shipment relationships to a departure city
    
</dd>
</dl>

<dl>
<dd>

**relationships_partner_name:** `typing.Optional[str]` — Filters shipment relationships to a trade partner name
    
</dd>
</dl>

<dl>
<dd>

**relationships_partner_risk:** `typing.Optional[typing.Union[Risk, typing.Sequence[Risk]]]` — Filters shipment relationships to a trade partner [risk tag](/sayari-library/ontology/enumerated-types#tag)
    
</dd>
</dl>

<dl>
<dd>

**relationships_hs_code:** `typing.Optional[str]` — Filters shipment relationships to an HS code
    
</dd>
</dl>

<dl>
<dd>

**possibly_same_as_next:** `typing.Optional[str]` — The pagination token for the next page of possibly same entities.
    
</dd>
</dl>

<dl>
<dd>

**possibly_same_as_prev:** `typing.Optional[str]` — The pagination token for the previous page of possibly same entities.
    
</dd>
</dl>

<dl>
<dd>

**possibly_same_as_limit:** `typing.Optional[int]` — Limit total possibly same as entities. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**referenced_by_next:** `typing.Optional[str]` — The pagination token for the next page of the entity's referencing records
    
</dd>
</dl>

<dl>
<dd>

**referenced_by_prev:** `typing.Optional[str]` — The pagination token for the previous page of the entity's referencing records
    
</dd>
</dl>

<dl>
<dd>

**referenced_by_limit:** `typing.Optional[int]` — Limit totals values returned for entity's referencing records. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/sayari/entity/client.py">entity_summary</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Entity Summary endpoint returns a smaller entity payload
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.entity.entity_summary(
    id="mGq1lpuqKssNWTjIokuPeA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Info
<details><summary><code>client.info.<a href="src/sayari/info/client.py">get_usage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The usage endpoint provides a simple interface to retrieve information on usage made by your API account. This includes both views per API path and credits consumed. The time period for the usage query is also specified in the response and whether or not this includes total usage.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.info.get_usage(
    from_=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    to=datetime.date.fromisoformat(
        "2023-01-15",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[dt.date]` — An ISO 8601 encoded date string indicating the starting time period to obtain usage stats. In the format YYYY-MM-DD
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[dt.date]` — An ISO 8601 encoded date string indicating the ending time period to obtain usage stats. In the format YYYY-MM-DD
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.info.<a href="src/sayari/info/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The history endpoint return a user's event history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.info.get_history(
    events="string",
    from_=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    to=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    size=1,
    token="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**events:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The type of events to filter on.
    
</dd>
</dl>

<dl>
<dd>

**from_:** `typing.Optional[dt.date]` — An ISO 8601 encoded date string indicating the starting time period for the events. In the format YYYY-MM-DD
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[dt.date]` — An ISO 8601 encoded date string indicating the ending time period for the events. In the format YYYY-MM-DD
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Size to limit number of events returned
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[str]` — Pagination token to retrieve the next page of results
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metadata
<details><summary><code>client.metadata.<a href="src/sayari/metadata/client.py">metadata</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get metadta about the api, both its versions, which releases are present, and the identity of the authenticated user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.metadata.metadata()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notifications
<details><summary><code>client.notifications.<a href="src/sayari/notifications/client.py">project_notifications</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> The Project Notifications endpoint returns a list of notifications on all entities saved to a project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.notifications.project_notifications(
    id="0oZnoG",
    limit=20,
    sort="-date",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the project
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit total notifications in the response. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset which notifications are returned. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[NotificationsSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/sayari/notifications/client.py">resource_notifications</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> The Resource Notifications endpoint returns a list of notifications for a saved entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.notifications.resource_notifications(
    id="03ePyj",
    limit=20,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit total notifications in the response. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset which notifications are returned. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/sayari/notifications/client.py">delete_project_notifications</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all notifications from a project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.notifications.delete_project_notifications(
    project_id="YWmNKV",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/sayari/notifications/client.py">delete_entity_notifications</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes notifications for saved resources of an entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.notifications.delete_entity_notifications(
    entity_id="N0xLDy4wcud-M1ZtwdsvRA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/sayari/notifications/client.py">delete_resource_notifications</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes notifications for a saved resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.notifications.delete_resource_notifications(
    resource_id="oGxxqG",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Project
<details><summary><code>client.project.<a href="src/sayari/project/client.py">create_project</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Create a new project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari import CreateProjectRequest
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.project.create_project(
    request=CreateProjectRequest(
        label="Project Alpha",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateProjectRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/sayari/project/client.py">get_projects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Retrieve a list of projects including upload progress info.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.project.get_projects(
    archived=True,
    limit=5,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**next:** `typing.Optional[str]` — The pagination token for the next page of projects.
    
</dd>
</dl>

<dl>
<dd>

**prev:** `typing.Optional[str]` — The pagination token for the previous page of projects.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit total values returned for projects. Defaults to 100. Max 100.
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Toggle between projects that have been archived (true) or not (false). Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/sayari/project/client.py">get_project_entities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Retrieve a list of entities in a project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.project.get_project_entities(
    id="gPq6EY",
    accept="application/json",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The project identifier.
    
</dd>
</dl>

<dl>
<dd>

**accept:** `GetProjectEntitiesAcceptHeader` — The response format. Defaults to application/json.
    
</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — The pagination token for the next page of entities.
    
</dd>
</dl>

<dl>
<dd>

**prev:** `typing.Optional[str]` — The pagination token for the previous page of entities.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit total entities returned. Defaults to 1,000. Max 10,000.
    
</dd>
</dl>

<dl>
<dd>

**entity_types:** `typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]` — Only return entities of the specified [entity type(s)](/sayari-library/ontology/entities). Defaults to all types.
    
</dd>
</dl>

<dl>
<dd>

**geo_facets:** `typing.Optional[bool]` — Whether to include geo facets in the response. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**hs_codes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Only return entities with the specified HS code(s).
    
</dd>
</dl>

<dl>
<dd>

**received_hs_codes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Only return entities that received the specified HS code(s).
    
</dd>
</dl>

<dl>
<dd>

**shipped_hs_codes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Only return entities that shipped the specified HS code(s).
    
</dd>
</dl>

<dl>
<dd>

**translation:** `typing.Optional[str]` — The language code to translate the entity labels to. Defaults to the user's preferred language.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[
    typing.Union[ProjectEntitiesFilter, typing.Sequence[ProjectEntitiesFilter]]
]` — Filter for entities in a project. The format is `field=value`, where the equal sign is encoded as `%3D`. Supported fields are as follows
    
</dd>
</dl>

<dl>
<dd>

**aggregations:** `typing.Optional[
    typing.Union[
        ProjectEntitiesAggsDefinition,
        typing.Sequence[ProjectEntitiesAggsDefinition],
    ]
]` — Aggregations that should be returned for entities in the project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/sayari/project/client.py">delete_project</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.project.delete_project(
    project_id="Gam5qG",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Record
<details><summary><code>client.record.<a href="src/sayari/record/client.py">get_record</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a record from the database based on the ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.record.get_record(
    id="74cf0fc2a62f9c8f4e88f8a0b3ffcca4%2FF0000110%2F1682970471254",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for a record in the database
    
</dd>
</dl>

<dl>
<dd>

**references_limit:** `typing.Optional[int]` — A limit on the number of references to be returned. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**references_offset:** `typing.Optional[int]` — Number of references to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Resolution
<details><summary><code>client.resolution.<a href="src/sayari/resolution/client.py">resolution</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.resolution.resolution(
    name="victoria beckham limited",
    limit=1,
    profile="suppliers",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 10 inclusive. Defaults to 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Entity name
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `typing.Optional[
    typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]
]` — Entity identifier. Can be from either the [Identifier Type](/sayari-library/ontology/enumerated-types#identifier-type) or [Weak Identifier Type](/sayari-library/ontology/enumerated-types#weak-identifier-type) enums.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[typing.Union[Country, typing.Sequence[Country]]]` — Entity country - must be ISO (3166) Trigram i.e., `USA`. See complete list [here](/sayari-library/ontology/enumerated-types#country)
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Entity address
    
</dd>
</dl>

<dl>
<dd>

**date_of_birth:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Entity date of birth
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Entity contact
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]` — [Entity type](/sayari-library/ontology/entities). If multiple values are passed for any field, the endpoint will match entities with ANY of the values.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[ProfileEnum]` — Profile can be used to switch between search algorithms. The default profile `corporate` is optimized for accurate entity attribute matching and is ideal for business verification and matching entities with corporate data. The `suppliers` profile is optimized for matching entities with extensive trade data. Ideal for supply chain and trade-related use cases.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resolution.<a href="src/sayari/resolution/client.py">resolution_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari import ResolutionBody
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.resolution.resolution_post(
    limit=1,
    request=ResolutionBody(
        name=["victoria beckham limited"],
        profile="suppliers",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ResolutionBody` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 10 inclusive. Defaults to 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resolution.<a href="src/sayari/resolution/client.py">resolution_persisted</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> The persisted resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the resolution endpoint, except it also stores matched entities into user's project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari import ResolutionBody
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.resolution.resolution_persisted(
    project_id="6GaxYn",
    limit=1,
    request=ResolutionBody(
        name=["victoria beckham limited"],
        profile="suppliers",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — Unique identifier of the project
    
</dd>
</dl>

<dl>
<dd>

**request:** `ResolutionBody` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 10 inclusive. Defaults to 10.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Resource
<details><summary><code>client.resource.<a href="src/sayari/resource/client.py">save_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Save an entity to a project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari import SaveEntityRequest
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.resource.save_entity(
    request=SaveEntityRequest(
        type="entity",
        project="GNJbkG",
        entity_id="Zk0qOaM2SSYg_ZhsljykMQ",
        custom_fields={"properties": {"custom_name": "Victoria Beckham"}},
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SaveEntityRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.resource.<a href="src/sayari/resource/client.py">delete_resource</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing saved resource from a project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.resource.delete_resource(
    type="entity",
    resource_id="YWmNKV",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `ResourceType` 
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Search
<details><summary><code>client.search.<a href="src/sayari/search/client.py">search_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for an entity. Please note, searches are limited to a maximum of 10,000 results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.search.search_entity(
    limit=1,
    q="victoria beckham limited",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[SearchField]]` — Record or entity fields to search against.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[FilterList]` — Filters to be applied to search query to limit the result-set.
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[bool]` — Whether or not to return search facets in results giving counts by field. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**geo_facets:** `typing.Optional[bool]` — Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**advanced:** `typing.Optional[bool]` — Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.search.<a href="src/sayari/search/client.py">search_entity_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for an entity. Please note, searches are limited to a maximum of 10,000 results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.search.search_entity_get(
    limit=1,
    q="victoria beckham limited",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]]` — Record or entity fields to search against.
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[bool]` — Whether or not to return search facets in results giving counts by field. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**geo_facets:** `typing.Optional[bool]` — Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**advanced:** `typing.Optional[bool]` — Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.search.<a href="src/sayari/search/client.py">search_record</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for a record. Please note, searches are limited to a maximum of 10,000 results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.search.search_record(
    limit=1,
    q="victoria beckham limited",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[SearchField]]` — Record or entity fields to search against.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[FilterList]` — Filters to be applied to search query to limit the result-set.
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[bool]` — Whether or not to return search facets in results giving counts by field. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**advanced:** `typing.Optional[bool]` — Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.search.<a href="src/sayari/search/client.py">search_record_get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for a record. Please note, searches are limited to a maximum of 10,000 results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.search.search_record_get(
    q="victoria beckham limited",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]]` — Record or entity fields to search against.
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[bool]` — Whether or not to return search facets in results giving counts by field. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**advanced:** `typing.Optional[bool]` — Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Source
<details><summary><code>client.source.<a href="src/sayari/source/client.py">list_sources</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for all sources that Sayari collects data from
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.source.list_sources(
    limit=2,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.source.<a href="src/sayari/source/client.py">get_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for a source that Sayari collects data from
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.source.get_source(
    id="f4396e4b8a41d1fd9f09ea94d2ebedb9",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for a source in the database
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SupplyChain
<details><summary><code>client.supply_chain.<a href="src/sayari/supply_chain/client.py">upstream_trade_traversal</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Execute a traversal of the upstream trade network (supply chain) of an entity, returning a set of entities and edges between them.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.supply_chain.upstream_trade_traversal(
    id="ESkH7J-UCRfY5t0_JXIH3w",
    min_date="2023-03-15",
    product=["3204"],
    risk=["forced_labor_xinjiang_origin_subtier"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The root entity identifier.
    
</dd>
</dl>

<dl>
<dd>

**risk:** `typing.Optional[typing.Sequence[Risk]]` — Risk leaf node filter. Only return supply chains that end with a supplier that has 1+ of the specified [risk factors](/sayari-library/ontology/risk-factors).
    
</dd>
</dl>

<dl>
<dd>

**not_risk:** `typing.Optional[typing.Sequence[Risk]]` — Risk leaf node filter. Only return supply chains that end with a supplier that has none of the specified [risk factors](/sayari-library/ontology/risk-factors).
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Sequence[Country]]` — Country leaf node filter. Only return supply chains that end with a supplier in 1+ of the specified countries.
    
</dd>
</dl>

<dl>
<dd>

**not_countries:** `typing.Optional[typing.Sequence[Country]]` — Country leaf node filter. Only return supply chains that end with a supplier in none of the specified countries.
    
</dd>
</dl>

<dl>
<dd>

**product:** `typing.Optional[typing.Sequence[str]]` — Product root edge filter. Only return supply chains that start with an edge that has 1+ of the specified HS codes.
    
</dd>
</dl>

<dl>
<dd>

**not_product:** `typing.Optional[typing.Sequence[str]]` — Product root edge filter. Only return supply chains that start with an edge that has none of the specified HS codes.
    
</dd>
</dl>

<dl>
<dd>

**component:** `typing.Optional[typing.Sequence[str]]` — Component node filter. Only return supply chains that contain at least one edge with 1+ of the specified HS codes.
    
</dd>
</dl>

<dl>
<dd>

**not_component:** `typing.Optional[typing.Sequence[str]]` — Component node filter. Only return supply chains that contain no edges with any of the specified HS codes.
    
</dd>
</dl>

<dl>
<dd>

**min_date:** `typing.Optional[str]` — Minimum date edge filter. Only return supply chains with edge dates that are greater than or equal to this date.
    
</dd>
</dl>

<dl>
<dd>

**max_date:** `typing.Optional[str]` — Maximum date edge filter. Only return supply chains with edge dates that are less than or equal to this date.
    
</dd>
</dl>

<dl>
<dd>

**max_depth:** `typing.Optional[int]` — The maximum depth of the traversal, from 1 to 4 inclusive. Default is 4. Reduce if query is timing out.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return. Default and maximum values are 25,000.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trade
<details><summary><code>client.trade.<a href="src/sayari/trade/client.py">search_shipments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Search for a shipment. Please note, searches are limited to a maximum of 10,000 results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.trade.search_shipments(
    limit=1,
    q="rum",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[TradeFilterList]` — Filters to be applied to search query to limit the result-set.
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[bool]` — Whether or not to return search facets in results giving counts by field. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trade.<a href="src/sayari/trade/client.py">search_suppliers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Search for a supplier. Please note, searches are limited to a maximum of 10,000 results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.trade.search_suppliers(
    limit=1,
    q="rum",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[TradeFilterList]` — Filters to be applied to search query to limit the result-set.
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[bool]` — Whether or not to return search facets in results giving counts by field. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trade.<a href="src/sayari/trade/client.py">search_buyers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Search for a buyer. Please note, searches are limited to a maximum of 10,000 results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.trade.search_buyers(
    limit=1,
    q="rum",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before returning response. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[TradeFilterList]` — Filters to be applied to search query to limit the result-set.
    
</dd>
</dl>

<dl>
<dd>

**facets:** `typing.Optional[bool]` — Whether or not to return search facets in results giving counts by field. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Traversal
<details><summary><code>client.traversal.<a href="src/sayari/traversal/client.py">traversal</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Traversal endpoint returns paths from a single target entity to up to 50 directly or indirectly-related entities. Each path includes information on the 0 to 10 intermediary entities, as well as their connecting relationships. The response's explored_count field indicates the size of the graph subset the application searched. Running a traversal on a highly connected entity with a restrictive set of argument filters and a high max depth will require the application to explore a higher number of traversal paths, which may affect performance. In cases where a traversal searches over a very large, highly-connected subgraph, a partial result set may be returned containing only the most relevant results. This will be indicated in the response by the partial_results field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.traversal.traversal(
    id="mGq1lpuqKssNWTjIokuPeA",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the entity
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit total values for traversal. Defaults to 10. Max of 50.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset values for traversal. Defaults to 0. Max of 1000.
    
</dd>
</dl>

<dl>
<dd>

**min_depth:** `typing.Optional[int]` — Set minimum depth for traversal. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**max_depth:** `typing.Optional[int]` — Set maximum depth for traversal. Defaults to 4.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[typing.Union[Relationships, typing.Sequence[Relationships]]]` — Set relationship type(s) to follow when traversing related entities. Defaults to following all relationship types.
    
</dd>
</dl>

<dl>
<dd>

**psa:** `typing.Optional[bool]` — Also traverse relationships from entities that are possibly the same as any entity that appears in the path. Defaults to traversing possibly same as relationships.
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Union[Country, typing.Sequence[Country]]]` — Filter paths to only those that end at an entity associated with the specified country(ies). Defaults to returning paths that end in any [country](/sayari-library/ontology/enumerated-types#country).
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]` — Filter paths to only those that end at an entity of the specified type(s). Defaults to returning paths that end at any type.
    
</dd>
</dl>

<dl>
<dd>

**sanctioned:** `typing.Optional[bool]` — Filter paths to only those that end at an entity appearing on a watchlist. Defaults to not filtering paths by sanctioned status.
    
</dd>
</dl>

<dl>
<dd>

**pep:** `typing.Optional[bool]` — Filter paths to only those that end at an entity appearing on a pep list. Defaults to not filtering paths by pep status.
    
</dd>
</dl>

<dl>
<dd>

**min_shares:** `typing.Optional[int]` — Set minimum percentage of share ownership for traversal. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**include_unknown_shares:** `typing.Optional[bool]` — Also traverse relationships when share percentages are unknown. Only useful when min_shares is set greater than 0. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**exclude_former_relationships:** `typing.Optional[bool]` — Include relationships that were valid in the past but not at the present time. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**exclude_closed_entities:** `typing.Optional[bool]` — Include entities that existed in the past but not at the present time. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**eu_high_risk_third:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_modern_slavery:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**state_owned:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**formerly_sanctioned:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_terrorism:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_organized_crime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_financial_crime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_bribery_and_corruption:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_other:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_cybercrime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**regulatory_action:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**law_enforcement_action:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**xinjiang_geospatial:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.traversal.<a href="src/sayari/traversal/client.py">ubo</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The UBO endpoint returns paths from a single target entity to up to 50 beneficial owners. The endpoint is a shorthand for the equivalent traversal query.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.traversal.ubo(
    id="mGq1lpuqKssNWTjIokuPeA",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the entity
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit total values for traversal. Defaults to 10. Max of 50.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset values for traversal. Defaults to 0. Max of 1000.
    
</dd>
</dl>

<dl>
<dd>

**min_depth:** `typing.Optional[int]` — Set minimum depth for traversal. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**max_depth:** `typing.Optional[int]` — Set maximum depth for traversal. Defaults to 4.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[typing.Union[Relationships, typing.Sequence[Relationships]]]` — Set relationship type(s) to follow when traversing related entities. Defaults to has_shareholder, has_beneficial_owner, has_owner, subsidiary_of, and branch_of.
    
</dd>
</dl>

<dl>
<dd>

**psa:** `typing.Optional[bool]` — Also traverse relationships from entities that are possibly the same as any entity that appears in the path. Defaults to traversing possibly same as relationships.
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Union[Country, typing.Sequence[Country]]]` — Filter paths to only those that end at an entity associated with the specified country(ies). Defaults to returning paths that end in any [country](/sayari-library/ontology/enumerated-types#country).
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]` — Filter paths to only those that end at an entity of the specified type(s). Defaults to returning paths that end at any type.
    
</dd>
</dl>

<dl>
<dd>

**sanctioned:** `typing.Optional[bool]` — Filter paths to only those that end at an entity appearing on a watchlist. Defaults to not filtering paths by sanctioned status.
    
</dd>
</dl>

<dl>
<dd>

**pep:** `typing.Optional[bool]` — Filter paths to only those that end at an entity appearing on a pep list. Defaults to not filtering paths by pep status.
    
</dd>
</dl>

<dl>
<dd>

**min_shares:** `typing.Optional[int]` — Set minimum percentage of share ownership for traversal. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**include_unknown_shares:** `typing.Optional[bool]` — Also traverse relationships when share percentages are unknown. Only useful when min_shares is set greater than 0. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**exclude_former_relationships:** `typing.Optional[bool]` — Include relationships that were valid in the past but not at the present time. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**exclude_closed_entities:** `typing.Optional[bool]` — Include entities that existed in the past but not at the present time. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**eu_high_risk_third:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_modern_slavery:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**state_owned:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**formerly_sanctioned:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_terrorism:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_organized_crime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_financial_crime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_bribery_and_corruption:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_other:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_cybercrime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**regulatory_action:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**law_enforcement_action:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**xinjiang_geospatial:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.traversal.<a href="src/sayari/traversal/client.py">ownership</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Ownership endpoint returns paths from a single target entity to up to 50 entities directly or indirectly owned by that entity. The endpoint is a shorthand for the equivalent traversal query.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.traversal.ownership(
    id="mGq1lpuqKssNWTjIokuPeA",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the entity
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit total values for traversal. Defaults to 10. Max of 50.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset values for traversal. Defaults to 0. Max of 1000.
    
</dd>
</dl>

<dl>
<dd>

**min_depth:** `typing.Optional[int]` — Set minimum depth for traversal. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**max_depth:** `typing.Optional[int]` — Set maximum depth for traversal. Defaults to 4.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[typing.Union[Relationships, typing.Sequence[Relationships]]]` — Set relationship type(s) to follow when traversing related entities. Defaults to shareholder_of, beneficial_owner_of, owner_of, has_subsidiary, and has_branch.
    
</dd>
</dl>

<dl>
<dd>

**psa:** `typing.Optional[bool]` — Also traverse relationships from entities that are possibly the same as any entity that appears in the path. Defaults to traversing possibly same as relationships.
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Union[Country, typing.Sequence[Country]]]` — Filter paths to only those that end at an entity associated with the specified country(ies). Defaults to returning paths that end in any country.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]` — Filter paths to only those that end at an entity of the specified type(s). Defaults to returning paths that end at any type.
    
</dd>
</dl>

<dl>
<dd>

**sanctioned:** `typing.Optional[bool]` — Filter paths to only those that end at an entity appearing on a watchlist. Defaults to not filtering paths by sanctioned status.
    
</dd>
</dl>

<dl>
<dd>

**pep:** `typing.Optional[bool]` — Filter paths to only those that end at an entity appearing on a pep list. Defaults to not filtering paths by pep status.
    
</dd>
</dl>

<dl>
<dd>

**min_shares:** `typing.Optional[int]` — Set minimum percentage of share ownership for traversal. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**include_unknown_shares:** `typing.Optional[bool]` — Also traverse relationships when share percentages are unknown. Only useful when min_shares is set greater than 0. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**exclude_former_relationships:** `typing.Optional[bool]` — Include relationships that were valid in the past but not at the present time. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**exclude_closed_entities:** `typing.Optional[bool]` — Include entities that existed in the past but not at the present time. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**eu_high_risk_third:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_modern_slavery:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**state_owned:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**formerly_sanctioned:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_terrorism:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_organized_crime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_financial_crime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_bribery_and_corruption:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_other:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_cybercrime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**regulatory_action:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**law_enforcement_action:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**xinjiang_geospatial:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.traversal.<a href="src/sayari/traversal/client.py">watchlist</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Watchlist endpoint returns paths from a single target entity to up to 50 other entities that appear on a watchlist. The endpoint is a shorthand for the equivalent traversal query.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.traversal.watchlist(
    id="mGq1lpuqKssNWTjIokuPeA",
    limit=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the entity
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit total values for traversal. Defaults to 10. Max of 50.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset values for traversal. Defaults to 0. Max of 1000.
    
</dd>
</dl>

<dl>
<dd>

**min_depth:** `typing.Optional[int]` — Set minimum depth for traversal. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**max_depth:** `typing.Optional[int]` — Set maximum depth for traversal. Defaults to 4.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[typing.Union[Relationships, typing.Sequence[Relationships]]]` — Set relationship type(s) to follow when traversing related entities. Defaults to following 31 relevant relationship types covering ownership, control, and trade.
    
</dd>
</dl>

<dl>
<dd>

**psa:** `typing.Optional[bool]` — Also traverse relationships from entities that are possibly the same as any entity that appears in the path. Defaults to traversing possibly same as relationships.
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.Optional[typing.Union[Country, typing.Sequence[Country]]]` — Filter paths to only those that end at an entity associated with the specified country(ies). Defaults to returning paths that end in any country.
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]` — Filter paths to only those that end at an entity of the specified type(s). Defaults to returning paths that end at any type.
    
</dd>
</dl>

<dl>
<dd>

**sanctioned:** `typing.Optional[bool]` — Filter paths to only those that end at an entity appearing on a watchlist. Defaults to not filtering paths by sanctioned status.
    
</dd>
</dl>

<dl>
<dd>

**pep:** `typing.Optional[bool]` — Filter paths to only those that end at an entity appearing on a pep list. Defaults to not filtering paths by pep status.
    
</dd>
</dl>

<dl>
<dd>

**min_shares:** `typing.Optional[int]` — Set minimum percentage of share ownership for traversal. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**include_unknown_shares:** `typing.Optional[bool]` — Also traverse relationships when share percentages are unknown. Only useful when min_shares is set greater than 0. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**exclude_former_relationships:** `typing.Optional[bool]` — Include relationships that were valid in the past but not at the present time. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**exclude_closed_entities:** `typing.Optional[bool]` — Include entities that existed in the past but not at the present time. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**eu_high_risk_third:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_modern_slavery:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**state_owned:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**formerly_sanctioned:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_terrorism:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_organized_crime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_financial_crime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_bribery_and_corruption:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_other:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**reputational_risk_cybercrime:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**regulatory_action:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**law_enforcement_action:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**xinjiang_geospatial:** `typing.Optional[bool]` — Filter paths to only those that entity with an entity that we have flagged with this risk factor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.traversal.<a href="src/sayari/traversal/client.py">shortest_path</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Shortest Path endpoint returns a response identifying the shortest traversal path connecting each pair of entities.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from sayari.client import Sayari

client = Sayari(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.traversal.shortest_path(
    entities="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entities:** `typing.Union[str, typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

