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
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    """ Inhering to Add fields to enable social media sharing and styles"""
    _inherit = 'res.config.settings'

    enable_social_media_sharing_style = fields.Boolean(
        string='Product Social Media Sharing',
        config_parameter='style_social_media_sharing.enable')
    icon_style = fields.Selection([
        ('style1', 'Style-1'),
        ('style2', 'Style-2'),
        ('style3', 'Style-3'),
        ('style4', 'Style-4'),
        ('style5', 'Style-5'),
        ('style6', 'Style-6'),
        ('style7', 'Style-7'),
        ('style8', 'Style-8'),
        ('style9', 'Style-9'),
        ('style10', 'Style-10'),
        ('style11', 'Style-11')],
        config_parameter='style_social_media_sharing.icon_style')

    facebook_icon = fields.Boolean(
        "Facebook", config_parameter='style_social_media_sharing.facebook')
    whatsapp_icon = fields.Boolean(
        "WhatsApp", config_parameter='style_social_media_sharing.whatsapp')
    twitter_icon = fields.Boolean(
        "Twitter", config_parameter='style_social_media_sharing.twitter')
    linkedin_icon = fields.Boolean(
        "LinkedIn", config_parameter='style_social_media_sharing.linkedin')
    email_icon = fields.Boolean(
        "E-mail", config_parameter='style_social_media_sharing.email')
    pinterest_icon = fields.Boolean(
        "Pinterest", config_parameter='style_social_media_sharing.pinterest')
    reddit_icon = fields.Boolean(
        "Reddit", config_parameter='style_social_media_sharing.reddit')
    hackernews_icon = fields.Boolean(
        "Hacker News", config_parameter='style_social_media_sharing.hackernews'
    )
