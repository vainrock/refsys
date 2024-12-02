from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
import random
import time

# Simulate sending an authorization code
AUTH_CODES = {}  # Temporary in-memory storage for phone numbers and codes

@api_view(['POST'])
def send_auth_code(request):
    phone_number = request.data.get('phone_number')
    if not phone_number:
        return Response({"error": "Phone number is required"}, status=400)

    # Simulate sending a 4-digit code
    auth_code = random.randint(1000, 9999)
    AUTH_CODES[phone_number] = auth_code
    time.sleep(2)  # Simulate delay

    return Response({"message": f"Authorization code sent to {phone_number}"})

@api_view(['POST'])
def verify_auth_code(request):
    phone_number = request.data.get('phone_number')
    code = int(request.data.get('code', 0))
    
    if AUTH_CODES.get(phone_number) != code:
        return Response({"error": "Invalid code"}, status=400)

    # Check if the user already exists
    user, created = User.objects.get_or_create(phone_number=phone_number)
    serializer = UserSerializer(user)

    if created:
        return Response({"message": "User registered successfully", "user": serializer.data})
    return Response({"message": "User already exists", "user": serializer.data})

@api_view(['POST'])
def set_invite_code(request):
    phone_number = request.data.get('phone_number')
    inviter_code = request.data.get('invited_by')

    try:
        user = User.objects.get(phone_number=phone_number)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    if user.invited_by:
        return Response({"error": "Invite code already set"}, status=400)

    if not User.objects.filter(invite_code=inviter_code).exists():
        return Response({"error": "Invalid invite code"}, status=400)

    user.invited_by = inviter_code
    user.save()

    return Response({"message": "Invite code set successfully"})

@api_view(['GET'])
def get_user_profile(request, phone_number):
    try:
        user = User.objects.get(phone_number=phone_number)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    invitees = User.objects.filter(invited_by=user.invite_code)
    invitee_list = [invitee.phone_number for invitee in invitees]

    return Response({
        "phone_number": user.phone_number,
        "invite_code": user.invite_code,
        "invited_by": user.invited_by,
        "invitees": invitee_list,
    })

