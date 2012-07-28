from tastypie.resources import ModelResource
from tracker.models import Member, Report
from tastypie import fields
from tastypie.cache import SimpleCache

class MemberResource(ModelResource):
    
    reports = fields.ToManyField('myapp.api.resources.ReportResource', 'reports')
    
    class Meta:
        queryset = Member.objects.all()
        resource_name = 'member'
        excludes = ['race', 'status_id', 'service', 'margin_2010', 'social_networks', 'facebook_10', 'facebook_status', 'twitter_10', 'twitter_status', 'index_10']
        allowed_methods = ['get']
#        cache = SimpleCache(timeout=600)

class ReportResource(ModelResource):
    member = fields.ToOneField(MemberResource, 'members')

    class Meta:
        queryset = Report.objects.all()
