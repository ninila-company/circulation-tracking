from django.shortcuts import render
from .models import Order
from datetime import datetime


def order_list(request):
    """
    Renders a list of orders and their details for the user to view.

    Args:
        request (HttpRequest): The request object sent by the user.

    Returns:
        HttpResponse: The response object containing the rendered HTML page.
    """
    context = {
        "orders": Order.objects.all(),
        "now": datetime.now().date(),  # Получаем текущую дату без времени
        "count": Order.objects.filter(completeness=False).count(),
    }
    return render(request, "track/order/list.html", context)
