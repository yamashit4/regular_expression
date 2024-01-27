from django.shortcuts import render,redirect
import re

# Create your views here.
def index(regex_app):
    return render(regex_app, 'regex_app/index.html')

def confirm(request):
    if request.method == 'POST':
        name = re.sub('\s',"",request.POST.get("name"))
        age = request.POST.get("age")
        zip_code = request.POST.get("zip_code")
        tel = request.POST.get("tel")

        context = {
            "name":name,
            "age":age,
            "zip_code":zip_code,
            "tel":tel,
        }

        error_message = {
            "name":None,
            "age":None,
            "zip_code":None,
            "tel":None,
        }

        #ageの処理
        if not re.match('^[0-9]+$',context["age"]):
            error_message['age'] = 'ageは1〜3桁の半角数字のみで入力して下さい'
            age = None
        #zip_codeの処理
        if not re.match('^\d{3}-?\d{4}$',context["zip_code"]):
            error_message['zip_code'] = 'Zip Codeは全7桁の半角数字を入力して下さい(ハイフンはあってもなくてもよい)。'
            zip_code = None
        #telの処理
        if not re.match('^\d{3}-?\d{4}-?\d{4}$',context["tel"]):
            error_message['tel'] = 'Cell_phoneは全9桁の半角数字を入力して下さい(ハイフンはあってもなくてもよい)。'
            tel = None
        #全て一致した時の処理
        if re.match('^[0-9]+$',context["age"]) and re.match('^\d{3}-?\d{4}$',context["zip_code"]) and re.match('^\d{3}-?\d{4}-?\d{4}$',context["tel"]):
            return render(request,'regex_app/confirm.html',context)
    
    return render(request, 'regex_app/index.html', {'context': context, 'error_message': error_message})
