# # api/apps/raffle/views.py
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAdminUser, IsAuthenticated
# from rest_framework import status
# from .models import Raffle
# from .serializers import RaffleSerializer
# from api.apps.core.permissions.permissions import IsAuthenticatedWithToken
#
#
# class RaffleListView(APIView):
#     permission_classes = [IsAuthenticatedWithToken]
#
#     def get(self, request):
#         raffles = Raffle.objects.all()
#         serializer = RaffleSerializer(raffles, many=True)
#         return Response(serializer.data)
#
#
# class RaffleCreateView(APIView):
#     permission_classes = [IsAdminUser]
#
#     def post(self, request):
#         serializer = RaffleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class RaffleDetailView(APIView):
#     permission_classes = [IsAuthenticatedWithToken]
#
#     def get(self, request, pk):
#         try:
#             raffle = Raffle.objects.get(pk=pk)
#             serializer = RaffleSerializer(raffle)
#             return Response(serializer, status=status.HTTP_200_OK)
#         except ObjectDoesNotExist:
#             return Response({
#                 "error": "Raffle does not exist"
#             }, status=status.HTTP_404_NOT_FOUND)
#
#
# class RaffleUpdateView(APIView):
#     def get_object(self, pk):
#         try:
#             return Raffle.objects.get(pk=pk)
#         except ObjectDoesNotExist:
#             return Response( {"error": "Raffle does not exist"}, status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, pk):
#         raffle = self.get_object(pk)
#         serializer = RaffleSerializer(raffle, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class RaffleDeleteView(APIView):
#     def get_object(self, pk):
#         try:
#             return Raffle.objects.get(pk=pk)
#         except ObjectDoesNotExist:
#             return Response({"error": "Raffle does not exist"}, status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, pk):
#         raffle = self.get_object(pk)
#         raffle.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
