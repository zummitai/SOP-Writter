import os
import openai
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
openai.api_key = os.getenv('API_KEY')

# def input_param():
#     input_university_name = input("Enter Univeristy Full Name: ")
#     input_field_name = input("Enter Field / Program Full Name: ")
#     input_experince = input("Enter Your Experince: ")

#     return input_university_name,input_field_name,input_experince


def api(university_name, field_name, experince, uni_level):

    input_university_name = university_name
    input_field_name = field_name
    input_experince = experince
    university_level = uni_level

    input_prompt = f'write a one thousand five hundred word statement of purpose essay to the {input_university_name} to study {input_field_name} for the my {university_level} program. {input_experince}. Explain the usefulness of the course and how it will help the development of the economy and myself'

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'{input_prompt}.\n',
        temperature=0.85,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]['text']
