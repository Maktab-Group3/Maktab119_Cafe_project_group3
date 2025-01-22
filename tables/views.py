from django.shortcuts import render, HttpResponse
from .models import Table


def table_list(request):
    tables = Table.objects.all()
    return render(request, 'table.html', {'tables': tables})

def generate_receipt(request, table_id):
    table = Table.objects.get(id=table_id)
    orders = table.orders.all()

    # the content of the receipts
    receipt_content = f"رسید میز {table.table_number}:\n"
    for order in orders:
        receipt_content += f"{order.item_name} - {order.quantity} عدد - {order.total_price} تومان\n"
    

    response = HttpResponse(receipt_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="receipt_table_{table.table_number}.txt"'
    return response