from django.shortcuts import render
from django.http import HttpResponseRedirect
from manage import cursor
from .forms import YearForm
from .models import SearchingUsers


def get_year(request):
    print('Получен метод запроса: ', request.method)
    if request.method == 'POST':
        form = YearForm(request.POST)
        print('Сырые данные: ', request.POST)
        if form.is_valid():
            print('Введенное значение: ', form.cleaned_data['year'])
            SearchingUsers.ByYear = form.cleaned_data['year']
            return HttpResponseRedirect('user/search')
        else:
            print('Form is not valid')
    else:
        form = YearForm()
    return render(request, 'users/index.html', {'form': form})


def user_by_year(request):
    print('Получили: ', SearchingUsers.ByYear)
    substring = SearchingUsers.ByYear
    sql = "select first_name, last_name, date_of_birth from user where year(date_of_birth) > %s order by date_of_birth"
    cursor.execute(sql, substring)
    user_info = list()
    for r in cursor:
        sublist = [[r[0], r[1], r[2]]]
        user_info += sublist
    return render(request, 'users/results.html',
                  {'user': user_info, 'substring': substring})