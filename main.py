import argparse
import os
import openai

def main(args):
    """
    Get programming question answer with GPT-3
    :return:
    """

    programming_question = args.q
    print("Question: ", programming_question, '\n')

    # Create a prompt for the completion endpoint
    prompt = f"You're a programming expert, what is the answer to this question with code \n\n --- question start ---- \n\n  {programming_question} \n\n  --- question end --- show with code:"

    openai.api_key = os.environ['OPEN_AI']

    response_gpt3 = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Get answer
    answer = response_gpt3['choices'][0]['text']

    print("Answer: ", answer, '\n')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--q', help= "The programming question" )

    args = parser.parse_args()

    main(args)