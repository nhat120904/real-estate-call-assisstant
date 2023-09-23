ENDPOINT = "https://localhost:9200"
USERNAME = "elastic"
PASSWORD = "jHrRY8wc_*W9T+loisSn"

# import elasticsearch
from elasticsearch import Elasticsearch #, helpers
from searcher import generate_text
from extract_keyword import extract_keyword
import json
from converter import convert_to_string, convert_to_dict, merge_keyword
from fix import auto_correct_query

f = open("current_prompt.txt", "r")
current_prompt = f.read()
current_prompt = convert_to_dict(current_prompt)

def search(input, current_res):
    CERT_FINGERPRINT = "c948ba36b6348dd0b412a7998403f5d3a5e8c1e8c50b950292d49230a9e15cde"
    es = Elasticsearch(
        "https://localhost:9200",
        ssl_assert_fingerprint=CERT_FINGERPRINT,
        basic_auth=("elastic", PASSWORD)
    )
    # print(es.ping())

    try:
        prompt = extract_keyword(input)
        prompt = convert_to_dict(prompt)
        print(prompt)
        print(current_prompt)
        prompt = merge_keyword(prompt, current_prompt)
        f = open("current_prompt.txt", "w")
        f.write(convert_to_string(prompt))
        f.close()
        # current_prompt = prompt
        # print
        prompt = convert_to_string(prompt)
        current_res.value = "[pr]\n" + prompt

        print(prompt)
        prompt = input + "\n" + prompt
        response = generate_text(prompt)
        print(response)
    except:
        response = "null"
    if response == "null":
        response = {}
    else:
        try:
            response = json.loads(response)
            # print("sucessfully parsed response")
        except:
            try:
                response = response + "\n" + "}"
                response = json.loads(response)
            except:
                try:
                    response = response + "\n" + "}"
                    response = response + "\n" + "}"
                    response = json.loads(response)
                except:
                    response = ""
    if response == {} or response == "":
        response = {}
    else:
        response = auto_correct_query(response)
    query = {
        "size": 5,
    }
    try:
        query["query"] = response["query"]
    except:
        pass
    try:       
        query["sort"] = response["sort"]
    except:
        pass
    print(response)
    print(query)
    try:
        if response != "null":
            res = es.search(index='house', body=query)
            title = [x['_source']  for x in res['hits']['hits']]
            count = res['hits']['total']['value'] 
            title = str(title)
            count = str(count)
            if title == []:
                title = "No data found"
        else:
            title = "null"
            count = "0"
        data = "(Result count: " + count +" ."+ "Your data is: " + title + ")\n"+ " .You must provide super short answer (phone call conversation style). Answer must not have newline characters or a list.".upper()
        print(data)
    except Exception as e:
        # print(e)
        data = "(Your data is: " + "No data found" + ")\n" + " .You must provide answer within a paragraph like in a conversation."
        print(data)
    return input + " " + data