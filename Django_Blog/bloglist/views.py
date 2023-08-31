from django.shortcuts import render


def main_page(request):
    data = {
        'login': False
    }
    return render(
        request,
        template_name='bloglist/bloglist.html',
        context=data
    )
