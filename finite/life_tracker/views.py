from django.shortcuts import render
from .models import Profile

def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    weeks_lived = profile.weeks_lived()
    weeks_remaining = profile.weeks_remaining()
    life_completion = profile.life_completion_percentage()

    context = {
        "weeks_lived": weeks_lived,
        "weeks_remaining": weeks_remaining,
        "life_completion": round(life_completion, 2),
        "total_weeks": profile.expected_lifespan * 52
    }
    return render(request, "life_tracker/dashboard.html", context)
