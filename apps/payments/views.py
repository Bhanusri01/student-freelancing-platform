from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wallet, Transaction


@login_required
def wallet_view(request):
    wallet, created = Wallet.objects.get_or_create(user=request.user)

    transactions = Transaction.objects.filter(user=request.user)

    return render(request, 'payments/wallet.html', {
        'wallet': wallet,
        'transactions': transactions
    })