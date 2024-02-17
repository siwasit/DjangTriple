import os
from openpyxl import load_workbook
from django.shortcuts import redirect, render
from django.http import FileResponse, JsonResponse
from django.contrib.auth import login, logout  
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from rdflib import Graph, Literal, Namespace, RDF, XSD

from .forms import addTriple , RegisterForm

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request, 
            username=username, 
            password=password
        )

        if user is not None:
            # Log user in
            login(request, user)
            return redirect('homepage')
            
    return render(request, 'login.html')

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = RegisterForm()
        print(form)

    return render(request, 'register.html', {'form': form})

def sign_out(request):
    # sign user out
    logout(request)

    # Redirect to sign-in page
    return redirect('/sign-in')

excel_file_path = os.path.join(os.path.dirname(__file__), 'sheet', 'triple_sheet.xlsx')
workbook = load_workbook(excel_file_path)
sheet = workbook.active

@login_required(login_url="/sign-in")
def homepage(request):
    for row in sheet.iter_rows(values_only=True):
        print(row)

    items = []
    row_count = 1
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
            # print(type(triple_add['object']))

            workbook.save(excel_file_path)

            return redirect('homepage')
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
    return redirect('homepage')

def triple_edit(request, triple_id):

    if request.method == "POST":
        triple_form_get = request.POST
        sheet["A" + str(triple_id + 1)] = triple_form_get['editSubject']
        sheet["B" + str(triple_id + 1)] = triple_form_get['editPredicate']
        sheet["C" + str(triple_id + 1)] = triple_form_get['editObject']
        workbook.save(excel_file_path)
        return redirect('homepage')
    else:
        return JsonResponse({'Error': '404 internal server error'})
    
# @login_required(login_url="/sign-in")
def rdffile_export(request):
    graph = Graph()
    ex_person = Namespace("http://example.org/person#")
    foaf = Namespace("http://xmlns.com/foaf/0.1/")

    for i, row in enumerate(sheet.iter_rows(values_only=True), start=1):
        if i==1:
            continue

        name, class_type = row[0].split(':')
        predicate, obj = row[1], row[2]
        person_to_check = (ex_person[name], RDF.type, ex_person[class_type])

        triple_exists = False
        for triple in graph.triples((ex_person[name], RDF.type, None)):
            if triple == person_to_check:
                triple_exists = True
                break

        if not triple_exists:
            # If the triple does not exist, add it to the graph
            graph.add(person_to_check)

        if (ex_person[obj], RDF.type, None) in graph:
            graph.add((ex_person[name], foaf['knows'], ex_person[obj]))
        else:
            graph.add((ex_person[name], ex_person[predicate], Literal(obj)))

    graph_file_path = os.path.join(os.path.dirname(__file__), 'rdffile', 'rdf_graph_file.ttl')
    graph.serialize(destination=graph_file_path, format='turtle')

    response = FileResponse(open(graph_file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="rdf_graph_file.ttl"'

    return response
#rdflib simple example ผมสนใจ Monalisa พระพุทธรูปกับฟัน!!!!!!!!!! ระบบตรวจจับรอยโรคในฟันนนนน, ระบบวิเคราะห์ฉากทัศน์องค์ประกอบพระพุทธรูป กะเพราะปลา