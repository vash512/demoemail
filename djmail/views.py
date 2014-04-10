from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

from django.http import HttpResponseRedirect,HttpResponse


def mail_view(request):
	htmly     = get_template('sidebar-hero.html')
	d = Context({})
	html_content = htmly.render(d)
	#mensaje=html_content
	asunto='Hola'
	para=['nextcase_jesus001@hotmail.com']
	#para=['chipgirl_g87@hotmail.com', 'fa.hikariangel@gmail.com',
	#'fhy_hdez@yahoo.com.mx', 'xtornasol512@gmail.com', 'jesua_cb@yahoo.com.mx','malu__ag@hotmail.com',
	#'malu.ag@gmail.com', 'phyrox.vash512@gmail.com', 'nextcase_jesus001@hotmail.com']
	for name in para:
		d = Context({'nombre':name})
		mensaje= htmly.render(d)
		email = EmailMessage(asunto+' '+name, mensaje, to=[name])
		email.content_subtype = "html"
		email.send()

	return HttpResponseRedirect('http://ffcmexico.com/?enviado=True')