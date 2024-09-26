# infoimages/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import MyModel, Region, District
from .serializers import MyModelSerializer
from .utils import check_api_token  # utils.py dan funksiya import qilish

@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        # Tokenni tekshirish
        token_error = check_api_token(request)
        if token_error:
            return token_error  # Agar token xato bo'lsa, xato javobini qaytarish

        try:
            # Rasmni yuklash uchun request.FILES dan foydalaning
            data = request.POST  # POST ma'lumotlarini olish
            photo = request.FILES.get('photo')  # photo faylini olish

            # Regionni tekshirish va saqlash
            region_name = data.get('region')
            region, created = Region.objects.get_or_create(name=region_name)

            # Districtni tekshirish va saqlash
            district_name = data.get('district')
            district, created = District.objects.get_or_create(name=district_name, region=region)

            # Ma'lumotlarni saqlash
            my_model_instance = MyModel(
                barcode=data.get('barcode'),
                fish=data.get('fish'),
                date=data.get('date'),
                region=region,
                district=district,
                post_name=data.get('post_name'),
                photo=photo  # Rasmni saqlash
            )

            my_model_instance.save()
            return JsonResponse({'message': 'Data saved successfully'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
