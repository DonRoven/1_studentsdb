# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from studentsdb.settings import ADMIN_EMAIL


class ContactForm(forms.Form):
    form_email = forms.EmailField(label=u"Ваша Емейл Адреса")
    subject = forms.CharField(label=u'Заголовок листа', max_length=128)
    message = forms.CharField(label=u'Текст повідомлення', max_length=3000, widget=forms.Textarea)

def contact_admin(request):
    # check if form was posted
    if request.method == 'POST':
        # create e form instanse and populate it with data from the request:
        form = ContactForm(request.POST)

        # check whether user data is valid:
        if form.is_valid():
            # send mail
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_mail = form.cleaned_data['from_mail']

            try:
                send_mail(subject, message, from_mail, [ADMIN_EMAIL])
            except Exception:
                message = u'Під час відправки листа виникла непередбачувана помилка.'\
                        u'Спробуйте скористатися даною формою пізніше'

            else:
                message = u'Повідомлення успішно надіслане!'

            # redirect to same contact page with success message
            return  HttpResponseRedirect(u'%s?status_message=%s' % (reverse('contact_admin'), message))

        # if there was not POST render blank forn
        else:
            form = ContactForm()

        return render(request, 'contact_admin/form.html', {'form': form})
