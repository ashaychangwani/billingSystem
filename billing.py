#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:19:42 2019

@author: ashay
"""
#dimensions are 595 × 842 points
width=595
height=842

from fpdf import FPDF
import os

pdf.output("Demo.pdf")
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
pdf.output("Demo.pdf")