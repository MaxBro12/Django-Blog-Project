from django.shortcuts import render

data = {
    'login': False,
    'title': 'Новости',
}


def news_list(request):

    return render(
        request,
        template_name='bloglist/bloglist.html',
        context=data
    )


def create_new(request):
    data['title'] = 'Создать пост'

    return render()
