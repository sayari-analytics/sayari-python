A Python SDK for interacting with the Sayari graph API.

## Using the SDK
Look in the 'example' directory to see how to use the SDK.
- Export your Sayari credentials as ENV variables
  - Alternately, create a `.env` file in the root of this project containing your Sayari creds
    ```json
      CLIENT_ID=YOUR_CLIENT_ID_HERE
      CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE
      ```
- Ensure you have the required dependancies `make setup`
- Install the sdk using `make install`
  - NOTE: before doing this you must be authenticated with gcp `gcloud auth login`
- Run the example **from within the example dir**
  `python3 example.py`

## Development
### Fern
Fern is used to generate the api bindings, these live in /src/sayari/python and will be updated via CI whenever the fern spec is updated.
**Do not manually edit any code in that directory**

### Building + Publishing
While still under development, this SDK will be published to a private registry.

#### Authenticating to push to the private registry
In order to push to the repository:
- Authenticate to GCP `gcloud auth login`
- Update your `.pypirc` (found at $HOME/.pypirc) to include
  ```toml
  [distutils]
  index-servers =
      sayari-python
  
  [sayari-python]
  repository: https://us-east1-python.pkg.dev/sayari-datastore/sayari-python/
  ```

#### Building and publishing
Once authenticated you can use `make gcp-build-push` to build and publish the SDK.

Note: Publish will fail if the release already exists in the registry. Be sure to increment the version tag in `projects.toml` before building.

## Testing
Tests have been written. Use `make test` to see results
