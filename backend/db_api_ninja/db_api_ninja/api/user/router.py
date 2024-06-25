import jwt
import uuid
from datetime import datetime, timedelta
from ninja import Router
from django.shortcuts import get_object_or_404
from .models import CustomUser, UserOut, UserIn
from django.contrib.auth import authenticate, login, logout

router = Router(tags=["user"])

@router.get("/", response=list[UserOut])
def get_users(request):
    data = CustomUser.objects.all()
    return data

@router.get("/{uuid}", response=UserOut)
def get_user(request, uuid: uuid.UUID):
    data = get_object_or_404(CustomUser, uuid=uuid)
    return data

@router.post("/")
def create_user(request, payload: UserIn):
    data = CustomUser.objects.create_user(**payload.dict())
    return {"id": data.id}

@router.put("/{uuid}")
def update_employee(request, uuid: uuid.UUID, payload: UserIn):
    data = get_object_or_404(CustomUser, uuid=uuid)
    for attr, value in payload.dict().items():
        setattr(data, attr, value)
    data.save()
    return {"success": True}

@router.delete("/{uuid}")
def delete_employee(request, uuid: uuid.UUID):
    data = get_object_or_404(CustomUser, uuid=uuid)
    data.delete()
    return {"success": True}

@router.post("/{uuid}/password")
def change_passwor(request, uuid: uuid.UUID, payload: UserIn):
    payload = payload.dict()
    username = payload["username"]
    password = payload["password"]
    user =  get_object_or_404(CustomUser, username=username, uuid=uuid)
    user.set_password(password)
    user.save()
    return {"success": True}

# Auth only
# auth = Router(tags=["auth"])

# @auth.post("/login")
# def user_login(request, payload: UserIn ):
#     payload = payload.dict()
#     username = payload["username"]
#     password = payload["password"]
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return {"success": True}
#     else:
#         return {"success": False}

# @auth.post("/logout")
# def user_logout(request):
#     logout(request)
#     return {"success": True}
