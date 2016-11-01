from datetime import date
from django.forms import Form, fields

class ChargesForm(Form):
    date = fields.DateField(label = 'date')
    value = fields.DecimalField(label = 'value')

    def clean(self):
        cleaned_data = super(ChargesForm,self).clean()
        date_charge = cleaned_data.get('date')
        value_charge = cleaned_data.get('value')
        today =  date.today()
        if  value_charge < 0:
            if date_charge > today:
                self.add_error('date',"Impossible to make a write-off")
                self.add_error('value',"Impossible to make a write-off")

        return cleaned_data