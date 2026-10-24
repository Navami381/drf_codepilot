from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView,DestroyAPIView,RetrieveAPIView

from exams.serializers import AssessmentSerializer
from exams.models import AssessmentModel
from exams.permissions import IsOwner

from datetime import datetime,timedelta

# Create your views here.
class AssessmentCreateListView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        instance=AssessmentModel.objects.filter(created_by=request.user)
        serailizer_instance=AssessmentSerializer(instance,many=True)
        return Response(data=serailizer_instance.data)
    
    def post(self,request):
        form_data=request.data
        serailizer_instance=AssessmentSerializer(data=form_data)
        if serailizer_instance.is_valid():
            serailizer_instance.save(created_by=request.user)              
            # cleaned_data=serailizer_instance.validated_data    #def perform_create(self,serializer)
            # exam_date=cleaned_data.get("exam_date")             #serializers.save(created_by=self.request.user) must inherit from createAPIVIEW
            # start_time=cleaned_data.get("start_time")
            # duration=cleaned_data.get("duration")
            # end_date_time = datetime.combine(exam_date,start_time)+timedelta(hours=duration)
            # end_time = end_date_time.time()
            # qs=AssessmentModel.objects.create(created_by=request.user,**cleaned_data,end_time=end_datetime.time())
            # serializer_instance=AssessmentSerializer(qs)

            return Response(data=serailizer_instance.data)
        else:
                return Response(data=serailizer_instance.errors)

class AssessmentRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
     authentication_classes=[authentication.TokenAuthentication]
     permission_classes=[permissions.IsAdminUser]
     serializer_class=AssessmentSerializer
     queryset=AssessmentModel.objects.all()


