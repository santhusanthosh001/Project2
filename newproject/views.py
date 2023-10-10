from django.shortcuts import render

from django.shortcuts import render

def add_numbers(request):
    # Perform the addition
    num1 = 5  # Replace with your first number
    num2 = 3  # Replace with your second number
    result = num1 + num2

    # Pass the result to the template
    context = {'num1': num1, 'num2': num2, 'result': result}
    return render(request, 'addition.html', context)


# Create your views here.
