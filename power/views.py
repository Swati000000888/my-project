from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from io import BytesIO


def home_page(request):
       return render(request, "home.html")



def generate_qr_code(request):
       # Example data to encode in QR code
       data = "https://yourwebsite.com/anonymous-access-page"

       # Create QR code
       qr = qrcode.make(data)
       buffer = BytesIO()
       qr.save(buffer, format='PNG')
       buffer.seek(0)

       return HttpResponse(buffer, content_type='image/png')




def anonymous_access_page(request):
    try:
        # Render the template
        return render(request, 'anonymous.html')  # Make sure 'anonymous.html' exists in your templates directory
    except Exception as e:
        # Log the error if needed
        print(f"Error rendering the template: {e}")
        # Handle the error or show a custom error page
        return render(request, 'error.html', {'error_message': 'An error occurred while rendering the page.'})



