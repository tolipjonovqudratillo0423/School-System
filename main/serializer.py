from rest_framework import serializers

from .models import Student,School,Class




class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'



class SchoolSerializer(serializers.ModelSerializer):
    class_ids = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(),many=True,write_only=True)
    classes = ClassSerializer(many=True,read_only=True)
    class Meta:
        model = School
        fields = '__all__'
    def create(self,validated_data):
        class_ids = validated_data.pop('class_ids',None)
        school = School.objects.create(**validated_data)
        if class_ids:
            school.classes.set(class_ids)
        return school
    
    def update(self,instance,validated_data):
        class_ids = validated_data.pop('class_ids',None)

        for attr , value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()

        if class_ids:
            instance.classes.set(class_ids)

        return instance




class StudentSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source = 'student_school.name',read_only = True)
    class Meta:
        model = Student
        fields = '__all__'