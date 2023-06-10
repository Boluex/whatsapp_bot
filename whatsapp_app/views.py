from django.shortcuts import render
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from.models import *
# from django.view
# Create your views here.
homework='solve x+y=2,who is the current president of Nigeria,What is science,How tall is the eiffel tower,when was the first world war'
notes='i help in:\n -Waec/jamb tutorials\n -Assignments and Educational questions\n -University courses and\n -Adverts'
hint="Hint: If you don't understand you can just type the question e.g Solve this question x+y=2 and 2x + y=4"
math_topics='-Number bases\n -Fractions and Decimals\n -Approximations and Percentages\n -Indices\n -Logarithms and Surds\n -Sets\n -Polynomials\n -Variation\n -Inequalities\n -Progression\n -Binary Operations\n -Matrices and Determinants\n -Euclidean Geometry\n -Mensuration\n -Loci\n -Trigonometry\n -Differentiation\n -Application of differentiation\n -Integration\n -Representation of data\n -Measures of Location\n -Measures of Dispersion\n -Permutation and Combination\n -Probability '
@csrf_exempt
def home(request):
    if request.method=='POST':
        user_msg=request.POST.get('Body','').lower()
        bot_resp=MessagingResponse()
        msg=bot_resp.message()
        msg1=bot_resp.message()
        bot_list_1=['hi','hello','hey','holla','sup','ohayo','answerbot']
        bot_list_2=[]
        for resp in bot_list_1:
            if user_msg in resp:
                msg.body('Hi there, i am answerbot,your personal educational bot' + ' ' + notes + ' ' + '\nWhat are you interested in?')
                msg1.body('what up')
        if 'waec' in user_msg:
            msg.body('What class are you in?\n Art\n Science\n Commercial')
        elif 'art' in user_msg:
            msg.body(f'Alright,Here are the subjects for art students\n Mathematics\n English\n Government\n Literature\n C.R.S or Islam studies\n Which would you like to begin with?')
        elif 'math' in user_msg:
            msg.body(f'Here are our popular jamb topics:\n\n {math_topics}\n\n Which one do you want to start with?')
        elif 'mathematics' in user_msg:
            msg.body(f'Here are our popular jamb topics:\n\n {math_topics}\n\n Which one do you want to start with?')
        elif 'science' in user_msg:
            msg.body(f'Alright,Here are the subjects for science students\n Mathematics\n English\n Physics\n Biology\n Chemistry \n Which would you like to begin with?')
        elif 'physics' in user_msg:
            msg.body(f'Physics\n Hint:Type send subject question to get started to test your skill e.g send phy question(s)')
        elif 'phy' in user_msg:
            msg.body(f'Physics\n Hint:Type send subject question to get started to test your skill e.g send phy question(s)')
        elif 'biology' in user_msg:
            msg.body(f'Biology\n Hint:Type send subject ques`tion to get started to test your skill e.g send bio question(s)')
        elif 'bio' in user_msg:
            msg.body(f'Biology\n Hint:Type send subject question to get started to test your skill e.g send bio question(s)')
        elif 'chemistry' in user_msg:
            msg.body(f'chemistry\n Hint:Type send subject question to get started to test your skill e.g send chem question(s)')
        elif 'chem' in user_msg:
            msg.body(f'chemistry\n Hint:Type send subject question to get started to test your skill e.g send chem question(s)')
        elif 'commercial' in user_msg:
            msg.body(f'Alright,Here are the subjects for science students\n Mathematics\n English\n Commerce\n Economics\n Accounting \n Which would you like to begin with?')
        elif 'commerce' in user_msg:
            msg.body(f'commerce\n Hint:Type send subject question to get started to test your skill e.g send commerce question(s)')
        elif 'economics' in user_msg:
            msg.body(f'economics\n Hint:Type send subject question to get started to test your skill e.g send economics question(s)')
        elif 'accounting' in user_msg:
            msg.body(f'accounting\n Hint:Type send subject question to get started to test your skill e.g send accounting question(s)')
        elif 'assignments' in user_msg:
            msg.body(f"For assignment purpose(s) you can send questions related to {homework} with references to 'who,what,how and when'\n\n")
            msg.body('Solution to assignments can also be generated as pdf or file e.g -write short notes on education as a file or in pdf format')
        return HttpResponse(str(bot_resp))
    return HttpResponse('')