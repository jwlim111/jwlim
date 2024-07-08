#!/usr/bin/python

from concurrent.futures.process import _SafeQueue
import tkinter as tk
from tkinter import ttk
from xml.etree.ElementTree import tostring
import pyvisa as visa
from tkinter import scrolledtext
from time import sleep
from ttkthemes import ThemedTk
from datetime import datetime

rm = visa.ResourceManager()
inst = rm.open_resource('TCPIP0::192.168.100.254::inst0::INSTR',  
    write_termination = '\n', read_termination='\n')
inst1 = rm.open_resource('TCPIP0::192.168.100.254::inst1::INSTR',  
    write_termination = '\n', read_termination='\n')
inst2 = rm.open_resource('TCPIP0::192.168.100.254::inst2::INSTR',  
    write_termination = '\n', read_termination='\n')
inst3 = rm.open_resource('TCPIP0::192.168.100.254::inst3::INSTR',  
    write_termination = '\n', read_termination='\n')


win = ThemedTk(theme='blue')

win.title('WTS Tester') 

#LabelFrame
entry = tk.LabelFrame(win,text='WTS')
entry.grid(column=0, row=0)

#Connection

connection = tk.LabelFrame(entry, text='Connection')
connection.grid(column=0,row=0, pady= 20)

log = ttk.LabelFrame(win, text='Log')
log.grid(column=1, row=0)

log_box = scrolledtext.ScrolledText(log)

log_box.grid(column=0,row=0)


def ch1_capture_tx_1():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst.write(":CONFigure:RFSA:GPRF:FREQuency 2405000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2405000000\n")
    inst.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst.write("TRIGger:RFSA:GPRF:SOUR IF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR IF\n")
    inst.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    sleep(0.02)
    fetch = inst.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst1.write("SOURce:RFSG:GPRF:STATe OFF")

def ch1_gen_1():
    #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00\n")
    inst1.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:IDLEtime 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime 1\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
    inst1.write("SOURce:RFSG:GPRF:STATe ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
    
    opc = inst1.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
    #log_box.see(tk.END)
    fetch = inst1.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')

def ch2_capture_tx_1():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst.write(":CONFigure:RFSA:GPRF:FREQuency 2410000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2410000000\n")
    inst.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst.write("TRIGger:RFSA:GPRF:SOUR IF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR IF\n")
    inst.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    sleep(0.02)
    fetch = inst.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst1.write("SOURce:RFSG:GPRF:STATe OFF")

def ch2_gen_1():
    #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2410, 2.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2410, 2.00\n")
    inst1.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2410E6")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2410E6\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:IDLEtime 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime 1\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
    inst1.write("SOURce:RFSG:GPRF:STATe ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
    
    opc = inst1.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
    #log_box.see(tk.END)
    fetch = inst1.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')

def ch3_capture_tx_1():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst.write(":CONFigure:RFSA:GPRF:FREQuency 2415000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2415000000\n")
    inst.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst.write("TRIGger:RFSA:GPRF:SOUR IF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR IF\n")
    inst.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    sleep(0.02)
    fetch = inst.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst1.write("SOURce:RFSG:GPRF:STATe OFF")

def ch3_gen_1():
    #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2415, 2.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2415, 2.00\n")
    inst1.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2415E6")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2415E6\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:IDLEtime 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime 1\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
    inst1.write("SOURce:RFSG:GPRF:STATe ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
    
    opc = inst1.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
    #log_box.see(tk.END)
    fetch = inst1.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')

def ch4_capture_tx_1():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst.write(":CONFigure:RFSA:GPRF:FREQuency 2420000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2420000000\n")
    inst.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst.write("TRIGger:RFSA:GPRF:SOUR IF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR IF\n")
    inst.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    sleep(0.02)
    fetch = inst.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst1.write("SOURce:RFSG:GPRF:STATe OFF")

def ch4_gen_1():
    #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2420, 2.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2420, 2.00\n")
    inst1.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2420E6")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2420E6\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:IDLEtime 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime 1\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
    inst1.write("SOURce:RFSG:GPRF:STATe ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
    
    opc = inst1.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
    #log_box.see(tk.END)
    fetch = inst1.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')

def ch1_capture_tx_2():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst2.write(":CONFigure:RFSA:GPRF:FREQuency 2405000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2405000000\n")
    inst2.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst2.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst2.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst2.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst2.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst2.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst2.write("TRIGger:RFSA:GPRF:SOUR IF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR IF\n")
    inst2.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst2.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst2.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    sleep(0.02)
    fetch = inst2.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst3.write("SOURce:RFSG:GPRF:STATe OFF")

def ch1_gen_2():
    #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
    inst3.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00\n")
    inst3.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
    inst3.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:IDLEtime 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime 1\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
    inst3.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
    inst3.write("SOURce:RFSG:GPRF:STATe ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
    
    opc = inst3.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
    #log_box.see(tk.END)
    fetch = inst3.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')

def ch2_capture_tx_2():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst2.write(":CONFigure:RFSA:GPRF:FREQuency 2410000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2410000000\n")
    inst2.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst2.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst2.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst2.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst2.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst2.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst2.write("TRIGger:RFSA:GPRF:SOUR IF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR IF\n")
    inst2.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst2.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst2.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    sleep(0.02)
    fetch = inst2.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst3.write("SOURce:RFSG:GPRF:STATe OFF")

def ch2_gen_2():
    #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
    inst3.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2410, 2.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2410, 2.00\n")
    inst3.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
    inst3.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2410E6")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2410E6\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:IDLEtime 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime 1\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
    inst3.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
    inst3.write("SOURce:RFSG:GPRF:STATe ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
    
    opc = inst3.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
    #log_box.see(tk.END)
    fetch = inst3.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')

def ch3_capture_tx_2():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst2.write(":CONFigure:RFSA:GPRF:FREQuency 2415000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2415000000\n")
    inst2.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst2.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst2.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst2.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst2.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst2.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst2.write("TRIGger:RFSA:GPRF:SOUR IF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR IF\n")
    inst2.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst2.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst2.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    sleep(0.02)
    fetch = inst2.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst3.write("SOURce:RFSG:GPRF:STATe OFF")

def ch3_gen_2():
    #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
    inst3.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2415, 2.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2415, 2.00\n")
    inst3.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
    inst3.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2415E6")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2415E6\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:IDLEtime 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime 1\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
    inst3.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
    inst3.write("SOURce:RFSG:GPRF:STATe ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
    
    opc = inst3.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
    #log_box.see(tk.END)
    fetch = inst3.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')

def ch4_capture_tx_2():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst2.write(":CONFigure:RFSA:GPRF:FREQuency 2420000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2420000000\n")
    inst2.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst2.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst2.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst2.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst2.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst2.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst2.write("TRIGger:RFSA:GPRF:SOUR IF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR IF\n")
    inst2.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst2.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst2.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    sleep(0.02)
    fetch = inst2.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst3.write("SOURce:RFSG:GPRF:STATe OFF")

def ch4_gen_2():
    #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
    inst3.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2420, 2.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2420, 2.00\n")
    inst3.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
    inst3.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2420E6")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2420E6\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:IDLEtime 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime 1\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
    inst3.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
    inst3.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
    inst3.write("SOURce:RFSG:GPRF:STATe ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
    
    opc = inst3.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
    #log_box.see(tk.END)
    fetch = inst3.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')

def Init():
    # TX  INIT
    #inst.write(" :TRIGger:RFSA:WLAN:TOUT 2")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :TRIGger:RFSA:WLAN:TOUT 2\n")
   # inst.write(":TRIGger:RFSA:WLAN:THReshold -22.0000")
  #  log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :TRIGger:RFSA:WLAN:THReshold -22.0000\n")
    #inst.write(":TRIGger:RFSA:WLAN:DELay 0.0 ms")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :TRIGger:RFSA:WLAN:DELay 0.0 ms\n")
    
    #inst.write(":CONFigure:RFSA:WLAN:POWer:AUTO OFF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:POWer:AUTO OFF\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:TXPower:AVERaging 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":CONFigure:RFSA:WLAN:MEASurement:TXPower:AVERaging 1\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:SEM:AVERaging 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:SEM:AVERaging 1\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:AVERaging 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":CONFigure:RFSA:WLAN:MEASurement:MODulation:AVERaging 1\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp:AVERages 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:PRAMp:AVERages 1\n")
    
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:TXPower ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:TXPower ON\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:SEM ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:SEM ON\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation ON\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:GPOW OFF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:GPOW OFF\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF\n")
    
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:HDETection ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:HDETection ON\n")
    
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:EQUalization OFF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:EQUalization OFF\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:TRACking:PHASe STANdard")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:TRACking:PHASe STANdard\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter RCOSine")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter RCOSine\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter:COEFficient 0.5")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter:COEFficient 0.5\n")
    
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:AMPLitude OFF")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:AMPLitude OFF ms\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:PHASe STANdard")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:PHASe STANdard\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:TIME ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:TIME ON\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:CHANnel ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:CHANnel ON\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:MSYMbols 16")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:MSYMbols 16\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:CFOMethod PDATa")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:CFOMethod PDATa\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP ON")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP ON\n")
    #inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP:FFORmat GREenfield")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP:FFORmat GREenfield\n")
    
    #opc = inst.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" +"*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"  + opc + " \n")
    #syserr = inst.query(":SYSTem:ERRor?")

    #log_box.insert(tk.END,  datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" +":SYST:ERR? \n" + syserr + '\n')
    #log_box.insert(tk.END,  datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA RECV]" +syserr + '\n')
    #log_box.see(tk.END)
    ch1_gen_1()
    ch1_capture_tx_1()
    ch2_gen_1()
    ch2_capture_tx_1()
    ch3_gen_1()
    ch3_capture_tx_1()
    ch4_gen_1()
    ch4_capture_tx_1()
    ch1_gen_2()
    ch1_capture_tx_2()
    ch2_gen_2()
    ch2_capture_tx_2()
    ch3_gen_2()
    ch3_capture_tx_2()
    ch4_gen_2()
    ch4_capture_tx_2()

ret = tk.StringVar()
connect_button = ttk.Button(connection, text='Connect Tester', width = 30, command=Init)
connect_button.grid(column=0, row=0, pady= 15)
disconnect_button = ttk.Button(connection, text='Disconnect Tester', width = 30)
disconnect_button.grid(column=1, row=0)



#Measurement


    
 
measurement = tk.LabelFrame(entry, text='Measurement')
measurement.grid(column=0,row=1)

b_tx_button = ttk.Button(measurement, text='ch1_capture_tx_1_1 Setting', width = 30, command=ch1_capture_tx_1)
b_tx_button.grid(column=0, row=1, pady= 10)
b_rx_button = ttk.Button(measurement, text='ch1_gen_1 Per Measurement', width = 30, command=ch1_gen_1)
b_rx_button.grid(column=1, row=1)



#CW


#Log

def clear():
    log_box.delete(1.0, tk.END)


clear_button = tk.Button(log, text= 'CLEAR', width= 10, command=clear)
clear_button.grid(column=0, row=2)

win.mainloop()