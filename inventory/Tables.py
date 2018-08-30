from inventory.models import Equipment
from table import Table
from table.columns import Column
from django_datatables_view.base_datatable_view import BaseDatatableView

class EquipmentListJson(BaseDatatableView):
    model = Equipment
    columns = ['Inventory Tag','Due Date']
    order_columns = ['Inventory Tag','Due Date']
    max_display_length = 500
