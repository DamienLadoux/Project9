
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review
from django.shortcuts import get_object_or_404


@login_required
def feed(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    context = {
        "tickets": tickets,
        "reviews": reviews,
    }
    return render(request, "reviews/feed.html", context)

@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            return redirect("feed")

    else:
        form = TicketForm()

    return render(
        request,
        "reviews/create_ticket.html",
        {"form": form},
    )

@login_required
def create_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()

            return redirect("feed")

    else:
        form = ReviewForm()

    return render(
        request,
        "reviews/create_review.html",
        {
            "form": form,
            "ticket": ticket,
        },
    )