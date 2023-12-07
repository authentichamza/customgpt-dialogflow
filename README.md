# CustomGPT DialogFlow Integration

## Overview

This repository facilitates the integration between DialogFlow CX and CustomGPT, enhancing conversational agents with advanced natural language understanding powered by OpenAI's CustomGPT. Follow the steps below to set up the integration and commence communication with users using the combined capabilities of DialogFlow CX and CustomGPT.

## Installation and Configuration

### 1. Webhook Creation

Commence by setting up a webhook using the provided `app.py` script. The webhook will handle user queries, make CustomGPT stream requests, and format the responses for DialogFlow. The expected response format is as follows:

```json
{
    "fulfillment_response": {
        "messages": [
            {
                "text": {
                    "text": ["your_customgpt_response"]
                }
            }
        ]
    }
}
```

### 2. DialogFlow CX Project Setup

- Create a DialogFlow CX project and navigate to the left side panel.
- Go to `Manage` > `Webhooks` and create a new webhook.
- Add your hosted endpoint to the `Webhook URL`.
- Set the `Webhook Timeout` to 30, and in additional key values, add `Authorization` and `Project-ID` (the ID of the chatbot to chat with). Save the configuration.

### 3. DialogFlow CX Intent Configuration

- In the DialogFlow CX side panel, go to `Build`, click on `Start Page`, and then on `Welcome Intent`.
- In the fulfillment section, remove all existing agent responses to ensure the call to CustomGPT triggers consistently.
- Enable the webhook and select the created webhook from the dropdown.
- Save the configuration.

## Testing

With the setup complete, you are now ready to communicate and test the integrated solution. Ensure that your DialogFlow CX project is properly configured, and the webhook is responding as expected.

Feel free to customize the integration further based on your specific use cases and requirements.
