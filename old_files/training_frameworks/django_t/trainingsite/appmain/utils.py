menu = ['Main page', 'Articles', 'About']

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        u_menu = menu.copy()
        if not self.request.user.is_authenticated:
            u_menu.pop(1)

        context['menu'] = u_menu
        context['link'] = 'orm/'
        return context