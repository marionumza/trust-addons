# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2016 Trustcode - www.trustcode.com.br                         #
#              Danimar Ribeiro <danimaribeiro@gmail.com>                      #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
###############################################################################


from openerp import api, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.multi
    def handle_partner_assignation(self, action='create',
                                   partner_id=False, context=None):
        partner_ids = super(CrmLead, self).handle_partner_assignation(
            action=action, partner_id=partner_id, context=context)

        for lead in self:
            partner_id = partner_ids[lead.id]
            partner = self.env['res.partner'].browse(partner_id)
            if partner.parent_id:
                partner_ids[lead.id] = partner.parent_id.id
                lead.partner_id = partner.parent_id.id

        return partner_ids
