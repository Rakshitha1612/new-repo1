from django.shortcuts import render
from myapp.models import Student
from myapp.forms import StudentForm
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from myapp.utils import is_json
from myapp.mixins import SerilizeMixin,HttpResponseMixin
import json
@method_decorator(csrf_exempt,name='dispatch')
class StudentCBV(View,HttpResponseMixin,SerilizeMixin):
    def get_rec_by_id(self,id):
        try:
            stud=Student.objects.get(id=id)
        except Exception:
            stud=None
        return stud
    def get(self,request,*args,**kwargs):
        data=request.body #data is a json data it may be empty or it may contain id
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'invalid'})
            return self.render_to_http_response(json_data,status=404)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            stud=self.get_rec_by_id(id)
            if stud is None:
                json_data=json.dumps({'msg':'invalid record'})
                return self.render_to_http_response(json_data,status=404)
            json_data=self.fun([stud])
            return self.render_to_http_response(json_data)
        qs=Student.objects.all() # if id is None
        json_data=self.fun(qs)
        return self.render_to_http_response(json_data)
    def post(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'invalid'})
            return self.render_to_http_response(json_data,status=404)
        p_data=json.loads(data)
        form=StudentForm(p_data)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Successfully created the record'})
            return self.render_to_http_response(json_data)
        if form.errors():
            json_data=json.dumps({'msg':'Form submission error'})
            return self.render_to_http_response(json_data,status=404)
    def put(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'Not a json data'})
            return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'invalid id'})
            return self.render_to_http_response(json_data,status=404)
        stud=self.get_rec_by_id(id)
        if stud is None:
            json_data=json.dumps({'msg':'invalid record'})
            return self.render_to_http_response(json_data,status=404)
        original_data={'name':stud.name,'rollno':stud.rollno,'marks':stud.marks,'address':stud.address}
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=stud)
        if form.is_valid():
           form.save(commit=True)
           json_data=json.dumps({'msg':'Updation is successful'})
           return self.render_to_http_response(json_data)
        if form.errors:
           json_data=json.dumps({'msg':'Error in form submission'})
           return self.render_to_http_response(json_data,status=404)
    def delete(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'Not a json data'})
            return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'Invalid id'})
            return self.render_to_http_response(json_data,status=404)
        stud=self.get_rec_by_id(id)
        if stud is None:
            json_data=json.dumps({'msg':'invalid record'})
            return self.render_to_http_response(json_data,status=404)
        status,item=stud.delete()
        if status==1:
            print("Deleted successfully")
        else:
            print("Deletion error")