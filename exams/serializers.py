from rest_framework import serializers
from exams.models import AssessmentModel
from datetime import datetime

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssessmentModel
        fields="__all__"
        read_only_fields=["id","created_by","end_time"]

        def validate(self,validated_data):
            exam_date=validated_data.get("exam_date")

            if exam_date<datetime.today().date():
                raise serializers.ValidationError("invalid date..")
            return validated_data