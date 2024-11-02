import speech_recognition as sr
import win32com.client
import os
import webbrowser
import datetime
import google.generativeai as genai
import requests

def get_news(apikey, query="top-headlines", category=None, country=None):
    apikey = "94cafaa9b0b14caf9bd024f93a3534de"
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": apikey,
        "q": query,
        "category": category,
        "country": country,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors

    data = response.json()
    articles = data['articles']
    print(articles)
    return articles

speaker = win32com.client.Dispatch("SAPI.SpVoice")
chatStr=""
def chat(query):
    global chatStr
    chatStr += f"User: {query}\n Jarvis: "

    genai.configure(api_key="AIzaSyCNx2ZR3HiSHL67Y6BpYlq45Ai7OC_3MO0")

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(chatStr)
    chatStr += f"{response.text}\n"

    print(f"Jarvis: {response.text}")
    speaker.Speak(response.text)
    return response.text

def ai(prompt):
    genai.configure(api_key="AIzaSyCNx2ZR3HiSHL67Y6BpYlq45Ai7OC_3MO0")
    text = f"Gemini response for prompt: {prompt} \n **************************\n\n"
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(prompt)

    print(response.text)
    text += response.text
    if not os.path.exists("Gemini"):
        os.mkdir("Gemini")

    with open(f"Gemini/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error have occured"

if __name__ == '__main__':
    userInput = input("Press enter")


    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"],
                 ["wikipedia", "https://wikipedia.com"],
                 ["instagram", "https://instagram.com"],
                 ["google", "https://google.com"],
                 ["anime", "https://hianime.to"],
                 ["hianime", "https://hianime.to"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                speaker.Speak(f"Opening {site[0]}")

        if "open music" in query.lower():
            musicPath = "C:/Users/LENOVO/Music/Music/New folder/Discord.mp3"
            os.startfile(musicPath)

        elif "shutdown" in query.lower():
            os.system("shutdown -s -t 10")
            print("System will shut down in 5 seconds")

        elif "time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"The time is {strfTime}")

        elif "open app" in query.lower():
            os.system()

        elif "artificial intelligence".lower() in  query.lower():
            ai(prompt=query)

        elif "using ai".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            speaker.Speak("It was nice talking to you")
            exit();

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        elif "news".lower() in query.lower():
            apikey = "94cafaa9b0b14caf9bd024f93a3534de"
            news_articles = get_news(apikey, country="us")
            print(news_articles)

            #for article in news_articles:
                #print(article['title'])
                #speaker.Speak(article['title'])

        elif query == "":
            takeCommand()

        elif "restart".lower() in query.lower():
            os.system("shutdown -r -t 10")

        elif "abort shutdown".lower() in query.lower():
            os.system("shutdown -a")

        elif "cancel shutdown".lower() in query.lower():
            os.system("shutdown -a")

        elif "abort restart".lower() in query.lower():
            os.system("shutdown -a")

        elif "cancel shutdown".lower() in query.lower():
            os.system("shutdown -a")

        else:
            print("Chatting....")
            chat(query)

        #speaker.Speak(query)
