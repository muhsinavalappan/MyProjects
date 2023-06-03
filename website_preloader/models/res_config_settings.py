# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Muhsina V (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    """ Inhering to Add a field to enable delivery slot"""
    _inherit = 'res.config.settings'

    enable_website_preloader = fields.Boolean(
        string='Website Preloader',
        config_parameter='WebsitePreloader.enable_website_preloader',
        default=True)
    loader_style = fields.Selection([
        ('bean eater', 'bean eater'),
        ('cube', 'cube'),
        ('disk', 'disk'),
        ('dual', 'dual'),
        ('gear', 'gear'),
        ('infinity', 'infinity'),
        ('pulse', 'pulse'),
        ('ripple', 'ripple'),
        ('spinner', 'spinner'),
    ], config_parameter='website_preloader.loader_style', default='dual')
