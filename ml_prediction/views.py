from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HeartAttackRiskModel
from .forms import HeartAttackRiskForm
from django.contrib import messages
import joblib
# Create your views here.
def users_test(mlp,user_test):
    
    user_pred = mlp.predict(user_test)
    if user_pred[0]==1:
        msg= True
    elif user_pred[0]==0:
        msg=False
    return msg

def heart_attack_risk_home_view(request):

    if request.user.is_authenticated:
        form= HeartAttackRiskForm()
        msg=None
        if request.method == 'POST':
            form = HeartAttackRiskForm(request.POST)
            if form.is_valid():
                # form.save()
                age=form.cleaned_data.get('age')
                sex=form.cleaned_data.get('sex')
                cp = form.cleaned_data.get('cp')
                trtbps=form.cleaned_data.get('trtbps')
                chol=form.cleaned_data.get('chol')
                fbs=form.cleaned_data.get('fbs')
                restecg=form.cleaned_data.get('restecg')
                thalachh=form.cleaned_data.get('thalachh')
                exang=form.cleaned_data.get('exang')
                oldpeak=form.cleaned_data.get('oldpeak')
                slp=form.cleaned_data.get('slp')
                caa=form.cleaned_data.get('caa')
                thal=form.cleaned_data.get('thal')
                data = [age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exang,oldpeak,slp,caa,thal]
                mlp = joblib.load('finalized_model.sav')
                user_test = [data]
                # user_test = [[23, 1, 3, 120, 200, 1, 140, 1, 0, 2.3, 0, 0, 1]]
                msg=users_test(mlp, user_test)

                if not msg:
                    messages.success(request, "Patient Has no/less Heart Attack Risk. But, Suggest Patient to follow heart health rules")
                elif msg:
                    messages.error(request, "Patient has Heart Attack Risk!!")
                context={
                    'form':form,
                    'msg':msg
                }
                return render(request,'ml_prediction/heartRisk.html',context)
        context = {
            'form': form,
        }
        return render(request,'ml_prediction/heartRisk.html',context)
    else:
        return redirect('login')