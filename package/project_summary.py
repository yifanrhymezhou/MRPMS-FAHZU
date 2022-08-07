from flask import Flask
from flask_restful import Resource, Api, request
import pymssql
#from package.connect import connect,cursor
from package.connect import get_db

class Project_Summaries(Resource):
    def get(self):
        sql = "SELECT * FROM KY_PROJ_COMP"
        summaries = get_db(sql, "cp936", "select")     
        return summaries

    def post(self):
        project_input = request.get_json(force=True)
        print(project_input)
        proj_id = project_input['proj_id']
        proj_name = project_input['proj_name']
        proj_management = project_input['proj_management']
        proj_startdate = project_input['proj_startdate']
        proj_enddate = project_input['proj_enddate']
        proj_completion = project_input['proj_completion']
        proj_expansion = project_input['proj_expansion']
        proj_new_enddate = project_input['proj_new_enddate']
        proj_delay_remarks = project_input['proj_delay_remarks']
        sql = "INSERT INTO KY_PROJ_COMP VALUES ('"+ proj_id + "','" + proj_name  + "','" + proj_management  + "','" + proj_startdate  + "','" + proj_enddate  + "','" +  proj_completion  + "','"+ proj_expansion  + "','" + proj_new_enddate + "','" +proj_delay_remarks +"')"
        get_db(sql, "utf8", "update")     
        return project_input

class Project_Summary(Resource):
    def get(self, id):
        sql = "SELECT * FROM KY_PROJ_COMP WHERE id=" + str(id)
        project = get_db(sql, "cp936", "select")     
        #print(project)
        return project
    def delete(self,id):
        sql = "DELETE FROM KY_PROJ_COMP WHERE id=" + str(id)
        get_db(sql, "utf8", "update")  
        return {'msg':'successfully deleted'}
    def put(self, id):
        project_input = request.get_json(force=True)
        proj_id = project_input['proj_id']
        proj_name = project_input['proj_name']
        proj_management = project_input['proj_management']
        proj_startdate = project_input['proj_startdate']
        proj_enddate = project_input['proj_enddate']
        proj_completion = project_input['proj_completion']
        proj_expansion = project_input['proj_expansion']
        proj_new_enddate = project_input['proj_new_enddate']
        proj_delay_remarks = project_input['proj_delay_remarks']
        sql = "UPDATE KY_PROJ_COMP SET proj_id ='"+ proj_id + "',proj_name='" + proj_name  + "',proj_management='" + proj_management  + "',proj_startdate='" + proj_startdate  + "',proj_enddate='" + proj_enddate  + "',proj_completion='" +  proj_completion  + "',proj_expansion='"+ proj_expansion  + "', proj_new_enddate='" + proj_new_enddate + "',proj_delay_remark='" +proj_delay_remarks +"'"
        get_db(sql, "utf8", "update")     
        return project_input
