from django.shortcuts import render


def nature_view(request):
    # we added additional folder "nature_facts" in templates to make sure index.html will be unique path in case we have other templates in other apps named index.html
    # this is because Django is collecting all templates, when scanning for them and we might have conflicting names/paths
    return render(request, "nature_facts/index.html", {"activity": "climbing"})
