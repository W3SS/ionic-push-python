# Ionic Push Python
Ionic Push Service client in Python for Google App Engine

Currently, this is a very simple client that only creates push notifications and is specific to Google App Engine.

## Getting Started
Just copy the `ionic_push_client.py` module to your GAE project and
fill in the blanks, i.e.:

```Python
    PUSH_API_TOKEN = '<put-your-app-api-token-here>'
    PUSH_PROFILE = '<put-your-profile-tag-here>'
```

### Example
The following code snippet demonstrates the way this client can be
used in order to send push notifications.

```Python
import IonicPushClient

msg = 'The message will be received by your app users'
tokens = ['user-1-token', 'user-2-token', ...]
result = IonicPushInterface.push(tokens=tokens, alert=msg)
if result:
    # do whatever you want with the result
```
