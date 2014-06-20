from django.http import HttpResponse
from django.core.urlresolvers import reverse

from twilio.twiml import Response
from django_twilio.decorators import twilio_view

from .models import Visitor, Message


def home(request):
    return HttpResponse('')


def user(request, user_id):
    return HttpResponse(user_id)


def messages(request, user_id):
    # return json to indicate number of messages, and their contents
    return HttpResponse(user_id + ' messages')


@twilio_view
def welcome(request, message=''):
    if message == '':
        message = 'Welcome to Hill Valley.'
    if 'welcome_message' in request.session:
        message = request.session['welcome_message']
        del request.session['welcome_message']
    r = Response()
    r.say(message)
    # if we are logged in return options, otherwise ask for login
    if 'visitor' in request.session:
        r.redirect(reverse('twiliorouter:welcome_options'))
    else:
        # try to login
        r.redirect(reverse('twiliorouter:login'))
    return r


@twilio_view
def welcome_options(request):
    r = Response()
    # check they are actually logged in
    if 'visitor' in request.session:
        visitor = request.session['visitor']
        r.say('welcome {0:s}'.format(visitor['name']))
        with r.gather(
            numDigits=1,
            timeout=10,
            finishOnKey='*',
            action=reverse('twiliorouter:handle_welcome_options'), method='POST'
        ) as g:
            g.say(
                'press 1 to listen to messages, or press 2 to enter a number you want to connect to'
            )


@twilio_view
def handle_welcome_options(request):
    if 'visitor' in request.session:
        visitor = request.session['visitor']
        choice = int(request.POST.get('Digits', '0'))
        r = Response()
        if choice == 1:
            # user wants to listen to their message - try to login
            r.redirect(
                reverse('twiliorouter:twilio_messages'), args=[visitor['number']])
        elif choice == 2:
            # user wants to contact another user
            r.redirect(reverse('twiliorouter:connect'))
        else:
            request.session['welcome_message'] = 'Option not available'
            r.redirect(reverse('twiliorouter:welcome'))
    else:
        request.session['welcome_message'] = 'Option not available'
        r.redirect(reverse('twiliorouter:welcome'))
    return r


@twilio_view
def login(request):
    r = Response()
    with r.gather(
        numDigits=6,
        timeout=10,
        finishOnKey='*',
        action=reverse('twiliorouter:handle_login'), method='POST'
    ) as g:
        g.say(
            'please enter your 6 digit phone number to continue'
        )
    return r


@twilio_view
def handle_login(request):
    access_code = request.POST.get('Digits', '')
    r = Response()
    try:
        visitor = Visitor.objects.get(access_code=access_code)
        request.session['visitor'] = {
            'id': visitor.id,
            'name': visitor.user.first_name,
            'number': visitor.access_code
        }
        # this was a valid user code - redirect to inbox
        r.redirect(
            reverse('twiliorouter:twilio_messages', args=[visitor.access_code]))
        return r
    except Visitor.DoesNotExist:
        request.session['welcome_message'] = 'Number not recognised'
        r.redirect(reverse('twiliorouter:welcome'))
    return r


@twilio_view
def twilio_messages(request):
    # this endpoint is used to return the twiml response for the inbox count
    r = Response()
    if 'visitor' in request.session:
        visitor = request.session['visitor']
        # get active messages for this user
        # todo - only return active messages (i.e. not expired)
        num_new_messages = 0
        num_old_messages = 0
        messages = Message.objects.filter(recipient__id=visitor['id'])
        for message in messages:
            if message.accessed == False:
                num_new_messages += 1
            else:
                num_old_messages += 1

        if num_new_messages > 0:
            r.say('user inbox')
        else:
            r.say('you have no new messages')
    else:
        request.session['welcome_message'] = 'Number not recognised'
        r.redirect(reverse('twiliorouter:welcome'))
    return r


@twilio_view
def connect(request):
    # we are trying to connect to another account
    r = Response()
    if 'visitor' in request.session:
        with r.gather(
            numDigits=6,
            timeout=10,
            finishOnKey='*',
            action=reverse('twiliorouter:handle_connect'), method='POST'
        ) as g:
            g.say(
                'please enter the 6 digit number you want to connect to'
            )
    else:
        request.session['welcome_message'] = ''
        r.redirect(reverse('twiliorouter:welcome'))
    return r


@twilio_view
def handle_connect(request):
    recipient_number = request.POST.get('Digits', '')
    r = Response()
    if 'visitor' in request.session:
        try:
            recipient = Visitor.objects.get(access_code=recipient_number)
            request.session['recipient'] = {
                'id': recipient.id,
                'name': recipient.user.first_name,
                'number': recipient.access_code
            }
            # record a message
            r.say(
                'The person you tried to call is unavailable. Please leave a message')
            r.record(maxLength=30, action=reverse(
                'twiliorouter:handle_record')
            )
        except Visitor.DoesNotExist:
            request.session['welcome_message'] = 'Number not recognised'
            r.redirect(reverse('twiliorouter:connect'))
    else:
        request.session[
            'welcome_message'] = 'You need to enter your phone number'
        r.redirect(reverse('twiliorouter:welcome'))
    return r


@twilio_view
def handle_record(request):
    r = Response()
    return r
