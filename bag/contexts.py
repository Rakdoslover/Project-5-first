from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from workouts.models import Workout_Session


def bag_contents(request):

    bag_items = []
    total = 0
    session_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            session = get_object_or_404(Workout_Session, pk=item_id)
            total += item_data * session.price
            session_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'session': session,
            })
        else:
            session = get_object_or_404(Workout_Session, pk=item_id)

   

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'session_count': session_count,
        'grand_total': grand_total,
    }

    return context