from django.shortcuts import render, get_object_or_404
from .serializers import *
import json
from django.db.models.functions import Round

# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# class UserView(APIView):
#     def get(self, request, *args, **kwargs):
#         serializer = UserSerializer()   


class PlayerView(APIView):
    def get(self, request):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        user = request.user
        grp = user.groupr2
        queryset = Player.objects.filter(groupr2 = grp)
        serializer = PlayerSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            user.canRatePlayers = False
            user.save()
            playerArray = request.data["playerArray"]
            for player in playerArray:
                id = int(player['id'])
                p = Player.objects.get(pk=id)
                rating = int(player['rating'])
                res = PlayerResponse(player=p,user=user,rating=rating)
                res.save()

            serializer = {"status":"noice"}
            return Response(serializer)
        return Response('{"status": "Unauthorized User"}')

class TeamView(APIView):
    def post(self, request):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        user = request.user
        
        try:
            team = Team.objects.get(user = user)
        except:
            team = Team.objects.create(user=user)
        players = request.data["selectedPlayers"]
        
        if user.canSelectTeam:
            for id in players:
                player = get_object_or_404(Player, pk = id)
                player.teams.add(team)
            team.save() # Jugaad for signal

        user.canSelectTeam = False
        user.save()

        return Response({"status":"hehe"})

    # get selecled 11
    def get(self, request):
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        user = request.user

        try:
            team = Team.objects.get(user = user)
        except:
            team = Team.objects.create(user=user)
        for player in team.teamplayers.all():
            player.final_rating = round(player.final_rating,2)
            player.save()
        players = team.teamplayers.all().order_by("-final_rating")
        serializer = PlayerSerializer(players, many = True)

        return Response(serializer.data)

class UserView(APIView):
    def get(self,request):
        
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        return Response({"status":"Auth details not provided"})

class EmergencyView(APIView):
    def post(self, request):
        try:
            grp = GroupR2.objects.get(name = request.data['name'])
        except:
            return Response({"status" : "Grp not found"})
        print(grp)

        return Response({"status" : "hehe"})

