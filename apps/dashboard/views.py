from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Avg, Sum
from django.db.models.functions import TruncMonth
from django.utils import timezone

from apps.gigs.models import Gig
from apps.orders.models import Order
from apps.payments.models import Transaction, Wallet
from apps.reviews.models import Review
from apps.messaging.models import Conversation


# ðŸ” Dashboard Redirect Based on Role
@login_required
def dashboard_redirect(request):
    if request.user.user_type == 'student':
        return redirect('student_dashboard')
    elif request.user.user_type == 'client':
        return redirect('client_dashboard')
    else:
        return redirect('home')


# ðŸ‘¨â€ðŸ’» STUDENT (FREELANCER) DASHBOARD
@login_required
def student_dashboard(request):
    user = request.user

    gigs_count = Gig.objects.filter(seller=user).count()
    my_gigs = Gig.objects.filter(seller=user).order_by('-created_at')
    orders_count = Order.objects.filter(seller=user).count()

    wallet, _ = Wallet.objects.get_or_create(user=user)

    reviews = Review.objects.filter(seller=user)
    avg_rating = reviews.aggregate(avg=Avg('rating'))['avg'] or 0
    status_labels = ['Pending', 'In Progress', 'Delivered', 'Completed', 'Cancelled']
    order_status_counts = [
        Order.objects.filter(seller=user, status='pending').count(),
        Order.objects.filter(seller=user, status='in_progress').count(),
        Order.objects.filter(seller=user, status='delivered').count(),
        Order.objects.filter(seller=user, status='completed').count(),
        Order.objects.filter(seller=user, status='cancelled').count(),
    ]
    earnings_by_month_qs = (
        Transaction.objects
        .filter(user=user, transaction_type='release')
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )
    earnings_month_labels = [
        item['month'].strftime('%b %Y') for item in earnings_by_month_qs if item['month']
    ]
    earnings_month_values = [float(item['total']) for item in earnings_by_month_qs]

    return render(request, 'dashboard/student_dashboard.html', {
        'gigs_count': gigs_count,
        'my_gigs': my_gigs,
        'orders_count': orders_count,
        'wallet_balance': wallet.balance,
        'avg_rating': round(avg_rating, 1),
        'status_labels': status_labels,
        'order_status_counts': order_status_counts,
        'earnings_month_labels': earnings_month_labels,
        'earnings_month_values': earnings_month_values,
    })


# ðŸ§‘â€ðŸ’¼ CLIENT DASHBOARD
@login_required
def client_dashboard(request):
    user = request.user

    total_spent = Order.objects.filter(client=user).aggregate(
        total=Sum('price')
    )['total'] or 0

    messages_count = Conversation.objects.filter(client=user).count()
    status_labels = ['Pending', 'In Progress', 'Delivered', 'Completed', 'Cancelled']
    order_status_counts = [
        Order.objects.filter(client=user, status='pending').count(),
        Order.objects.filter(client=user, status='in_progress').count(),
        Order.objects.filter(client=user, status='delivered').count(),
        Order.objects.filter(client=user, status='completed').count(),
        Order.objects.filter(client=user, status='cancelled').count(),
    ]
    spending_by_month_qs = list(
        Order.objects
        .filter(client=user)
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total=Sum('price'))
        .order_by('month')
    )
    spending_month_labels = [
        item['month'].strftime('%b %Y') for item in spending_by_month_qs if item['month']
    ]
    spending_month_values = [float(item['total']) for item in spending_by_month_qs]
    if not spending_month_values and float(total_spent) > 0:
        spending_month_labels = [timezone.now().strftime('%b %Y')]
        spending_month_values = [float(total_spent)]

    return render(request, 'dashboard/client_dashboard.html', {
        'total_spent': total_spent,
        'messages_count': messages_count,
        'status_labels': status_labels,
        'order_status_counts': order_status_counts,
        'spending_month_labels': spending_month_labels,
        'spending_month_values': spending_month_values,
    })
