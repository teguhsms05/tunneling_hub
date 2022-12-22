# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect

from .forms import GroupDomainCreate
from .models import *
from .access import AccessDomain

import logging

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def register_cpanel(request):
    #load template
    load_template = request.path.split('/')[1]
    if request.method == 'POST':
        try:
            post = request.POST.copy()
            groupDomain = post['group_domain']
            cpanelDomain = post['cpanel_domain']
            createdBy = request.user.username
            #domainName = subDomain+'.'+groupDomain
            
            if not GroupDomain.objects.filter(group_domain=groupDomain).exists():
                # or set several values from dict
                post.update({
                    'group_domain': groupDomain, 
                    'cpanel_domain': cpanelDomain,
                    'created_by': createdBy
                    })
                # and update original POST in the end
                request.POST = post
                form = GroupDomainCreate(request.POST)
                if form.is_valid():
                    form.save()
                    record = GroupDomain.objects.get(group_domain=groupDomain)   
                    record.created_by = createdBy
                    record.save(update_fields=['created_by'])
                    
                    messages.success(request, "Entry Data")
                    
            else:
                messages.warning(request, 'Duplicate Data Entry')
                context = {'form' : GroupDomainCreate(), 'cpanel' : GroupDomain.objects.all() }
                return render(request, 'home/register-cpanel.html', context)
                
        except Exception as err:
            print (err)
        #domainUsed = AccessDomain(domainName, groupDomain).register()
        return redirect('home:register_cpanel')
    context = {'form_cpanel' : GroupDomainCreate(), 'cpanel' : GroupDomain.objects.all()}
    context['segment'] = load_template
    return render(request, 'home/register_cpanel.html', context)

@login_required(login_url="/login/")
def delete_cpanel(request, task_id):
    context = {}
    try:
        # mengambil data domain yang akan dihapus berdasarkan task id
        task = GroupDomain.objects.get(pk=task_id)
        # menghapus data dari table Domain
        task.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.error(request, 'Delete Data')
        return redirect('home:register_cpanel')
    
    except GroupDomain.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")  
def update_cpanel(request, task_id):
    if request.method == 'POST':
        try:
            post = request.POST.copy()
            groupDomain = post['group_domain']
            cpanelDomain = post['cpanel_domain']
            data = {'group_domain': groupDomain, 'cpanel_domain': cpanelDomain}
            
            form_update = GroupDomain.objects.get(id=task_id)
            for key, value in data.items():
                setattr(form_update, key, value)
            form_update.save()

            messages.success(request,"Update Data")
        except Exception as e:
            print (e)
        return redirect('home:register_cpanel')

    data_update = GroupDomain.objects.get(id=task_id)
    initial_data = {
        'group_domain': data_update.group_domain,
        'cpanel_domain': data_update.cpanel_domain
    }
    context = {'form_cpanel': GroupDomainCreate(initial=initial_data), 'cpanel': GroupDomain.objects.all(), 'gp_domain': initial_data['group_domain']}
    return render(request, 'home/register_cpanel.html', context)