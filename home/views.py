from django.http import HttpResponse
from django.shortcuts import render



import requests
import json


# set the endpoint URL
url = "https://api.pawan.krd/v1/completions"

# set the authorization header
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer pk-glhEMkJtzsgemigfLmoYhGszGeQJMNEkSMKKsSsRngWxWMxr"
}

def fact(user_input):
    messages = []
    messages.append({"role": "system", "content": "AI BEST FRIEND"})

    print("Your new assistant is ready FOR PUBLISH!")
    while input != "quit()":
        message = user_input
        messages.append({"role": "user", "content": message})
        data = {
        "model": "text-davinci-003",
        "prompt": "The following is a conversation with an AI Friend. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nDOST: I am your AI Friend created by Iron Force. How can I help you today?\nHuman: {} ?".format(messages),
        "temperature": 0.7,
        "max_tokens": 128,
        }
        response = requests.post(url, headers=headers, json=data)
        result = json.loads(response.text)
        reply = result["choices"][0]["text"]
        messages.append({"role": "friend", "content": reply})
        reply="\n" + reply + "\n"
        return reply

def index(request):
    responseme='Hello'
    if request.method == 'POST':
        # Get the user's input from the form
        user_input = request.POST.get('article')

        #API
        responseme=fact(user_input)
    
        # Return the prediction to the user on a new page
        print(responseme)            
        return render(request,'index.html',{'bot':responseme,'user1':user_input})
    else:
        return render(request,'index.html',{'bot':responseme})
