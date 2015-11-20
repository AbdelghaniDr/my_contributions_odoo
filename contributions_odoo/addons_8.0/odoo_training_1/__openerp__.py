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
{
    "name": u"Odoo Training",
    'complexity': "normal",
    "version": "1.0",
    "depends": ["base","hr"],
    "author": "Ait-MLouk Addi",
    "sequence":10,
    "website" : "http://www.aitmlouk-addi.info/",
    "category": "functionality",
    'description' : " Functions  to get employee age",
    "init_xml": [],
    'update_xml': [
                    'hr_view.xml',
                   ],
    'demo_xml': [],
    'application': False,
    'installable': True,
    'active': False,

}

