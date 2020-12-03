from rest_framework import serializers
from .models import Bucket, Pipe
from datetime import datetime, timedelta
from django.utils import timezone

class PipeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    pipe_name = serializers.CharField(max_length=200)
    dest_bsb_number = serializers.IntegerField()
    dest_account_number = serializers.IntegerField()
    dest_account_name = serializers.CharField(max_length=200)
    dest_balance = serializers.IntegerField()
    amount_dollar =serializers.IntegerField()
    amount_percent = serializers.IntegerField()
    statement_text = serializers.CharField(max_length=200)

    #destination_id is like supporter_id
    destination_id = serializers.IntegerField()
    bucket_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Pipe.objects.create(**validated_data)

class PipeDetailSerializer(PipeSerializer):

    def update(self, instance, validated_data):
        instance.pipe_name = validated_data.get('pipe_name', instance.pipe_name)
        instance.dest_account_number = validated_data.get('dest_account_number',instance.dest_account_number)
        instance.dest_bsb_number = validated_data.get('dest_bsb_number', instance.dest_bsb_number)
        instance.dest_account_name = validated_data.get('dest_account_name', instance.dest_account_name)
        instance.dest_balance = validated_data.get('dest_balance', instance.dest_balance)
        instance.amount_dollar = validated_data.get('amount_dollar', instance.amount_dollar)
        instance.amount_percent = validated_data.get('amount_percent', instance.amount_percent)
        instance.statement_text = validated_data.get('statement_text',instance.statement_text)
        instance.bucket_id = validated_data.get('bucket_id', instance.bucket_id)
        instance.destination_id = validated_data.get('destination_id',instance.destination_id)
    
        instance.save()
        return instance

    def delete(self, instance, validated_data):
        instance.pipe_name = validated_data.get('pipe_name', instance.pipe_name)
        instance.dest_account_number = validated_data.get('dest_account_number',instance.dest_account_number)
        instance.dest_bsb_number = validated_data.get('dest_bsb_number', instance.dest_bsb_number)
        instance.dest_account_name = validated_data.get('dest_account_name', instance.dest_account_name)
        instance.dest_balance = validated_data.get('dest_account_balance', instance.dest_account_balance)
        instance.amount_dollar = validated_data.get('amount_dollar', instance.amount_dollar)
        instance.amount_percent = validated_data.get('amount_percent', instance.amount_percent)
        instance.statement_text = validated_data.get('statement_text',instance.statement_text)
        instance.bucket_id = validated_data.get('bucket_id', instance.bucket_id)
        instance.destination_id = validated_data.get('destination_id',instance.destination_id)
        instance.save()
        return instance

class BucketSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(default=timezone.now())
    # is_open = serializers.SerializerMethodField()
    is_open = serializers.BooleanField()
    source_bsb_number = serializers.IntegerField()
    source_account_number =serializers.CharField(max_length=200)
    source_account_name =serializers.CharField(max_length=200)
    source_balance =serializers.IntegerField()
    # owner = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Bucket.objects.create(**validated_data)

    
class BucketDetailSerializer(BucketSerializer):
    pipes= PipeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.source_bsb_number = validated_data.get('source_bsb_number', instance.source_bsb_number)
        instance.source_account_number = validated_data.get('source_account_number', instance.source_account_number)
        instance.source_account_name = validated_data.get('source_account_name', instance.source_account_name)
        instance.source_balance = validated_data.get('source_balance', instance.source_balance)

        instance.save()
        return instance

    def delete(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.source_bsb_number = validated_data.get('source_bsb_number', instance.source_bsb_number)
        instance.source_account_number = validated_data.get('source_account_number', instance.source_account_number)
        instance.source_account_name = validated_data.get('source_account_name', instance.source_account_name)
        instance.source_balance = validated_data.get('source_balance', instance.source_balance)
        instance.save()
        return instance