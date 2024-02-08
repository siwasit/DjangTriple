import os
from django.shortcuts import render
from openpyxl import load_workbook
from django.shortcuts import redirect

from .forms import addTriple

# Create your views here.
# def index(request):
#     return render(request, 'index.html', {'items' : items})

def index(request):
    excel_file_path = os.path.join(os.path.dirname(__file__), 'sheet', 'triple_sheet.xlsx')
    workbook = load_workbook(excel_file_path)
    sheet = workbook.active

    items = []
    row_count = 0
    for i, row in enumerate(sheet.iter_rows(values_only=True), start=1):
        if i==1:
            continue
        items.append((list(str(i-1)) + list(row)))
        row_count = i

    if request.method == "POST":
        form = addTriple(request.POST)
        if form.is_valid():
            triple_add = form.cleaned_data

            sheet["A" + str(row_count + 1)] = triple_add['subject']
            sheet["B" + str(row_count + 1)] = triple_add['predicate']
            sheet["C" + str(row_count + 1)] = triple_add['object']

            workbook.save(excel_file_path)

            return redirect('index')
    else:
        form = addTriple()

    context = {
        'items': items,
        'form': form,
    }

    return render(request, 'index.html', context)

def triple_delete(request):
    return 