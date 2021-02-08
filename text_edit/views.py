from django.views.generic.edit import FormView

from . import forms

# Create your views here.
class Index(FormView):
    form_class = forms.TextForm
    template_name = "index.html"
    
    # 入力に問題がなければ、この関数が自動的に呼ばれる
    def form_valid(self, form):
        data = form.cleaned_data
        text = data["text"]
        search = data["search"]
        replace = data["replace"]
        
        new_text = text.replace(search, replace)
        
        ctxt = self.get_context_data(new_text=new_text, form=form)
        return self.render_to_response(ctxt)