# -*- coding: utf-8 -*-

#from django.shortcuts import render
#from django.http import HttpResponse
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#from ..models import Journal


#def journal_list(request):
#    journal = Journal.objects.all()

    # try to order groups list
#    order_by = request.GET.get('order_by', '')
#    if order_by in ('title',):
#        journal = journal.order_by(order_by)
#        if request.GET.get('reverse', '') == '1':
#            journal = journal.reverse()

    # paginate groups
#    paginator = Paginator(journal, 1)
#    page = request.GET.get('page')
#    try:
#        journal = paginator.page(page)
#    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
#        journal = paginator.page(1)
#    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
#        groups = paginator.page(paginator.num_pages)

#    return render(request, 'students/journal_list.html',
#        {'groups': groups})

#def journal_add(request):
#    return HttpResponse('<h1>Group Add Form</h1>')

#def journal_edit(request, jid):
#    return HttpResponse('<h1>Edit Group %s</h1>' % jid)

#def journal_delete(request, jid):
#    return HttpResponse('<h1>Delete Group %s</h1>' % jid)
