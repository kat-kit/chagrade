from django.urls import reverse_lazy
from django.urls import resolve


class WizardMixin(object):

    _ordered_steps = [
        'klass_enrollment',
        'klass_homework',
        'klass_grading',
        'klass_activate',
    ]
    _current_step = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # If we don't have a current_step set try to set one automatically
        if not self._current_step:
            self._current_step = resolve(self.request.path_info).url_name
        context['wizard_current'] = self._current_step
        for index, step in enumerate(self._ordered_steps):
            if step == self._current_step:
                if index > 0:
                    # Set our previous step to our index-1 value of list
                    context['wizard_previous'] = reverse_lazy('klasses:{}'.format(self._ordered_steps[index-1]), kwargs={'klass_pk': kwargs.get('klass_pk')})
                if index < (len(self._ordered_steps) - 1):
                    # Set our next step to our index+1 value of list
                    context['wizard_next'] = reverse_lazy('klasses:{}'.format(self._ordered_steps[index+1]), kwargs={'klass_pk': kwargs.get('klass_pk')})
        return context