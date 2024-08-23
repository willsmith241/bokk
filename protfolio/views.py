from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import sys
def home(request):
	return render(request, 'portfolio/index.html')

def gen_pdf(request):
	context = {} # Initialize the context dictionary

	if request.method == "POST":
		name = request.POST.get('name', '')
		about = request.POST.get('about', '')
		pro1 = request.POST.get('pro1', '')
		pd1 = request.POST.get('pd1', '')
		pro2 = request.POST.get('pro2', '')
		pd2 = request.POST.get('pd2', '')
		pro3 = request.POST.get('pro3', '')
		pd3 = request.POST.get('pd3', '')
		ach1 = request.POST.get('ach1', '')
		ad1 = request.POST.get('ad1', '')
		ach2 = request.POST.get('ach2', '')
		ad2 = request.POST.get('ad2', '')
		ad3 = request.POST.get('ad3', '')
		ach3 = request.POST.get('ach3', '')
		address = request.POST.get('address', '')
		number = request.POST.get('number', '')
		email = request.POST.get('email', '')

		cv_file = request.FILES.get('cv')
		if cv_file:
			# Save the file to the media directory
			cv_path = default_storage.save('media/cv.pdf', ContentFile(cv_file.read()))

			# Add the CV path to the context
			cv_url = default_storage.url(cv_path)
			context['cv_url'] = cv_url

		return render(request, 'protfolio/pdf.html', {
			'name': name, 'about': about, 'pro1': pro1, 'pd1': pd1, 'pro2': pro2,
			'pd2': pd2, 'pro3': pro3, 'pd3': pd3, 'ach1': ach1, 'ad1': ad1, 'ach2': ach2,
			'ad2': ad2, 'ad3': ad3, 'ach3': ach3, 'address': address, 'number': number, 'email': email,
			**context # Include the context dictionary
		})

	return render(request, 'portfolio/index.html')

print(sys.path)