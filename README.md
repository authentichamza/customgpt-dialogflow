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
![Webhook_Creation](https://github.com/authentichamza/customgpt-dialogflow/assets/43203240/1307e7e6-f6f1-41ae-9ea7-dd430f340095)
- Create a DialogFlow CX project and navigate to the left side panel.
- Go to `Manage` > `Webhooks` and create a new webhook.
- Add your hosted endpoint to the `Webhook URL`.
- Set the `Webhook Timeout` to 30, and in additional key values, add `Authorization` and `Project-ID` (the ID of the chatbot to chat with). Save the configuration.
![Screenshot from 2023-12-07 04-53-59](https://github.com/authentichamza/customgpt-dialogflow/assets/43203240/53a38fb6-2020-4a3e-a162-e5cbac098403)

### 3. DialogFlow CX Intent Configuration
- In the DialogFlow CX side panel, go to `Build`
- Click on `Start Page`, and then on `Welcome Intent`.
- ![Screenshot from 2023-12-07 04-42-34](https://github.com/authentichamza/customgpt-dialogflow/assets/43203240/3559f086-5ee6-4b48-9aeb-a2b5b0a8192b)

- In the fulfillment section, remove all existing agent responses to ensure the call to CustomGPT triggers consistently.
- ![Screenshot from 2023-12-07 05-26-54](https://github.com/authentichamza/customgpt-dialogflow/assets/43203240/d0c39109-0496-4bd0-9949-a092e8c9fdf9)
- Enable the webhook and select the created webhook from the dropdown.
- Save the configuration.

## Testing

With the setup complete, you are now ready to communicate and test the integrated solution. Ensure that your DialogFlow CX project is properly configured, and the webhook is responding as expected.

Feel free to customize the integration further based on your specific use cases and requirements.
