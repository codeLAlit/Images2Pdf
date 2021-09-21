import argparse
import os
from fpdf import FPDF

pages = {'A0':(841, 1188), 'A1':(594, 841), 'A2':(420, 594), 'A3':(297, 420) , 'A4':(210, 297)}

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', '-f', type=str, required=True, help='Folder in which the images are present')
    parser.add_argument('--name', '-n', type=str, required=True, help='Name of output file, it will created in your cwd')
    parser.add_argument('--margin', '-m', type=int, required=False, default=10, help='page margin (in mm) to leave at top, bottom, left and right')
    parser.add_argument('--orient', '-o', type=str, required=False, default='L', choices=['L', 'P'], help='Landscape or potrait')
    parser.add_argument('--paper', '-p', type=str, required=False, default='A4', help='Type of paper like A4 or A3')

    args = parser.parse_args()
    margin = args.margin
    ptype = args.paper
    orient = args.orient
    
    image_list = os.listdir(args.folder)
    image_list = [i for i in image_list if (i.split('.')[-1]=='png' or i.split('.')[-1]=='jpg')]
    image_list.sort()

    pdf_file = FPDF(orient, 'mm', ptype)
    
    if orient == 'L':
        height, width = pages[ptype]
    else:
        width, height = pages[ptype]

    height -= 2*margin
    width -= 2*margin
    x = margin
    y = margin

    for image in image_list:
        pdf_file.add_page()
        pdf_file.image(os.path.join(args.folder, image), x, y, width, height)
    
    pdf_file.output(args.name, "F")

    
