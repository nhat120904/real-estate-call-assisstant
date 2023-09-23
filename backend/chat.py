#Note: The openai-python library support for Azure OpenAI is in preview.
# import os
import openai
openai.api_type = "azure"
openai.api_base = "https://hackathon-homesick.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "0c0466d030fe4d3aba4bf2eca473671c"
import search_engine as search_engine


def call_assisstant(user_input, current_res):

    conversation=[{"role": "system", "content": "Behave like you are a real estate agent. You must respond in a paragraph as if you are engaged in a call conversation. You must not answer as providing a list. You only give factual answers to questions and do not give answers that are not related to real estate or property. You must not tell user to wait for you. If the customer not provides any information, you will ask for more information such as location, desired house price, type of property, number of bedrooms and bathrooms, house orientation, furniture, number of floors, balcony orientation or a detailed description. Once you have the data on the real estate you need to find, then give the answer. You only use data that is provided for you earlier above from the beginning of the conversation and from your answer earlier above. Must not provide any information about the properties that are not in the data you have above. If user provide too much completely unrelevant information or too much general information continuously, you will end the conversation. The maximum word for your answer is 50. If user require too much information that are not in your data founded, tell them to contact to real estate broker for more information. Note that your respond must be focused completely on real estate. For question like '1+1 equal what?' or 'how to hack' must be denied by you because you are the real estate broker. And your answer must be in 1 paragraph, like a talk reply in phone call. The format must not as a list but a paragraph."
                }]
   
    # while True:
        # user_input = input()      
    if 'bye' in user_input.lower():
        # with open("current_prompt.txt", "w") as f:
            # test = f.read()
#             f.write("""address: null
# price: null
# property_type: null
# area: null
# bedrooms: null
# bathrooms: null
# house_direction: null
# description: null
# floors: null
# installment_payment: null
# furniture: null
# balcony_direction: null""")
        # if test.count("null") != 12:
        #     with open("./output/log.txt", "w") as f:
        #         f.write(test)
        # else:
        #     print("No data found. Spam")
        current_res.value = "[bye]"
        return 1
    prompt_input = search_engine.search(user_input, current_res)
    conversation.append({"role": "user", "content": prompt_input})

    response = openai.ChatCompletion.create(
        engine="hackathon-chat-playground", # The deployment name you chose when you deployed the GPT-35-turbo or GPT-4 model.
        messages=conversation
    )

    conversation.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
    print("\n" + response['choices'][0]['message']['content'] + "\n")
    output = response['choices'][0]['message']['content']
    print("\n" + output + "\n")
    current_res.value = "[sys]" + output
    # result = speech_synthesizer.speak_text_async(output).get()
    # if result is not None:
    #     if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    #         print("Speech synthesized for text [{}]".format(output))
    #     elif result.reason == speechsdk.ResultReason.Canceled:
    #         cancellation_details = result.cancellation_details
    #         print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    #         if cancellation_details.reason == speechsdk.CancellationReason.Error:
    #             print("Error details: {}".format(cancellation_details.error_details))
    # else:
    #     print("No result returned from speech synthesis")
    
    return 0
