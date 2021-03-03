from pdf_annotate import PdfAnnotator, Location, Appearance
from random import randint
from config import * # pylint: disable=unused-wildcard-import
def annotatePDF(pathToPDF):
    try:
        randomNumber1 = str(randint(0,9))
        randomNumber2 = str(randint(1000,9999))

        a = PdfAnnotator(pathToPDF)
        #Name and adress
        a.add_annotation(
            'text',
            Location(x1=350, y1=590, x2=560, y2=650, page=0),
            Appearance(content= name +"\n" + adress +"\n" + city.upper(), font_size=11, fill=(0,0,0), line_spacing=1.8),
        )
        #Edition date
        a.add_annotation(
            'text',
            Location(x1=393, y1=550, x2=570, y2=573, page=0),
            Appearance(content= beautifulDate, font_size=9, fill=(0,0,0), line_spacing=1.65),
        )
        #Request number
        a.add_annotation(
            'text',
            Location(x1=1.37*72, y1=8.23*72, x2=3.58*72, y2=8.40*72, page=0),
            Appearance(content= date+'-'+randomNumber1+'-'+randomNumber2, font_size=9, fill=(0,0,0), line_spacing=1.65),
        )
        #name and date of birth
        a.add_annotation(
            'text',
            Location(x1=0.73*72, y1=8*72, x2=2.1*72, y2=8.3*72, page=0),
            Appearance(content= lastName.upper() + ' le : ' + birthDate, font_size=9, fill=(0,0,0), line_spacing=1.5),
        )
        #PrelevementDateTime
        a.add_annotation(
            'text',
            Location(x1=1.32*72, y1=7.43*72, x2=3*72, y2=7.7*72, page=0),
            Appearance(content= date + ' . ' + hour, font_size=9, fill=(0,0,0), line_spacing=1.1),
        )
        #ValidationDate1
        a.add_annotation(
            'text',
            Location(x1=5.34*72, y1=1.75*72, x2=5.85*72, y2=1.93*72, page=0),
            Appearance(content= date, font_size=9, fill=(0,0,0), line_spacing=1.1),
        )
        #ValidationDate2
        a.add_annotation(
            'text',
            Location(x1=3.6*72, y1=0.45*72, x2=4.1*72, y2=0.60*72, page=0),
            Appearance(content= date, font_size=9, fill=(0,0,0), line_spacing=1.1),
        )

        #Create a new file
        a.write(pathToPDF.replace('inputs','outputs'))
        return 'Done'
    except Exception as e:
        return e
