from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
# Create your views here.


def generate_pdf_view(request, report_id):

    # report = ReportResult.objects.filter(pk=report_id).first()
    # template = Template.objects.all().first()

    list_report = ['defining_niche',
                   'voluem_market',
                   'list_key_players',
                   'key_consumers',
                   'development_trends']

    html_template = render_to_string('pdf/test.html',)

    html = HTML(string=html_template)
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    return response


