from django.shortcuts import render
# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import(LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from society.models import Society,SocietyMember
from . import models

class CreateSociety(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Society

class SingleSociety(generic.DetailView):
    model = Society

class ListSocieties(generic.ListView):
    model = Society


class JoinSociety(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("societies:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        society = get_object_or_404(Society,slug=self.kwargs.get("slug"))

        try:
            SocietyMember.objects.create(user=self.request.user,society=society)

        except IntegrityError:
            messages.warning(self.request,("Ya hace parte de {}".format(society.name)))

        else:
            messages.success(self.request,"Ahora eres miembro de {} .".format(society.name))

        return super().get(request, *args, **kwargs)


class LeaveSociety(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("societies:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.SocietyMember.objects.filter(
                user=self.request.user,
                society__slug=self.kwargs.get("slug")
            ).get()

        except models.SocietyMember.DoesNotExist:
            messages.warning(
                self.request,
                "No puede dejar la comunidad porque ya no pertenece a esta."
            )

        else:
            membership.delete()
            messages.success(
                self.request,
                "Has abandonado la comunidad."
            )
        return super().get(request, *args, **kwargs)