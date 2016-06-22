from rest_framework import serializers
from .models import Shortener

class Shortener_Serializer(serializers.HyperlinkedModelSerializer):
    short_url = serializers.CharField(required=False)
    click = serializers.IntegerField(required=False)
    class Meta:
        model = Shortener
        fields = ('url', 'long_url', 'short_url', 'click')

    def get_validation_exclusions(self):
        exclusions = super(Shortener_Serializer, self).get_validation_exclusions()
        return exclusions + ['short_url', 'click']

    def create(self, validated_data):
        print('here')
        instance = Shortener.objects.filter(long_url=validated_data['long_url'])
        if instance:
            instance = instance[0]
            instance.short_url = validated_data.get('short_url', instance.short_url)
            instance.save()
            return instance
        print('create: ' + str(validated_data))
        return Shortener.objects.create(**validated_data)

    def validate(self, attr):
        if 'short_url' in attr:
            instance = Shortener.objects.filter(short_url=attr['short_url'])
            if instance:
                instance = instance.filter(long_url=attr['long_url'])
                if not instance:
                    raise serializers.ValidationError("This shortener is used. Please change another one.")
        return attr

    def update(self, instance, validated_data):
        instance.long_url = validated_data.get('long_url', instance.long_url)
        instance.short_url = validated_data.get('short_url', Shortener.new_url)
        instance.click = validated_data.get('click', instance.click)
        instance.save()
        return instance
