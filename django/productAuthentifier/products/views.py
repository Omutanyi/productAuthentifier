from django.shortcuts import render 
from django.http import HttpResponse 
from .models import Products, addProductForm
import qrcode
import psycopg2

# Create your views here.

def landing(request):

    prods = Products.objects.all()
    # input_data = "Product Authentifier"
    # qr = qrcode.QRCode(
    #     version=1,
    #     box_size=10,
    #     border=5)
    # qr.add_data(input_data)
    # qr.make(fit=True)
    # img = qr.make_image(fill='black', back_color='white')
    # img.save('qrcode001.png')

    if "add_product" in request.POST:
        add_product_form = addProductForm(data=request.POST)
        sql = """INSERT INTO products_products()
             VALUES(add_product_form)"""
        conn = None
        product_id = None
        try:
            conn = psycopg2.connect("dbname = ProductAuth user = postgres")
            cur = conn.cursor()
            cur.execute(sql, ())
            product_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error: print(error)
        finally:
             if conn is not None:
                conn.close()
                add_product_message = 'The product has been added successfully!!'
        return render(request, "landing.html", {'prods':prods}, {'messages': add_product_message})

    return render(request, "landing.html", {'prods':prods})