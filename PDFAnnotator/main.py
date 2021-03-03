from annotatePDF import annotatePDF
import os
from config import pdfName

print(os.path.dirname(os.path.realpath(__file__)))

def main():
    print(annotatePDF(os.path.dirname(os.path.realpath(__file__)) + '/inputs/' + pdfName))

main()