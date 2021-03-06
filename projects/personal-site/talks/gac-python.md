{% load static %}
class: inverse, spaced
layout: true
background-image: url({% static "img/nac.svg" %})

---

class: middle

# Google Actions with Python

- These Slides: [bit.ly/py-gac](http://bit.ly/py-gac)
- My Google Action: [Neutron Academy](https://www.neutron.academy/)
- Paul Bailey: [@PizzaPanther](https://twitter.com/pizzapanther)
- Developer @ [SaltStack](https://saltstack.com/)

---

# What is a Google Action?

Actions on Google lets you extend the functionality of the Google Assistant with your own actions.

- conversational interface
- works with voice and text
- works on
    - voice-activated speakers
    - Android phones
    - iPhones
    - Android TVs
    - and more!

---

# Ways to Build Your App

https://developers.google.com/actions/

- Use a template *(no coding required)*
- Use a platform:
  - Coding may or may not be required
  - More opinionated
  - [DialogFlow](https://dialogflow.com/docs/integrations/google-assistant)
  - [Converse](https://get.converse.ai/docs/google-actions)
  - [PullString](https://www.pullstring.com/blog/pullstring-announces-support-for-actions-on-google?hsCtaTracking=2c9d2014-7829-4d37-9a6e-26ca844a5171%7Cf929e814-a0cb-4869-aaea-5408025029e0&__hstc=184034361.e41fcd15c37387327b67c2a2869bb15f.1474952963337.1489506642691.1489718912868.167&__hssc=184034361.1.1489784561986&__hsfp=976989674)
  - [gupshup](https://www.gupshup.io/developer/googlehome)
- Build it from Scratch! ([Actions SDK](https://developers.google.com/actions/sdk/))

---

# Technical Overview

<table style="border-collapse: collapse; margin: 0 auto; height: 500px;">
  <tr>
    <td>
      <img src="{% static "img/talk.gif" %}" alt="talk to google" style="height: 130px;">
    </td>
    <td>
      <pre style="font-size: 14px;">
#1: OK Google
"Talk to      =>
MY APP"


<= #4: Google
speaks response


#5: User
     responds =>


<= #8: Google
speaks response
      </pre>
    </td>
    <td>
      <img src="{% static "img/google.gif" %}" alt="google home" style="width: 220px;">
    </td>
    <td>
      <pre style="font-size: 14px;">
#2: New Intent =>
(conversation id)



<= #3: Respond


#6 Response
    Intent =>
    
    
<= #7 Response
      </pre>
    </td>
    <td>
      <img src="{% static "img/cat.gif" %}" alt="cat programming" style="height: 140px;">
    </td>
  </tr>
</table>

---

# Building Your Action

[Sample App](https://github.com/pizzapanther/google-actions-python-example)

1. Create your project in the [actions console](https://console.actions.google.com/).
2. Upload your [actions.json](https://github.com/pizzapanther/google-actions-python-example/blob/master/actions.json)
  - https://developers.google.com/actions/tools/gactions-cli
3. Fill out your app info.
4. Create code to process intents.
5. Enjoy fame and fortune!

<iframe src="https://giphy.com/embed/m2knL5cKZZxMQ" width="215" height="180" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

---

# Testing Your App

- Using the simulator
- Using a real device

---

# Input and Output

- [Sample Input](https://github.com/pizzapanther/google-actions-python-example/blob/master/sample-input.json)
  - [App Request API Reference](https://developers.google.com/actions/reference/rest/Shared.Types/AppRequest)
- [Sample SSML Output](https://github.com/pizzapanther/google-actions-python-example/blob/master/sample-output.json)
  - [App Response API Reference](https://developers.google.com/actions/reference/rest/Shared.Types/AppResponse)
  
---

# Security

- [Verifying a request](https://developers.google.com/actions/reference/rest/verify-requests)

<iframe src="https://giphy.com/embed/VTc8cXZN2Vpf2" width="200" height="141" frameBorder="0" class="giphy-embed" allowFullScreen style="float:right"></iframe>

```python
from google.oauth2 import id_token
from google.auth.transport import requests

request = requests.Request()

try:
  id_info = id_token.verify_oauth2_token(
    token, request, PROJECT_ID)
    
except:
  self.set_status(401)
  self.write('Token Mismatch')
```

---

class: tight

# Tools and Libraries

**Testing/Development**
- [ngrok](https://ngrok.com/)

**Web Development**
- [Tornado](http://www.tornadoweb.org/)
- [Flask](http://flask.pocoo.org/)
- [Django](https://www.djangoproject.com/)

---

class: tight

# Tools and Libraries

**Language Processing**
- [DialogFlow](http://dialogflow-python-client-v2.readthedocs.io/)
- [NLTK](https://www.nltk.org/)
- [spaCy](https://spacy.io/)
- [scikit-learn](http://scikit-learn.org/)
- [polyglot](http://polyglot.readthedocs.io/)
- [Rasa Core (dialogue)](https://rasa.com/docs/core/)
- [Rasa NLU](http://rasa.com/docs/nlu/)
- [Gensim](https://radimrehurek.com/gensim/)

**Text to Speech**
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/)
- [Amazon Polly](https://aws.amazon.com/polly/)

---

class: middle, center

# Questions?

<iframe src="https://giphy.com/embed/3o7buirYcmV5nSwIRW" width="480" height="269" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/emoji-idk-thinking-3o7buirYcmV5nSwIRW">via GIPHY</a></p>
