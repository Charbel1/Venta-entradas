# -*- coding: utf-8 -*-
import asyncio
from random import randint

import aiohttp
import psycopg2


from datetime import datetime
from sanic import Sanic
from sanic import response
from sanic_cors import CORS, cross_origin
from sanic.handlers import ErrorHandler
import smtplib
import email.message

def sendMail(data,random):
    email_content = """<!doctype html>
        <html>
          <head>
            <meta name="viewport" content="width=device-width" />
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <title>Simple Transactional Email</title>
            <style>
              /* -------------------------------------
                  GLOBAL RESETS
              ------------------------------------- */
              img {
                border: none;
                -ms-interpolation-mode: bicubic;
                max-width: 100%; }
              body {
                background-color: #f6f6f6;
                font-family: sans-serif;
                -webkit-font-smoothing: antialiased;
                font-size: 14px;
                line-height: 1.4;
                margin: 0;
                padding: 0;
                -ms-text-size-adjust: 100%;
                -webkit-text-size-adjust: 100%; }
              table {
                border-collapse: separate;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                width: 100%; }
                table td {
                  font-family: sans-serif;
                  font-size: 14px;
                  vertical-align: top; }
              /* -------------------------------------
                  BODY & CONTAINER
              ------------------------------------- */
              .body {
                background-color: #f6f6f6;
                width: 100%; }
              /* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
              .container {
                display: block;
                Margin: 0 auto !important;
                /* makes it centered */
                max-width: 580px;
                padding: 10px;
                width: 580px; }
              /* This should also be a block element, so that it will fill 100% of the .container */
              .content {
                box-sizing: border-box;
                display: block;
                Margin: 0 auto;
                max-width: 580px;
                padding: 10px; }
              /* -------------------------------------
                  HEADER, FOOTER, MAIN
              ------------------------------------- */
              .main {
                background: #ffffff;
                border-radius: 3px;
                width: 100%; }
              .wrapper {
                box-sizing: border-box;
                padding: 20px; }
              .content-block {
                padding-bottom: 10px;
                padding-top: 10px;
              }
              .footer {
                clear: both;
                Margin-top: 10px;
                text-align: center;
                width: 100%; }
                .footer td,
                .footer p,
                .footer span,
                .footer a {
                  color: #999999;
                  font-size: 12px;
                  text-align: center; }
              /* -------------------------------------
                  TYPOGRAPHY
              ------------------------------------- */
              h1,
              h2,
              h3,
              h4 {
                color: #000000;
                font-family: sans-serif;
                font-weight: 400;
                line-height: 1.4;
                margin: 0;
                Margin-bottom: 30px; }
              h1 {
                font-size: 35px;
                font-weight: 300;
                text-align: center;
                text-transform: capitalize; }
              p,
              ul,
              ol {
                font-family: sans-serif;
                font-size: 14px;
                font-weight: normal;
                margin: 0;
                Margin-bottom: 15px; }
                p li,
                ul li,
                ol li {
                  list-style-position: inside;
                  margin-left: 5px; }
              a {
                color: #3498db;
                text-decoration: underline; }
              /* -------------------------------------
                  BUTTONS
              ------------------------------------- */
              .btn {
                box-sizing: border-box;
                width: 100%; }
                .btn > tbody > tr > td {
                  padding-bottom: 15px; }
                .btn table {
                  width: auto; }
                .btn table td {
                  background-color: #ffffff;
                  border-radius: 5px;
                  text-align: center; }
                .btn a {
                  background-color: #ffffff;
                  border: solid 1px #3498db;
                  border-radius: 5px;
                  box-sizing: border-box;
                  color: #3498db;
                  cursor: pointer;
                  display: inline-block;
                  font-size: 14px;
                  font-weight: bold;
                  margin: 0;
                  padding: 12px 25px;
                  text-decoration: none;
                  text-transform: capitalize; }
              .btn-primary table td {
                background-color: #3498db; }
              .btn-primary a {
                background-color: #5b3989;
                border-color: #5b3989;
                color: #ffffff; }
              /* -------------------------------------
                  OTHER STYLES THAT MIGHT BE USEFUL
              ------------------------------------- */
              .last {
                margin-bottom: 0; }
              .first {
                margin-top: 0; }
              .align-center {
                text-align: center; }
              .align-right {
                text-align: right; }
              .align-left {
                text-align: left; }
              .clear {
                clear: both; }
              .mt0 {
                margin-top: 0; }
              .mb0 {
                margin-bottom: 0; }
              .preheader {
                color: transparent;
                display: none;
                height: 0;
                max-height: 0;
                max-width: 0;
                opacity: 0;
                overflow: hidden;
                mso-hide: all;
                visibility: hidden;
                width: 0; }
              .powered-by a {
                text-decoration: none; }
              hr {
                border: 0;
                border-bottom: 1px solid #f6f6f6;
                Margin: 20px 0; }
              /* -------------------------------------
                  RESPONSIVE AND MOBILE FRIENDLY STYLES
              ------------------------------------- */
              @media only screen and (max-width: 620px) {
                table[class=body] h1 {
                  font-size: 28px !important;
                  margin-bottom: 10px !important; }
                table[class=body] p,
                table[class=body] ul,
                table[class=body] ol,
                table[class=body] td,
                table[class=body] span,
                table[class=body] a {
                  font-size: 16px !important; }
                table[class=body] .wrapper,
                table[class=body] .article {
                  padding: 10px !important; }
                table[class=body] .content {
                  padding: 0 !important; }
                table[class=body] .container {
                  padding: 0 !important;
                  width: 100% !important; }
                table[class=body] .main {
                  border-left-width: 0 !important;
                  border-radius: 0 !important;
                  border-right-width: 0 !important; }
                table[class=body] .btn table {
                  width: 100% !important; }
                table[class=body] .btn a {
                  width: 100% !important; }
                table[class=body] .img-responsive {
                  height: auto !important;
                  max-width: 100% !important;
                  width: auto !important; }}
              /* -------------------------------------
                  PRESERVE THESE STYLES IN THE HEAD
              ------------------------------------- */
              @media all {
                .ExternalClass {
                  width: 100%; }
                .ExternalClass,
                .ExternalClass p,
                .ExternalClass span,
                .ExternalClass font,
                .ExternalClass td,
                .ExternalClass div {
                  line-height: 100%; }
                .apple-link a {
                  color: inherit !important;
                  font-family: inherit !important;
                  font-size: inherit !important;
                  font-weight: inherit !important;
                  line-height: inherit !important;
                  text-decoration: none !important; }
                .btn-primary table td:hover {
                  background-color: #6E42AA !important; }
                .btn-primary a:hover {
                  background-color: #6E42AA !important;
                  border-color: #6E42AA !important; } }
            </style>
          </head>
          <body class="">
            <table border="0" cellpadding="0" cellspacing="0" class="body">
              <tr>
                <td>&nbsp;</td>
                <td class="container">
                  <div class="content">
                    <!-- START CENTERED WHITE CONTAINER -->
                    <span class="preheader">Entrada Wango</span>
                    <table class="main">
                      <!-- START MAIN CONTENT AREA -->
                      <tr>
                        <td class="wrapper">
                          <table border="0" cellpadding="0" cellspacing="0">
                            <tr>
                              <td>
                                <img src="https://goo.gl/images/S7Mgch" style="height:100px" alt="">
                             <p>Saludos  <b>"""+data["nombre"]+"""  """+data["apellido"]+"""</b>. </p>
                            <p>Anexamos en este correo el código correspondiente a la compra de tu entrada</p>
                            <p>este codigo es <b>Intransferible</b> solo lo podras usar  <b>TU</b>.</p>
                            <table border="0" cellpadding="0" cellspacing="0" class="btn btn-primary">
                              <tbody>
                                <tr>
                                  <td align="center">

                                    <div class="h3">
                                        <b>"""+str(random)+"""</b>
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <p>Puedes retirar tu entrada personalmente en nuestra oficina ubicada en
                            Av Andrés Bello entre Francisco de Miranda y transversal 1 Edificio plaza 1
                            Planta Baja  salón Arena Los Palos Grandes
                             Contacto al momento de retirar la entrada 0212-7143333
                            Horario de entregas 9:00 AM a 4:00 PM de lunes a viernes  </p>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    <!-- END MAIN CONTENT AREA -->
                    </table>
                    <!-- START FOOTER -->
                    <div class="footer">
                      <table border="0" cellpadding="0" cellspacing="0">
                        <tr>
                          <td class="content-block">
                            <span class="apple-link">Wango</span>
                          </td>
                        </tr>
                        <tr>
                          <td class="content-block powered-by">
                            Powered by <a href="">Charbel Nachar </a>.
                          </td>
                        </tr>
                      </table>
                    </div>
                    <!-- END FOOTER -->
                  <!-- END CENTERED WHITE CONTAINER -->
                  </div>
                </td>
                <td>&nbsp;</td>
              </tr>
            </table>
          </body>
        </html>
    """

    msg = email.message.Message()
    msg['Subject'] = 'Entrada Digital Wango'

    msg['From'] = 'xparty.ventas@gmail.com'
    msg['To'] = data['correo']
    password = "12505990"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)

    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('UTF-8 '))


    print("se envio el correo a " + msg['To'])


class CustomHandler(ErrorHandler):
    def default(self, request, exception):
        print(exception)
        return response.json('NO',501)



def get_db():
    db = ""
    return db




def con():

    # Open database connection
    #conn = psycopg2.connect(database='chino', user='postgres', password='G4l1l30', host='sql.lorebi.com')
    conn = psycopg2.connect(database='pruebawango', user='postgres', password='123', host='localhost')
    # prepare a cursor object using cursor() method

    return conn




app = Sanic(__name__)
PORT = 5034

handler = CustomHandler()
app.error_handler = handler



@app.route('/wango/registro',methods=['POST','OPTIONS'])
@cross_origin(app, automatic_options=True)
async def get_by_id(request):
    data = request.json
    random = randint(24211, 23631507)
    conn = con()
    cursor = conn.cursor()
    try:

        int(data['cedula'])
        fecha =str(datetime.now())
        cursor.execute("INSERT INTO cliente(nombre, apellido, cedula, codigo, correo, fecha, entregado, embajador,instagram )"
                       "VALUES ('"+data['nombre']+"', '"+data['apellido']+"', '"+data['cedula']+"',"+str(random)+" ,'"+data['correo']+"', TO_DATE('"+fecha+"', 'DD/MM/YYYY'),false,'"+data['embajador']+"','"+data['instagram']+"');")

        conn.commit()

    except ValueError:
        return response.json({"data": "", "error": "Error en Cédula"})
            print("Error Cedula")
    except (Exception, psycopg2.IntegrityError) as error:
        print(error)
        conn.rollback()

        if  str(error).find("cedula") > 0 :
            return response.json({"data": "", "error": "Cédula ya Registrada"})
        else:
            return response.json({"data": "", "error": "Error Volver a intentar"})



    finally:
        if conn is not None:
            conn.close()
        if cursor is not None:
            cursor.close()


    try:
        sendMail(data,random)
    except Exception as e:
        print(e)
        return response.json({"data":"","error":"No se envío "})

    return response.json({"data":random, "error": "0"})


@app.route('/wango/buscarC',methods=['POST','OPTIONS'])
@cross_origin(app, automatic_options=True)
async def get_by_id(request):
    aux = {}
    data = request.json

    conn = con()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT nombre, apellido, cedula, codigo, correo, fecha ,entregado , codigoe ,embajador , instagram"
                       "  FROM cliente where cedula = "+data['cedula'])
        data = cursor.fetchone()
        aux['nombre'] =data[0]
        aux['apellido'] = data[1]
        aux['cedula'] = data[2]
        aux['codigo'] = data[3]
        aux['correo'] = data[4]
        aux['embajador'] = data[8]
        aux['fecha'] = datetime.strftime(data[5], '%d/%m')
        aux['instagram'] = data[9]
        if (data[6] == True):
            aux['entregado'] ='Si'

        else:
            aux['entregado'] = 'No'

        aux['codigoe'] = data[7]

    except (Exception, psycopg2.Error) as error:
        print(error)



    finally:
        if conn is not None:
            conn.close()
        if cursor is not None:
            cursor.close()


    if data is not None:
        return response.json({"data": aux, "error": "0"})
    else:
        return response.json({"data":"", "error": "No regitrado"})


@app.route('/wango/aprobar',methods=['POST','OPTIONS'])
@cross_origin(app, automatic_options=True)
async def get_by_id(request):
    aux = {}
    data = request.json

    conn = con()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT nombre, apellido, cedula, codigo, correo, fecha ,entregado, codigoE"
                       "  FROM cliente where cedula = "+str(data['cedula']))
        info = cursor.fetchone()

        if info[6] == False  :
            cambio = True

            cursor.execute("SELECT nombre, apellido, cedula, codigo, correo, fecha ,entregado, codigoE"
                           "  FROM cliente where codigoE = '"+data['entrada']+"'")

            auxentrada = cursor.fetchone()
            if auxentrada is None:
                sql = "UPDATE cliente  SET entregado = True, codigoe ='"+str(data['entrada'])+"' WHERE cedula = "+str(data['cedula'])
            else:
                return response.json({"data": '',"error": "Entrada Repetida"})
            # execute the UPDATE  statement

            cursor.execute(sql)
            # get the number of updated rows

            # Commit the changes to the database
            conn.commit()
        else:
            cambio=False




    except (Exception, psycopg2.Error) as error:
        print(error)
        return response.json({"data": '',"error": "Error"})


    finally:
        if conn is not None:
            conn.close()
        if cursor is not None:
            cursor.close()


    if cambio:
        return response.json({"data": 'si',"error": "0"})
    elif not cambio:
        return response.json({"data":"", "error": "Entrada Entregada"})
    elif info is None:
        return response.json({"data":"", "error": "No regitrado"})


@app.route('/wango/renviarC',methods=['POST','OPTIONS'])
@cross_origin(app, automatic_options=True)
async def get_by_id(request):
    aux = {}
    data = request.json

    conn = con()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT nombre, apellido, cedula, codigo, correo, fecha ,codigoe"
                       "  FROM cliente where cedula = "+data['cedula'])
        data = cursor.fetchone()
        aux['nombre'] =data[0]
        aux['apellido'] = data[1]
        aux['cedula'] = data[2]
        aux['codigo'] = data[3]
        aux['correo'] = data[4]
        aux['fecha'] = data[5]
        aux['codigoe'] = data[6]

    except (Exception, psycopg2.Error) as error:
        print(error)



    finally:
        if conn is not None:
            conn.close()
        if cursor is not None:
            cursor.close()


    if data is not None:

        try:

            sendMail(aux,aux['codigo'])
            return response.json({"data":"","error":"0"})
        except Exception as e:
           print(e)
           return response.json({"data":"","error":"No se envío "})
    else:
        return response.json({"data":"", "error": "No registrado"})


@app.route('/wango/reporte',methods=['POST','OPTIONS'])
@cross_origin(app, automatic_options=True)
async def get_by_id(request):
    aux = {}
    cont = no = 0
    data = request.json
    list = []
    conn = con()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT nombre, apellido, cedula, codigo, correo, fecha,entregado"
                       "  FROM cliente ")
        data = cursor.fetchall()
        for row in data:
            aux['nombre'] =row[0]
            aux['apellido'] = row[1]
            aux['cedula'] = row[2]
            aux['codigo'] = row[3]
            aux['correo'] = row[4]
            aux['fecha'] = row[5]
            list.append(aux)
            if row[6] == True:
                cont= cont +1
            else:
                no= no +1

    except (Exception, psycopg2.Error) as error:
        print(error)



    finally:
        if conn is not None:
            conn.close()
        if cursor is not None:
            cursor.close()


    if list is not None:
        return response.json({"data":{"entregada":cont,"no":no}, "error": "0"})
    else:
        return response.json({"data":{"entregada":cont,"no":no}, "error": "0"})

@app.route('/wango/reportecsv',methods=['POST','OPTIONS'])
@cross_origin(app, automatic_options=True)
async def get_by_id(request):
    aux = {}
    cont = no = 0
    data = request.json
    list = []
    conn = con()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT nombre, apellido, cedula, codigo, correo,instagram, fecha,entregado,codigoE,embajador,entro"
                       "  FROM cliente order by entregado ")
        data = cursor.fetchall()

        for row in data:


            aux['nombre'] =row[0]
            aux['apellido'] = row[1]
            aux['cedula'] = row[2]
            aux['correo'] = row[4]
            aux['instagram'] = row[5]
            aux['fecha'] = datetime.strftime(row[6], '%d/%m')
            aux['codigo'] = row[3]
            aux['embajador'] = row[9]
            aux['codigoE'] = row[8]
            if row[7] == True:
                aux['entregado'] = 'si'
            else:
                aux['entregado'] = 'no'
            if row[10] == True:
                aux['entro'] = 'si'
            else:
                aux['entro'] = 'no'




            list.append(aux)
            aux= {}



    except (Exception, psycopg2.Error) as error:
        print(error)



    finally:
        if conn is not None:
            conn.close()
        if cursor is not None:
            cursor.close()


    if list is not None:

        return response.json({"data":list, "error": "0"})
    else:
        return response.json({"data":"", "error": "No se envío"})




app.config.REQUEST_MAX_SIZE = 1024 * 1024 * 50

app.run(host='0.0.0.0', port = PORT, debug = False)
