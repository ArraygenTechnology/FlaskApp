import pdfkit
options = {
   'page-size': 'Letter',
   'margin-top': '0.9in',
   'margin-right': '0.9in',
   'margin-bottom': '0.9in',
   'margin-left': '0.9in',
   'encoding': "UTF-8",
   'header-html': '<img src="app/static/dist/img/Logo1.jpg" />',
   'footer-right': '[page] of [topage]',
   'no-outline': None
   }

pdfkit.from_url("https://stackoverflow.com/questions/50779742/pdfkit-formatting-header-footers", "test.pdf", options=options)