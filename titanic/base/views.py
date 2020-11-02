from django.shortcuts import render
import pickle

def home(request):
    return render(request, 'index.html')

def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    model = pickle.load(open('ml_model.sav', 'rb'))
    scaled = pickle.load(open('scaler.sav', 'rb'))

    prediction = model.predict(scaled.transform([
        [pclass, sex, age, sibsp, parch, fare, C, Q, S]
    ]))
    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'

def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])

    result = getPredictions(pclass, sex, age, sibsp,
                            parch, fare, embC, embQ, embS)

    return render(request, 'result.html', {'result': result})
