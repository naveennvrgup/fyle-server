from django.shortcuts import render
from django.db.models import Q
from .models import Branches
from .serializers import BranchSerializer, AutoCompleteInputSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status


@api_view(['get'])
def BranchAutocompleteView(request):
    q = request.GET.get('q', '')
    limit = request.GET.get('limit', '')
    offset = request.GET.get('offset', '')

    errs = {}

    if len(limit) == 0:
        limit = 10
    elif not limit.isnumeric():
        errs['limit'] = 'Limit should be a natural number'
    else:
        limit = int(limit)

    if len(offset) == 0:
        offset = 0
    elif not offset.isnumeric():
        errs['limit'] = 'Offset should be a natural number'
    else:
        offset = int(offset)

    # on case invalid pagination request
    if len(errs.keys()) > 0:
        return Response(errs, status=status.HTTP_400_BAD_REQUEST)

    queryset = Branches.objects.filter(branch__istartswith=q).order_by('ifsc')
    count = queryset.count()
    queryset = queryset[offset: offset+limit]
    serializer = BranchSerializer(queryset, many=True)
    branches = serializer.data

    return Response({
        'q': q,
        'offset': offset,
        'limit': limit,
        'count': count,
        'branches': branches
    }, status=status.HTTP_200_OK)


@api_view(['get'])
def BranchSearchView(request):
    q = request.GET.get('q', '')
    limit = request.GET.get('limit', '')
    offset = request.GET.get('offset', '')

    errs = {}

    if len(limit) == 0:
        limit = 10
    elif not limit.isnumeric():
        errs['limit'] = 'Limit should be a natural number'
    else:
        limit = int(limit)

    if len(offset) == 0:
        offset = 0
    elif not offset.isnumeric():
        errs['limit'] = 'Offset should be a natural number'
    else:
        offset = int(offset)

    # on case invalid pagination request
    if len(errs.keys()) > 0:
        return Response(errs, status=status.HTTP_400_BAD_REQUEST)

    queryset = Branches.objects.filter(
        Q(ifsc__icontains=q) |
        Q(branch__icontains=q) |
        Q(address__icontains=q) |
        Q(city__icontains=q) |
        Q(district__icontains=q) |
        Q(state__icontains=q)
    ).order_by('ifsc')
    count = queryset.count()
    queryset = queryset[offset: offset+limit]
    serializer = BranchSerializer(queryset, many=True)
    branches = serializer.data

    return Response({
        'q': q,
        'offset': offset,
        'limit': limit,
        'count': count,
        'branches': branches
    }, status=status.HTTP_200_OK)
