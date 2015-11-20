# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2014 Ait-Mlouk Addi <http://www.aitmlouk-addi.info>.

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv,fields
import time
from datetime import date
from datetime import datetime

class hr_employee(osv.osv): 
    _name='hr.employee'
    _inherit = 'hr.employee' 
    
    """def _get_age(self, cr, uid, ids, name, arg, context={}):
        data={}
        for object_parent in self.browse(cr,uid,ids):
            data[object_parent.id] = 0
            if object_parent.birthday:
                data[object_parent.id]=(datetime.now()-datetime.strptime(object_parent.birthday,"%Y-%m-%d")).days/356
        return data"""
    
    def onchange_birthday(self,cr,uid,ids,birthday,context={}):
        data={} 
        if birthday:
            data['age'] =(datetime.now()-datetime.strptime(birthday,"%Y-%m-%d")).days/356 
        else:birthday = False
        return {'value' : data }
    
    _columns = {
           #'age' : fields.function(_get_age,type='integer',string=u'Age'),
           'age' : fields.integer(u'Age'),
        }
    
hr_employee()