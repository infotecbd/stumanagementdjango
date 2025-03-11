from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student

# Home Page
def HomePage(request):
    users = Student.objects.all()
    context = {'users': users}
    return render (request, 'index.html',  context)
    #return render(request, 'studentapp/index.html', context)



# Add New Student
def Add_Std(request):
    if request.method == "POST":
     
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        course = request.POST.get("course", "").strip()

        if not name or not email or not phone or not course:
            messages.error(request, "Please fill all the fields.")
        elif Student.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered!")
        else:
            Student.objects.create(name=name, email=email, phone=phone, course=course)
            messages.success(request, "Student added successfully!")
            return redirect("homePage")

    return render(request, "add_std.html")

# Edit Student Details
def EditStd(request, id):
    user = get_object_or_404(Student, id=id)

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.course = request.POST.get("course")
  
        user.save()
        messages.success(request, "Student details updated successfully! ✅")
        return redirect("homePage")

    return render(request, "update.html", {"user": user})

# Delete Student
def DeleteStd(request, id):
    if request.method == "POST":
        user = get_object_or_404(Student, id=id)
        user.delete()
        messages.success(request, "Student deleted successfully! 🗑️")
        return redirect('homePage')

    messages.error(request, "Something went wrong! ❌")
    return redirect('homePage')
