A Python SDK for interacting with the Sayari graph API.

## Using the SDK
Look in the 'example' directory to see how to use the SDK.
- Export your Sayari credentials as ENV variables
  - Alternately, create a `.env` file in the root of this project containing your Sayari creds
    ```json
      CLIENT_ID=YOUR_CLIENT_ID_HERE
      CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE
      ```
- Ensure you have the required dependencies `make setup`
- Install the sdk using `make install`
  - NOTE: before doing this you must be authenticated with gcp `gcloud auth login`
- Run the example **from within the example dir**
  `python3 example.py`

## Documentation
Please see our [docs site](http://documentation.sayari.com) for more info and or to get in touch with us.
