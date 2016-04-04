from rest_framework import serializers


class FastPassSerializer(serializers.Serializer):
    available = serializers.BooleanField()        

class WaitTimeSerializer(serializers.Serializer):
   fastPass = FastPassSerializer()
   status = serializers.CharField(max_length=200)
   singleRider = serializers.BooleanField()
   postedWaitMinutes = serializers.IntegerField()


class AttractionsSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200, required = False)
    type = serializers.CharField(max_length=200)
    waitTime = WaitTimeSerializer()


class RootAttractionsSerialize(serializers.Serializer):
    entries = serializers.ListField(
        child=AttractionsSerializer()
)

class AggregateAttractionSerialize(serializers.Serializer):
    id = serializers.CharField()
    attractionId = serializers.CharField(max_length = 300)
    date = serializers.DateTimeField(input_formats=["%Y-%m-%d %H"])
    waitTimeAvg = serializers.FloatField()