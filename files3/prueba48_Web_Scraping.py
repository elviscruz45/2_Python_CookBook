import requests
import json
import pprint
import random

topics = [
          'health',
          'education',
          'growth',
          'taxes',
          'security',
          'governability',
          'rights',
          'environment',
]
topics_as_params = '&'.join(map(lambda topic: 'topics={}'.format(topic), topics))
questions_url = 'https://api.openpolitica.com/policies/questions?{}'.format(topics_as_params)

sections_response = requests.get(questions_url).json()

sections = sections_response['data']



def build_random_response():
    response = {'answers': []}
    for section in sections:
        # print(section)
        # print('======')
        questions = sections[section]
        for question in questions:
            answers = question['answers']
            chosen_answer = random.choice(answers)

            answer_struct = {
                'questionId': question['question']['id'],
                'answerId': chosen_answer['id']
            }

            response['answers'].append(answer_struct)
    return response

def build_x_random_responses(amount):
    responses = []
    for i in range(amount):
        responses.append(build_random_response())
    return responses

def get_response_headers(response):
    answers = response['answers']
    return ','.join(map(lambda answer: answer['questionId'], answers))

def get_response_as_csv(response):
    answers = response['answers']
    return ','.join(map(lambda answer: answer['answerId'], answers))

def get_top_match_from_result(result):
    data = result['data']
    first_result = data[0]
    return '{},{}'.format(
        first_result['compatibility'],
        first_result['name']
    )

def work(amount):
    results_url = 'https://api.openpolitica.com/policies/results'
    print(get_response_headers)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    responses = build_x_random_responses(amount)

    for response in responses:
        api_response = requests.post(results_url, headers=headers,
                                     data=json.dumps(response))
        print('{},{}'.format(
            get_response_as_csv(response),
            get_top_match_from_result(api_response.json())
            )
        )

# print(get_response_headers(build_random_response()))
work(1000)

# random1 = build_random_response()

# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# api_resp = requests.post('https://api.openpolitica.com/policies/results', 
#                          headers=headers,
#                          data=json.dumps(random1))

# pprint.pprint(get_top_match_from_result(api_resp.json()))