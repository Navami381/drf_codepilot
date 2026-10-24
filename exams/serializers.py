from rest_framework import serializers
from exams.models import AssessmentModel
from datetime import datetime

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssessmentModel
        fields="__all__"
        read_only_fields=["id","created_by","end_time","created_at","updated_at"]

    def validate(self,validated_data):
        exam_date=validated_data.get("exam_date")

        if exam_date<datetime.today().date():
            raise serializers.ValidationError("invalid date..")
        return validated_data

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be greater than 0 hours.")
        if value > 4:
            raise serializers.ValidationError("Exam duration cannot exceed 4 hours.")
        return value