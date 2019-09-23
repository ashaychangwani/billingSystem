#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:19:42 2019

@author: ashay
"""
#dimensions are 595 × 842 points
width=538.5
height=842

from fpdf import FPDF
import os

class Invoice(FPDF):
    def header(self):
        self.add_font('Shusha', '', r"/Users/ashay/Downloads/Shusha.ttf", uni=True)
        self.set_font("Shusha",size=12)
        self.cell(0,0,txt="!",ln=1,align="C")
        self.set_font("Helvetica",size=8)
        self.cell(0,20,txt="SUBJECT TO MUMBAI JURISDICTION",ln=1,align="C")
        self.image("SV.jpg",x=(width-400)/2,y=50,w=400)
        self.image("LOGO.jpg",x=40,y=50,w=40)
        self.set_font("Helvetica",size=9)
        self.ln(45)
        self.cell(0,0,txt="Regd. Off.: Elavia Apartment, 1st Floor, 33rd Road, Off Linking Road, Bandra (W), Mumbai 400050.",ln=1,align="C")
        self.cell(0,22,txt="Email: huezjeans@gmail.com / Mob: 9820135125",ln=1,align="C")
        self.ln(10)
        self.set_font("helvetica",size=9,style='B')
        self.cell(0,0,txt="GSTIN: 27ADHPC2299M1Z6",ln=1,align="C")
        self.set_font("helvetica",size=12,style='B')
        self.cell(0,30,txt="GST INVOICE",ln=1,align="C")

pdf=Invoice(orientation='P',unit='pt',format='A4')
pdf.add_page()
pdf.set_font("helvetica",size=8)
pdf.cell(width/2,14,txt="Consignee / Billed to",ln=0,border=1,align="C")
pdf.cell(width/8,14,txt="Invoice No.",ln=0,border=1,align="C")
pdf.cell(0,14,txt="701",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="M/s.",ln=0,align="C",border="LR")
pdf.cell((7*width/16),14,txt="DARVESH SYNTHETICS PVT. LTD",ln=0,align="L",border="LR")
pdf.cell(width/8,14,txt="Date",ln=0,border=1,align="C")
pdf.cell(0,14,txt="13/09/2019",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="",ln=0,align="C",border="LR") 
pdf.cell((7*width/16),14,txt="64/A, Jasraj Bhawan, Gr, Floor,",ln=0,align="L",border="LR")
pdf.cell(width/8,14,txt="Due Date",ln=0,border=1,align="C")
pdf.cell(0,14,txt="13/10/2019",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="",ln=0,align="C",border="LR")
pdf.cell((7*width/16),14,txt="Old Hanuman Lane",ln=0,align="L",border="LR")
pdf.cell(width/8,14,txt="Order No.",ln=0,border=1,align="C")
pdf.cell(0,14,txt="701",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="City",ln=0,align="C",border="LR")
pdf.cell((7*width/16),14,txt="Mumbai 400002",ln=0,align="L",border="LBR")
pdf.cell(width/8,14,txt="Transport",ln=0,border=1,align="C")
pdf.cell(0,14,txt="The Nagpur Goods",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="State",ln=0,align="C",border="LR")
pdf.cell((5*width/16),14,txt="Maharashtra",ln=0,align="L",border="LBR")
pdf.cell((width/16),14,txt="Code",ln=0,align="L",border="LBR")
pdf.cell((width/16),14,txt="27",ln=0,align="L",border="LBR")
pdf.cell(width/8,14,txt="L.R. No.",ln=0,border=1,align="C")
pdf.cell(width/8,14,txt="123456",ln=0,border=1,align="L")
pdf.cell(width/8,14,txt="L.R. Date",ln=0,border=1,align="L")
pdf.cell(width/8,14,txt="14/09/2019",ln=1,border=1,align="L")


pdf.cell((width/16),14,txt="GST No.",ln=0,align="C",border="LR")
pdf.cell((7*width/16),14,txt="27AABCD0014B1ZM",ln=0,align="L",border="LBR")
pdf.cell(width/8,14,txt="Broker / Haste",ln=0,border=1,align="C")
pdf.cell(0,14,txt="Vijay Singh",ln=1,border=1,align="L")




pdf.cell(width/2,14,txt="Delivered / Shipped To",ln=0,border=1,align="C")
pdf.cell(width/8,14,txt="State",ln=0,border=1,align="C")
pdf.cell(0,14,txt="Maharashtra",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="M/s.",ln=0,align="C",border="LR")
pdf.cell((7*width/16),14,txt="DARVESH SYNTHETICS PVT. LTD",ln=0,align="L",border="LR")
pdf.cell(width/8,14,txt="Code",ln=0,border=1,align="C")
pdf.cell(0,14,txt="27",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="",ln=0,align="C",border="LR") 
pdf.cell((7*width/16),14,txt="64/A, Jasraj Bhawan, Gr, Floor,",ln=0,align="L",border="LR")
pdf.cell(width/8,14,txt="Transport Mode",ln=0,border=1,align="C")
pdf.cell(0,14,txt="By Road",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="",ln=0,align="C",border="LR")
pdf.cell((7*width/16),14,txt="Old Hanuman Lane",ln=0,align="L",border="LR")
pdf.cell(width/8,14,txt="Date of Supply",ln=0,border=1,align="C")
pdf.cell(0,14,txt="14-09-2019",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="City",ln=0,align="C",border="LR")
pdf.cell((7*width/16),14,txt="Mumbai 400002",ln=0,align="L",border="LBR")
pdf.cell(width/8,14,txt="Reverse Charge",ln=0,border=1,align="C")
pdf.cell(0,14,txt="No",ln=1,border=1,align="L")

pdf.cell((width/16),14,txt="State",ln=0,align="C",border="LR")
pdf.cell((5*width/16),14,txt="Maharashtra",ln=0,align="L",border="LBR")
pdf.cell((width/16),14,txt="Code",ln=0,align="L",border="LBR")
pdf.cell((width/16),14,txt="27",ln=0,align="L",border="LBR")
pdf.cell(width/8,14,txt="",ln=0,border=1,align="C")
pdf.cell(0,14,txt="",ln=1,border=1,align="L")


pdf.cell((width/16),14,txt="GST No.",ln=0,align="C",border="LR")
pdf.cell((7*width/16),14,txt="27AABCD0014B1ZM",ln=0,align="L",border="LBR")
pdf.cell(width/8,14,txt="",ln=0,border=1,align="C")
pdf.cell(0,14,txt="",ln=1,border=1,align="L")

pdf.set_font("helvetica",size=8,style="B")
y=pdf.get_y()
x=pdf.get_x()
pdf.multi_cell((width/16),14,txt="\nSr. No",align="C",border="LTBR")
pdf.set_y(y)
pdf.set_x(x+width/16)
x=pdf.get_x()
pdf.multi_cell((5*width/16),14,txt="\nName of Product",align="C",border="LTBR")
pdf.set_y(y)
pdf.set_x(x+5*width/16)
x=pdf.get_x()
pdf.multi_cell((width/16),14,txt="HSN / \nAcs",align="C",border="LBR")
pdf.set_y(y)
pdf.set_x(x+width/16)
x=pdf.get_x()
pdf.multi_cell((width/16),14,txt="Design\nNo.",align="C",border="LBR")
pdf.set_y(y)
pdf.set_x(x+width/16)
x=pdf.get_x()
pdf.multi_cell((width/16),14,txt="\nQty",align="C",border="LBR")
pdf.set_y(y)
pdf.set_x(x+width/16)
x=pdf.get_x()
pdf.multi_cell((width/16),14,txt="\nRate",align="C",border="LBR")
pdf.set_y(y)
pdf.set_x(x+width/16)
x=pdf.get_x()
pdf.multi_cell((width/12),14,txt="Less Rs\nPer pc",align="C",border="LBR")
pdf.set_y(y)
pdf.set_x(x+width/12)
x=pdf.get_x()
pdf.multi_cell((width/12),14,txt="Discount %",align="C",border="LBR")
pdf.set_y(y)
pdf.set_x(x+width/12)
x=pdf.get_x()
pdf.multi_cell((width/12),14,txt="\nNett Rate",align="C",border="LBR")
pdf.set_y(y)
pdf.set_x(x+width/12)
x=pdf.get_x()
pdf.multi_cell(0,14,txt="\nTotal",align="C",border="LBR")
pdf.output("Demo.pdf")