A Python SDK for interacting with the Sayari graph API.

Look in the 'example' directory to see how to use the SDK.
- Create a `.env` file containing your sayari api credentials
  - This file should look like this (with values updated)
  ```json
    CLIENT_ID=YOUR_CLIENT_ID_HERE
    CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE
    ```
- Ensure you have the required dependancies `pip install -r sdk/requirements.txt`
- Run the example **from the same directory as the .env file**
  `python3 example.py`
