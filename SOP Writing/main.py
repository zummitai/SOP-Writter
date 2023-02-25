import os
import openai

openai.api_key = "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"

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

    input_prompt = f'write a statement of purpose letter to a {input_university_name} in the field of {input_field_name} with having an experience of {input_experince} for the {university_level}'

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'{input_prompt}.\n',
        temperature=0.7,
        max_tokens=2500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]['text']

