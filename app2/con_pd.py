from django.http import HttpResponse
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from io import BytesIO


class Convert:
    def __init__(self, name, file_path) -> None:
        self.name = name
        self.file_path = file_path

    def convert(self):
        # قراءة الملف الأصلي
        reader = PdfReader(self.file_path)
        writer = PdfWriter()

        # تحقق من عدد الصفحات في الملف
        num_pages = len(reader.pages)

        # إضافة العلامة المائية إلى الصفحة الأولى فقط
        for page_number, page in enumerate(reader.pages, 1):
            # إنشاء كانفاس للصفحة
            packet = BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            
            # تعيين لون وحجم النص
            can.setFont("Helvetica", 50)  # تعيين الخط وحجم النص
            can.setFillColor(Color(0, 0, 1, alpha=0.3))  # لون أزرق بشفافية
            
            # إضافة الاسم كخلفية للصفحة الأولى فقط
            if page_number == 1:
                can.drawString(150, 100, self.name)
            
            # حفظ الكانفاس
            can.save()

            # إعادة تعيين المؤشر لبداية البايتس
            packet.seek(0)

            # إنشاء صفحة PdfReader للخلفية
            background_page = PdfReader(packet).pages[0]
            
            # إضافة الصفحة الحالية من الملف الأصلي
            background_page.merge_page(page)

            # إضافة الصفحة إلى الملف الجديد
            writer.add_page(background_page)

            # انتهت الحلقة إذا كانت الصفحة الحالية هي الصفحة الأولى
            if page_number == 1:
                break

        # إعادة تعيين المؤشر لبداية الملف الجديد
        output_pdf = BytesIO()
        writer.write(output_pdf)
        output_pdf.seek(0)

        # إرجاع الملف كاستجابة
        #response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="example_with_background_watermark889.pdf"'
        #response.write(output_pdf.getvalue())
        #return response


        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{self.name}_watermarked.pdf"'

        # كتابة الملف الجديد إلى الاستجابة
        writer.write(response)

        return response