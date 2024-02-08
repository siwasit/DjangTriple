import os
from django.shortcuts import render
from openpyxl import load_workbook
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse

from .forms import addTriple, editTriple

# Create your views here.
# def index(request):
#     return render(request, 'index.html', {'items' : items})

excel_file_path = os.path.join(os.path.dirname(__file__), 'sheet', 'triple_sheet.xlsx')
workbook = load_workbook(excel_file_path)
sheet = workbook.active

def index(request):

    items = []
    row_count = 0
    for i, row in enumerate(sheet.iter_rows(values_only=True), start=1):
        if i==1:
            continue
        items.append((list(str(i-1)) + list(row)))
        row_count = i

    if request.method == "POST":
        add_form = addTriple(request.POST)
        if add_form.is_valid():
            triple_add = add_form.cleaned_data

            sheet["A" + str(row_count + 1)] = triple_add['subject']
            sheet["B" + str(row_count + 1)] = triple_add['predicate']
            sheet["C" + str(row_count + 1)] = triple_add['object']

            workbook.save(excel_file_path)

            return redirect('index')
    else:
        add_form = addTriple()

    context = {
        'items': items,
        'add_form': add_form,
    }

    return render(request, 'index.html', context)

def triple_delete(request, triple_id):
    sheet.delete_rows(idx=triple_id + 1)
    workbook.save(excel_file_path)
    return redirect('index')

def triple_edit(request, triple_id):

    print(triple_id)   
    if request.method == "POST":
        form = editTriple(request.POST)
        print(form)
        if form.is_valid():
            triple_edit = form.cleaned_data 
            print(triple_edit)
            # sheet["A" + str(triple_id + 1)] = triple_edit['subject']
            # sheet["B" + str(triple_id + 1)] = triple_edit['predicate']
            # sheet["C" + str(triple_id + 1)] = triple_edit['object']
            # workbook.save(excel_file_path)
            return redirect('index')
    else:
        form = editTriple()

    return redirect('index')