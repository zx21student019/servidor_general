#!C:\Users\zx21student023\AppData\Local\Microsoft\WindowsApps\python

import datetime
from datetime import date, timedelta
import cgi




x = datetime.datetime.now()
y = datetime.datetime(2003,11,28)

print("Content-Type: text/plain\n")

print(type(x))
print(x)
print(x.year)
print(x.strftime("%A"))
print(y)

print("Current date and time:" , x)
print("Current year:", x.year)
print("Month of year:", x.month, x.strftime("%B"))
print("Week number of the year: ", x.strftime("%W"))
print("Weekday of the week:", x.strftime("%w"))
print("Day of year: ", x.today().strftime("%j"))
print("Day of the month : ", x.today().strftime("%d"))
print("Day of week: ", x.today().strftime("%A"))

print("===================================================")

"""
Directive	Description	Example	Try it
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
"""

datosForm = cgi.FieldStorage()

fecha = datosForm["fecha"].value if "fecha" in datosForm else datetime.datetime.now()

if "fecha" in datosForm:
    fechaSplit = fecha.split("-")

    fecha = datetime.datetime(int(fechaSplit[0]),int(fechaSplit[1]),int(fechaSplit[2]))

print(fecha)

bis = datetime.datetime(fecha.year,12,31)

print(bis.strftime("%j"))
if bis.strftime("%j") == "366" :
    print("Es bisiesto")
else :
    print("No es bisiesto")

dt = date(int(fechaSplit[0]),int(fechaSplit[1]),int(fechaSplit[2])) - timedelta(5)
print(dt)

print("Hoy:",date.today())
print("Ayer:",date.today()- timedelta(1))
print("Mañana:",date.today()+ timedelta(1))

for n in range(0,6):
    print(date.today()+ timedelta(n))

