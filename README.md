# Fivetran Webhooks Example in Python/Flask
Easily accept [Fivetran webhooks](https://fivetran.com/docs/rest-api/webhooks) from the comfort of your terminal!

## Setup
We'll use a really simple Flask server combined with Ngrok to locally test webhooks. 

If you're not familiar with Ngrok, it's a really fast, secure, and easy way to create tunnels to your desktop. This will make it so we can receive webhooks from Fivetran and show them on our local server.

### Prepare
You'll need a Fivetran account and your key and secret that you can find in settings. Find out more in our [getting started guide](https://fivetran.com/docs/rest-api/getting-started).

In addition, head over to Ngrok, create an account, and install it: https://ngrok.com/download

## Dev Environment
- Make sure you have pip installed: `pip -V`
- Make sure you have virtualenv installed: `virtualenv --v` (install with `pip install virtualenv`)

## Install required packages
- Install a virtual env for this project: `python3 -m venv .venv`
- Activate the virtual env: `source .venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`

## Signature Validation
Take advantage of signature validation to ensure that Fivetran is the one sending webhooks to your endpoint. Create a .env file in the root and add a value for `SIGNATURE_SECRET`. Define it as whatever you'd like, for example: `SIGNATURE_SECRET=whatever`. 

## Open a tunnel
Run this from your terminal to open an Ngrok tunnel to port 4242 on your machine (which is what this express server will run on)
- `ngrok http 4242`
- Copy down the https (secure) url that ngrok gives you

## Start the app
`python3 app.py`

### Create a webhook
Use the url that Ngrok gave you and create a webhook. You can utilize our [Postman collection](https://fivetran.com/docs/rest-api/api-tools#fivetranpostmancollection) for this.

POST https://api.fivetran.com/v1/webhooks/account
```
{
  "url": "https://a-bunch-of-numbers.ngrok.io/",
  "events": [
    "sync_end"
  ],
  "active": true,
  "secret": "CHANGE_THIS_VALUE"
}
```
### Test the webhook
Fire a test event to see the response in real time. Make sure to replace `{webhook_id}` with the actual id you got back in the previous step. 

POST https://api.fivetran.com/v1/webhooks/{webhook_id}/test
```
{
  "event": "sync_end"
}
```
### Check the results
You should see a response similar to the following show up on your command line.
```
{
  event: 'sync_end',
  created: '2022-04-09T00:08:12.294Z',
  connector_type: '_connector_type',
  connector_id: '_connector_1',
  destination_group_id: '_destination_1'
}
```

### Build cool stuff!
We can't wait to see what you build on top of our [webhooks](https://fivetran.com/docs/rest-api/webhooks)!

