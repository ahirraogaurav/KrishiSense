from collections import Counter
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from . import ml
from .crop_data import CROPS, crop_ctx
from .forms import FIELDS, ChangePasswordForm, PredictForm, SignUpForm
from .models import Prediction

def home(request):
    ctx = {"sample_crops": [crop_ctx(k) for k in ("rice", "mango", "banana", "maize", "grapes", "coffee")]}
    if request.user.is_authenticated:
        qs = request.user.predictions.all()
        top = Counter(qs.values_list("crop", flat=True)).most_common(1)
        ctx.update(recent=qs[:3], total=qs.count(), favourite=crop_ctx(top[0][0]) if top else None)
        for p in ctx["recent"]: p.c = crop_ctx(p.crop); p.pct = round(p.confidence * 100)
    return render(request, "advisor/home.html", ctx)

def signup(request):
    if request.user.is_authenticated: return redirect("home")
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        messages.success(request, "Welcome! Your account is ready.")
        return redirect("predict")
    return render(request, "advisor/auth_form.html", {"form": form, "title": "Create your account", "button": "Sign up", "alt": "login", "alt_text": "Already registered? Log in"})

class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = "advisor/auth_form.html"
    success_url = reverse_lazy("home")
    success_message = "Your password was changed."
    extra_context = {"title": "Change password", "button": "Save new password"}

@login_required
def predict(request):
    form = PredictForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        vals = form.cleaned_data
        top = ml.predict(vals, top=3)
        p = Prediction.objects.create(user=request.user, crop=top[0][0], confidence=top[0][1],
                                      top3=[[c, round(pr, 4)] for c, pr in top], **vals)
        return redirect("result", pk=p.pk)
    fields = [dict(f, value=form[f["name"]].value() if form.is_bound else f["default"],
                   errors=form[f["name"]].errors) for f in FIELDS]
    return render(request, "advisor/predict.html", {"fields": fields})

@login_required
def result(request, pk):
    p = get_object_or_404(Prediction, pk=pk, user=request.user)
    top = [dict(crop_ctx(c), pct=round(pr * 100)) for c, pr in p.top3]
    return render(request, "advisor/result.html", {"p": p, "best": top[0], "top": top, "notes": ml.soil_notes(p.values()),
        "readings": [(f["label"], f["unit"], getattr(p, f["name"])) for f in FIELDS]})

@login_required
def history(request):
    items = list(request.user.predictions.all())
    for p in items:
        p.c = crop_ctx(p.crop); p.pct = round(p.confidence * 100)
    return render(request, "advisor/history.html", {"items": items})

@login_required
@require_POST
def delete_prediction(request, pk):
    get_object_or_404(Prediction, pk=pk, user=request.user).delete()
    messages.success(request, "Prediction deleted.")
    return redirect("history")

def crop_list(request):
    return render(request, "advisor/crops.html", {"crops": [crop_ctx(k) for k in sorted(CROPS)]})

def crop_detail(request, key):
    if key not in CROPS: return redirect("crops")
    used = request.user.predictions.filter(crop=key).count() if request.user.is_authenticated else 0
    return render(request, "advisor/crop_detail.html", {"c": crop_ctx(key), "used": used})
