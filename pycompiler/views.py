# import sys

# from django.shortcuts import render

# # Create your views here.

# #create index function

# def index(request):
#     return render(request, 'index.html')

# def runcode(request):

#     if request.method == "POST":
#         codeareadata = request.POST['codearea']

#         try:
#             #save original standart output reference

#             original_stdout = sys.stdout
#             sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

#             #execute code

#             exec(codeareadata)  #example =>   print("hello world")

#             sys.stdout.close()

#             sys.stdout = original_stdout  #reset the standard output to its original value

#             # finally read output from file and save in output variable

#             output = open('file.txt', 'r').read()

#         except Exception as e:
#             # to return error in the code
#             sys.stdout = original_stdout
#             output = e


#     #finally return and render index page and send codedata and output to show on page

#     return render(request , 'index.html', {"code":codeareadata , "output":output})



import sys
import openai
from django.shortcuts import render

# Set your OpenAI API key here
api_key = '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'

# Function to generate comments for code using GPT-3.5
def generate_comments_for_code(code):
    openai.api_key = api_key

    # Define the prompt for the AI model
    prompt = f"Please provide comments for the following code:\n\n{code}\n\nComments:"

    # Generate comments using GPT-3.5
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )

    return response.choices[0].text.strip()

# Create your views here.

# create index function
def index(request):
    return render(request, 'index.html')

# from django.shortcuts import render

# def second_page(request):
#     # Add your view logic here
#     return render(request, 'second_page.html')  # Render the HTML template for the second page


# modify the runcode function
def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            # Save original standard output reference
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')  # Change the standard output to the file we created

            # Execute code
            exec(codeareadata)  # Example: print("hello world")

            sys.stdout.close()
            sys.stdout = original_stdout  # Reset the standard output to its original value

            # Finally read output from file and save it in the output variable
            output = open('file.txt', 'r').read()

            # Generate comments for the user's code using the generative AI
            commented_code = generate_comments_for_code(codeareadata)

        except Exception as e:
            # To return an error in the code
            sys.stdout = original_stdout
            output = e
            commented_code = ""

        # Finally return and render the index page and send code data, output, and commented code to show on the page
        return render(request, 'index.html', {"code": codeareadata, "output": output, "commented_code": commented_code})

