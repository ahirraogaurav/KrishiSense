from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User

# Ranges match what the model was trained on. `preset` values are example fields.
FIELDS = [
    dict(name="N", label="Nitrogen (N)", unit="kg/ha", min=0, max=140, step=1, default=50, help="Ask your soil-test report for the N value."),
    dict(name="P", label="Phosphorus (P)", unit="kg/ha", min=5, max=145, step=1, default=50, help="Phosphorus supports roots and flowering."),
    dict(name="K", label="Potassium (K)", unit="kg/ha", min=5, max=205, step=1, default=50, help="Potassium improves fruit quality and disease resistance."),
    dict(name="temperature", label="Temperature", unit="°C", min=8, max=44, step=0.1, default=25, help="Average temperature during the growing season."),
    dict(name="humidity", label="Humidity", unit="%", min=14, max=100, step=0.1, default=65, help="Average relative humidity."),
    dict(name="ph", label="Soil pH", unit="", min=3.5, max=9.9, step=0.1, default=6.5, help="Below 7 is acidic, above 7 is alkaline."),
    dict(name="rainfall", label="Rainfall", unit="mm", min=20, max=300, step=1, default=100, help="Expected rainfall for the season, in mm per month."),
]

class PredictForm(forms.Form):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        for f in FIELDS:
            self.fields[f["name"]] = forms.FloatField(
                min_value=f["min"], max_value=f["max"], label=f["label"], initial=f["default"],
                error_messages={"min_value": f"{f['label']} must be at least {f['min']}.",
                                "max_value": f"{f['label']} must be at most {f['max']}.",
                                "required": f"Enter a value for {f['label']}.",
                                "invalid": f"Enter a number for {f['label']}."})

class _Styled:
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        for f in self.fields.values():
            f.widget.attrs.setdefault("class", "input")
            f.help_text = f.help_text if f.help_text and "<ul>" not in f.help_text else ""

class LoginForm(_Styled, AuthenticationForm): pass

class ChangePasswordForm(_Styled, PasswordChangeForm): pass

class SignUpForm(_Styled, UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
    def clean_email(self):
        e = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=e).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return e
    def save(self, commit=True):
        u = super().save(commit=False)
        u.email = self.cleaned_data["email"]
        if commit: u.save()
        return u
