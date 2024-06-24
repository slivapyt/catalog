from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from blog.models import Material
from pytils.translit import slugify




class MaterialCreateView(CreateView):
    model = Material
    fields = ('title','body',)
    success_url = reverse_lazy('blog:list')
    
    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)
    


class MaterialListView(ListView):
    model = Material
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published = True)
        return queryset


class MaterialDetailView(DetailView):
    model = Material

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)




    def get_object(self, queryset = None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body')
    #success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('blog:list')
