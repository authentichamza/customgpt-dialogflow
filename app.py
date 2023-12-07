from flask import Flask, request, make_response, jsonify
from constants import Config
from customgpt_client import CustomGPT
from dialogflow_fulfillment import QuickReplies, WebhookClient, Text, Card, Payload, RichResponse

app = Flask(__name__)
project_id = Config.project_id
CustomGPT.api_key = Config.api_key
CustomGPT.base_url = Config.base_url
@app.route('/webhook', methods=['POST'])
def webhook():
    CustomGPT.api_key = request.headers.get('Authorization').replace('Bearer ', '')
    message_body = request.json['text']
    project_id = request.headers['Project_ID']
    create_conversation = CustomGPT.Conversation.create(project_id=project_id, name='DialogFlow')
    conversation_data = create_conversation.parsed.data
    session_id = conversation_data.session_id

    response = CustomGPT.Conversation.send(project_id=project_id, session_id=session_id, prompt=message_body)
    response_customgpt = response.parsed.data
    openai_response = response_customgpt.openai_response
    res =  {
            'fulfillment_response': {
                'messages': [
                    {
                        'text': {
                            'text': [openai_response]
                        }
                    }
                ]
            }
        }

    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
