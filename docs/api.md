# Api endpoint
all api endpoint information and how its use is.
## /api/clear_chat GET

Clears the global chat

### Usage

url :https://CHAT-SYNC-URL.com/api/clear_chatapi-key=APIKEY/ADMINCODE

### Responses

- "response" : "chat cleared", this means the the operation has been run successfully
- {"response" : "no api key"}, no api key has been provided
- {"response" : "Invalid api key"}, api key is invalid

## /api/send_msg POST
Sends a message to global chat
### Usage

Url: "https://CHAT-SYNC-URL.com/api/send-msg"

Body / Json: ```'{'username': "USERNAME-FOR-MSG, 'message': 'MESSAGE-TO-SEND'}'```

### Responses

- {"response" : "message sent"}, successfully sent message

- invalid method, http method besides POST was used

## /api/get_msgs GET

fetches global chat info

### Usage

url: "https://CHAT-SYNC-URL.com/api/get_msgs

### Responses

- Global chat contents





