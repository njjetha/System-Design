from django.http import HttpResponse, HttpRequest
import json
from mydemo.models import User

def user_request(request: HttpRequest) -> HttpResponse:
    
    if request.method=='GET':
        users=User.objects.all()
        serialized_user=[{
            "id":user.id,
            "username":user.username,
            "name":user.name,
            "email":user.email,
            "address":user.address
        }for user in users]
        return HttpResponse(json.dumps(serialized_user))

    if request.method=='POST':
        body=json.loads(request.body)
        user=User(name=body['name'], email=body['email'], address=body['address'])
        user.save()
        return HttpResponse(json.dumps({'id':user.id, 'name':user.name}))