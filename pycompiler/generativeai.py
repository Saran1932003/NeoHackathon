# import openai

# # Set your OpenAI API key here
# api_key = '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'

# # Function to generate comments for code using GPT-3.5
# def generate_comments_for_code(code):
#     openai.api_key = api_key

#     # Define the prompt for the AI model
#     prompt = f"Please provide comments for the following code:\n\n{code}\n\nComments:"

#     # Generate comments using GPT-3.5
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=100
#     )

#     return response.choices[0].text.strip()

# # Create a loop to keep prompting for code and generating comments
# while True:
#     # Get user input (code)
#     user_code = input()

#     if user_code.lower() == 'exit':
#         break  # Exit the loop if the user types 'exit'

#     # Generate comments for the user's code
#     commented_code = generate_comments_for_code(user_code)

#     # Display the generated comments
    
#     print(commented_code)


from flask import Flask, render_template, request

# Import the 'openai' library and define your API key
import openai

app = Flask(__name__)

# Set your OpenAI API key here
api_key = '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'
openai.api_key = api_key

# Function to generate comments for code using GPT-3.5
def generate_comments_for_code(code):
    # Define the prompt for the AI model
    prompt = f"Please provide comments for the following code:\n\n{code}\n\nComments:"

    # Generate comments using GPT-3.5
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )

    return response.choices[0].text.strip()

@app.route('/runcode', methods=['GET', 'POST'])
def index():
    code = ''
    comments = ''

    if request.method == 'POST':
        code = request.form.get('codearea')
        
        # Generate comments for the user's code
        comments = generate_comments_for_code(code)

    return render_template('index.html', code=code, comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
