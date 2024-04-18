A Python SDK for interacting with the Sayari graph API.

## Using the SDK
Look in the 'example' directory to see how to use the SDK.
- Export your Sayari credentials as ENV variables (**Required if using the `hello-world.py` example)
  - Alternately, if you use the dotenv package, you can create a `.env` file in the root of this project containing your Sayari creds (see `smoke-test.py` for an example of this)
    ```json
      CLIENT_ID=YOUR_CLIENT_ID_HERE
      CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE
      ```
- Ensure you have the required dependencies `make setup`
- Install the sdk using `make local-install`
- Run the smoke test example
  `python3 examples/smoke-test.py`

## Documentation
Please see our [docs site](http://documentation.sayari.com) for more info and or to get in touch with us.
