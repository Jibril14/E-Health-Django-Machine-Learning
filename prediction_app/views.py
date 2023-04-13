from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .models import DiabetesPrediction
import pandas as pd
from data_model.data_model import make_prediction



def index(request):
    return render(request, "index.html")


@login_required
def diabetes_prediction(request):
    make_prediction()
    if request.method == "POST":

        age = float(request.POST.get("age"))
        sex = float(request.POST.get("sex"))
        bmi = float(request.POST.get("bmi"))
        bp = float(request.POST.get("bp"))
        tc = float(request.POST.get("tc"))
        ldl = float(request.POST.get("ldl"))
        hdl = float(request.POST.get("hdl"))
        tch = float(request.POST.get("tch"))
        ltg = float(request.POST.get("ltg"))
        glucose = float(request.POST.get("glucose"))
        user = request.user

        diabetes_model = pd.read_pickle("data_model/model.pickle")
        result = diabetes_model.predict(
            [[age, sex, bmi, bp, tc, ldl, hdl, tch, ltg, glucose]])
        if result >= 0.75:
            result = "Diabetic"
        else:
            result = "No Diabetes"

        prediction = DiabetesPrediction(
            age=age,
            sex=sex,
            bmi=bmi,
            bp=bp,
            tc=tc,
            ldl=ldl,
            hdl=hdl,
            tch=tch,
            ltg=ltg,
            glucose=glucose,
            result=result,
            user=user)
        prediction.save()

        #return HttpResponseRedirect(reverse("diabetes_result"))

    return render(request, "prediction/diabetes.html")

