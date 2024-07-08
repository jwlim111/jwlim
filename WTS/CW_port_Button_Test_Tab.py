#!/usr/bin/python

import tkinter as tk
from tkinter import ttk
import pyvisa as visa
from tkinter import scrolledtext
from time import sleep
from datetime import datetime
from tkinter import *
import tkinter.messagebox as mbox



def connect():
    global inst0, inst1, inst2, inst3, inst4, inst5, inst6, inst7, rm
    rm = visa.ResourceManager()
    if p0.get() == 1:
        try:
            inst0 = rm.open_resource('TCPIP0::192.168.100.254::inst0::INSTR',  
                write_termination = '\n', read_termination='\n')
        except:
            print("Port 0 Connection Fail")
        else:
            print("Port 0 Connection Sucess")
    
    if p1.get() == 1:
        try:
            inst1 = rm.open_resource('TCPIP0::192.168.100.254::inst1::INSTR',  
                write_termination = '\n', read_termination='\n')
        except:
            print("Port 1 Connection Fail")
        else:
            print("Port 1 Connection Sucess")
            
            
    if p2.get() == 1:
        try:
            inst2 = rm.open_resource('TCPIP0::192.168.100.254::inst2::INSTR',  
                write_termination = '\n', read_termination='\n')
        except:
            print("Port 2 Connection Fail")
        else:
            print("Port 2 Connection Sucess")
    
    if p3.get() == 1:
        try:
            inst3 = rm.open_resource('TCPIP0::192.168.100.254::inst3::INSTR',  
                write_termination = '\n', read_termination='\n')
        except:
            print("Port 3 Connection Fail")
        else:
            print("Port 3 Connection Sucess")
            
    if p4.get() == 1:
        try:
            inst4 = rm.open_resource('TCPIP0::192.168.100.254::inst4::INSTR',  
                write_termination = '\n', read_termination='\n')
        except:
            print("Port 4 Connection Fail")
        else:
            print("Port 4 Connection Sucess")
    
    if p5.get() == 1:
        try:
            inst5 = rm.open_resource('TCPIP0::192.168.100.254::inst5::INSTR',  
                write_termination = '\n', read_termination='\n')
        except:
            print("Port 5 Connection Fail")
        else:
            print("Port 5 Connection Sucess")
            
    if p6.get() == 1:
        try:
            inst6 = rm.open_resource('TCPIP0::192.168.100.254::inst6::INSTR',  
                write_termination = '\n', read_termination='\n')
        except:
            print("Port 6 Connection Fail")
        else:
            print("Port 6 Connection Sucess")
    
    if p7.get() == 1:
        try:
            inst7 = rm.open_resource('TCPIP0::192.168.100.254::inst7::INSTR',  
                write_termination = '\n', read_termination='\n')
        except:
            print("Port 7 Connection Fail")
        else:
            print("Port 7 Connection Sucess")
    else:
        return

def disconnect():
    try:
        rm.close()
    except:
        print("Disconnection Fail")
    else:
        print("WTS Disconnected")


win = Tk()

win.title('WTS Tester') 

#Port CheckBox
check = tk.LabelFrame(win,text="Select Port")
check.grid(column=0, row=0)
p0 = IntVar()
p1 = IntVar()
p2 = IntVar()
p3 = IntVar()
p4 = IntVar()
p5 = IntVar()
p6 = IntVar()
p7 = IntVar()

port0 = Checkbutton(check, text='Port0', variable=p0)
port0.grid(column=0,row=0)
port1 = Checkbutton(check, text="Port1", variable=p1)
port1.grid(column=1,row=0)
port2 = Checkbutton(check, text="Port2", variable=p2)
port2.grid(column=2,row=0)
port3 = Checkbutton(check, text="Port3", variable=p3)
port3.grid(column=3,row=0)
port4 = Checkbutton(check, text="Port4", variable=p4)
port4.grid(column=4,row=0)
port5 = Checkbutton(check, text="Port5", variable=p5)
port5.grid(column=5,row=0)
port6 = Checkbutton(check, text="Port6", variable=p6)
port6.grid(column=6,row=0)
port7 = Checkbutton(check, text="Port7", variable=p7)
port7.grid(column=7,row=0)

#LabelFrame
entry = tk.LabelFrame(win,text='WTS')
entry.grid(column=0, row=1)

#IP Address
ip_address = tk.LabelFrame(entry, text='IP Address')
ip_address.grid(column=0,row=0)

ip_label = Label(ip_address, text='IP Address : (xxx.xxx.xxx.xxx)')
ip_label.grid(column=0,row=0)

ip_wts = IntVar()
ip_box = Entry(ip_address, textvariable=ip_wts, width=20)
ip_box.grid(column=1,row=0)

#Connection
connection = tk.LabelFrame(entry, text='Connection')
connection.grid(column=0,row=1, pady= 20)

#Log_Box
log = ttk.LabelFrame(win, text='Log')
log.grid(column=1, row=1)

log_box = scrolledtext.ScrolledText(log)
log_box.grid(column=0,row=0)

#Setting
settings = tk.LabelFrame(entry, text='Settings')
settings.grid(column=0,row=2)

frequency = IntVar()
power = IntVar()

str_freq = Label(settings, text='Center Frequency(MHz) : ')
str_freq.grid(column=0,row=0)
set_freq = Entry(settings, width=10, textvariable = frequency)
set_freq.grid(column=1,row=0)

str_power = Label(settings, text='Power(dBm) : ')
str_power.grid(column=2,row=0)
set_power = Entry(settings, width=10, textvariable = power)
set_power.grid(column=3,row=0)








def ch1_capture_tx_1():
   
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    ref = int(set_power.get()) + 3
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst1.write(":CONFigure:RFSA:GPRF:FREQuency "+set_freq.get()+"000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2405000000\n")
    inst1.write(":CONFigure:RFSA:GPRF:POWer "+str(ref))
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst1.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst1.write("TRIGger:RFSA:GPRF:SOUR FREE")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR FREE\n")
    inst1.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst1.write(":INITiate:RFSA:GPRF:POWer")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")

    
    opc = inst1.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    fetch = inst1.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    sleep(0.02)
    inst0.write("SOURce:RFSG:GPRF:STATe OFF")

def ch1_gen_1():
    if set_freq.get() != '0' :
        #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
        inst0.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, "+set_freq.get()+", 0.00")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00\n")
        inst0.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
        inst0.write("SOURce:RFSG:GPRF:RFSettings:FREQuency "+set_freq.get()+"E6")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:IDLEtime -1")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime -1\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
        inst0.write("SOURce:RFSG:GPRF:RFSettings:LEVel "+set_power.get())
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
        inst0.write("SOURce:RFSG:GPRF:STATe ON")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
        
        opc = inst0.query("*OPC?")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
        #log_box.see(tk.END)
        status = inst0.query(":SOURce:RFSG:GPRF:STATUS?")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + status + '\n')
    else:
        mbox.showwarning("ERROR", "Please set Frequency and Power before Generate Signal")
        return

def ch2_capture_tx_1():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst1.write(":CONFigure:RFSA:GPRF:FREQuency 2410000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2405000000\n")
    inst1.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst1.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst1.write("TRIGger:RFSA:GPRF:SOUR FREE")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR FREE\n")
    inst1.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst1.write(":INITiate:RFSA:GPRF:POWer")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst1.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    fetch = inst1.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst0.write("SOURce:RFSG:GPRF:STATe OFF")

def ch2_gen_1():
    if set_freq.get() != '0' :
        #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
        inst0.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2410, 2.00")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00\n")
        inst0.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
        inst0.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2410E6")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:IDLEtime -1")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime -1\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
        inst0.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
        inst0.write("SOURce:RFSG:GPRF:STATe ON")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
        
        opc = inst0.query("*OPC?")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
        #log_box.see(tk.END)
        status = inst0.query(":SOURce:RFSG:GPRF:STATUS?")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + status + '\n')
    else:
        mbox.showwarning("ERROR", "Please set Frequency and Power before Generate Signal")
        return

def ch3_capture_tx_1():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst1.write(":CONFigure:RFSA:GPRF:FREQuency 2415000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2405000000\n")
    inst1.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst1.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst1.write("TRIGger:RFSA:GPRF:SOUR FREE")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR FREE\n")
    inst1.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst1.write(":INITiate:RFSA:GPRF:POWer")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst1.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    fetch = inst1.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst0.write("SOURce:RFSG:GPRF:STATe OFF")

def ch3_gen_1():
    
    if set_freq.get() != '0' :
        #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
        inst0.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2415, 2.00")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2415, 2.00\n")
        inst0.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
        inst0.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2415E6")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2415E6\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:IDLEtime -1")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime -1\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
        inst0.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
        inst0.write("SOURce:RFSG:GPRF:STATe ON")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
        
        opc = inst0.query("*OPC?")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
        #log_box.see(tk.END)
        fetch = inst0.query(":SOURce:RFSG:GPRF:STATUS?")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    
    else:
        mbox.showwarning("ERROR", "Please set Frequency and Power before Generate Signal")
        return

def ch4_capture_tx_1():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst1.write(":CONFigure:RFSA:GPRF:FREQuency 2420000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2420000000\n")
    inst1.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst1.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst1.write("TRIGger:RFSA:GPRF:SOUR FREE")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR FREE\n")
    inst1.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst1.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst1.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    fetch = inst1.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst0.write("SOURce:RFSG:GPRF:STATe OFF")

def ch4_gen_1():
    
    if set_freq.get() != '0' :
        #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
        inst0.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2420, 2.00")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2420, 2.00\n")
        inst0.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
        inst0.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2420E6")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2420E6\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:IDLEtime -1")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime -1\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
        inst0.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
        inst0.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
        #log0_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
        inst0.write("SOURce:RFSG:GPRF:STATe ON")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
        
        opc = inst0.query("*OPC?")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
        #log_box.see(tk.END)
        status = inst0.query(":SOURce:RFSG:GPRF:STATUS?")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + status + '\n')
    
    else:
        mbox.showwarning("ERROR", "Please set Frequency and Power before Generate Signal")
        return

def ch1_capture_tx_2():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst3.write(":CONFigure:RFSA:GPRF:FREQuency 2405000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2405000000\n")
    inst3.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst3.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst3.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst3.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst3.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst3.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst3.write("TRIGger:RFSA:GPRF:SOUR FREE")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR FREE\n")
    inst3.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst3.write(":INITiate:RFSA:GPRF:POWer")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst3.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    fetch = inst3.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst2.write("SOURce:RFSG:GPRF:STATe OFF")

def ch1_gen_2():
    
    if set_freq.get() != '0' :
        #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
        inst2.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00\n")
        inst2.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
        inst2.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:IDLEtime -1")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime -1\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
        inst2.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
        inst2.write("SOURce:RFSG:GPRF:STATe ON")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
        
        opc = inst2.query("*OPC?")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
        #log_box.see(tk.END)
        status = inst2.query(":SOURce:RFSG:GPRF:STATUS?")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + status + '\n')
    
    else:
        mbox.showwarning("ERROR", "Please set Frequency and Power before Generate Signal")
        return

def ch2_capture_tx_2():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst3.write(":CONFigure:RFSA:GPRF:FREQuency 2410000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2410000000\n")
    inst3.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst3.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst3.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst3.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst3.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst3.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst3.write("TRIGger:RFSA:GPRF:SOUR FREE")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR FREE\n")
    inst3.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst3.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst3.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    fetch = inst3.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst2.write("SOURce:RFSG:GPRF:STATe OFF")

def ch2_gen_2():
    
    if set_freq.get() != '0' :
        #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
        inst2.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2410, 2.00")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2410, 2.00\n")
        inst2.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
        inst2.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2410E6")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2410E6\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:IDLEtime -1")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime -1\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
        inst2.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
        inst2.write("SOURce:RFSG:GPRF:STATe ON")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
        
        opc = inst2.query("*OPC?")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
        #log_box.see(tk.END)
        status = inst2.query(":SOURce:RFSG:GPRF:STATUS?")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + status + '\n')
    
    else:
        mbox.showwarning("ERROR", "Please set Frequency and Power before Generate Signal")
        return

def ch3_capture_tx_2():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst3.write(":CONFigure:RFSA:GPRF:FREQuency 2415000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2415000000\n")
    inst3.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst3.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst3.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst3.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst3.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst3.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst3.write("TRIGger:RFSA:GPRF:SOUR FREE")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR FREE\n")
    inst3.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst3.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst3.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    fetch = inst3.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst2.write("SOURce:RFSG:GPRF:STATe OFF")

def ch3_gen_2():
    
    if set_freq.get() != '0' :
        #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
        inst2.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2415, 2.00")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2415, 2.00\n")
        inst2.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
        inst2.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2415E6")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2415E6\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:IDLEtime -1")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime -1\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
        inst2.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
        inst2.write("SOURce:RFSG:GPRF:STATe ON")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
        
        opc = inst2.query("*OPC?")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
        #log_box.see(tk.END)
        fetch = inst2.query(":SOURce:RFSG:GPRF:STATUS?")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    
    else:
        mbox.showwarning("ERROR", "Please set Frequency and Power before Generate Signal")
        return

def ch4_capture_tx_2():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"---------------Sense---------------\n")
    

    inst3.write(":CONFigure:RFSA:GPRF:FREQuency 2420000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2420000000\n")
    inst3.write(":CONFigure:RFSA:GPRF:POWer -27.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -27.00\n")
    inst3.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst3.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst3.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst3.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.001")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.001\n")
    inst3.write("TRIGger:RFSA:GPRF:EDGE RISING")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst3.write("TRIGger:RFSA:GPRF:SOUR FREE")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR FREE\n")
    inst3.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst3.write(":INITiate:RFSA:GPRF:POWer")
   # log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst3.query("*OPC?")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" + " \n")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    fetch = inst3.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    inst2.write("SOURce:RFSG:GPRF:STATe OFF")

def ch4_gen_2():
    
    if set_freq.get() != '0' :
        #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') +"--------------SOURCE-----------\n")
        inst2.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2420, 2.00")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2420, 2.00\n")
        inst2.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
        inst2.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2420E6")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2420E6\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:IDLEtime -1")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime -1\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:REPetition 0")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 0\n")
        inst2.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
        inst2.write("SOURce:RFSG:GPRF:ARB:CYCLes -1")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes -1\n")
        inst2.write("SOURce:RFSG:GPRF:STATe ON")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
        
        opc = inst2.query("*OPC?")
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + "*OPC? \n" )
        #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]"+ opc + " \n")
        #log_box.see(tk.END)
        status = inst2.query(":SOURce:RFSG:GPRF:STATUS?")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
        log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA RECV]" + status + '\n')
    
    else:
        mbox.showwarning("ERROR", "Please set Frequency and Power before Generate Signal")
        return

def Stop():
    inst0.write("SOURce:RFSG:GPRF:STATe OFF")

def TestAll():
    # TX  INIT
    #inst.write(" :TRIGger:RFSA:WLAN:TOUT 2")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :TRIGger:RFSA:WLAN:TOUT 2\n")
    #inst.write(":TRIGger:RFSA:WLAN:THReshold -22.0000")
    #log_box.insert(tk.END, datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + "[VISA SEND]" + " :TRIGger:RFSA:WLAN:THReshold -22.0000\n")
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
    """
    ch1_gen_1()
    ch1_capture_tx_1()
    ch1_gen_2()
    ch1_capture_tx_2()
    ch2_gen_1()
    ch2_capture_tx_1()
    ch2_gen_2()
    ch2_capture_tx_2()
    ch3_gen_1()
    ch3_capture_tx_1()
    ch3_gen_2()
    ch3_capture_tx_2()
    ch4_gen_1()
    ch4_capture_tx_1()
    ch4_gen_2()
    ch4_capture_tx_2()
    """

ret = tk.StringVar()
connect_button = ttk.Button(connection, text='Connect Tester', width = 30, command=connect)
connect_button.grid(column=0, row=0, pady= 15)
disconnect_button = ttk.Button(connection, text='Disconnect Tester', width = 30, command=disconnect)
disconnect_button.grid(column=1, row=0)



#Measurement


    
 
measurement = tk.LabelFrame(entry, text='Measurement')
measurement.grid(column=0,row=3)

ch1p1_tx_button = ttk.Button(measurement, text='ch1_capture_tx_1 ', width = 30, command=ch1_capture_tx_1)
ch1p1_tx_button.grid(column=0, row=1, pady= 10)
ch1p1_rx_button = ttk.Button(measurement, text='ch1_gen_1 ', width = 30, command=ch1_gen_1)
ch1p1_rx_button.grid(column=1, row=1)
ch1p1_stop_button = ttk.Button(measurement, text='stop ', width = 30, command=Stop)
ch1p1_stop_button.grid(column=2, row=1)

ch1p5_tx_button = ttk.Button(measurement, text='ch1_capture_tx_2 ', width = 30, command=ch1_capture_tx_2)
ch1p5_tx_button.grid(column=0, row=2, pady= 10)
ch1p5_rx_button = ttk.Button(measurement, text='ch1_gen_2 ', width = 30, command=ch1_gen_2)
ch1p5_rx_button.grid(column=1, row=2)

ch2p1_tx_button = ttk.Button(measurement, text='ch2_capture_tx_1 ', width = 30, command=ch2_capture_tx_1)
ch2p1_tx_button.grid(column=0, row=3, pady= 10)
ch2p1_rx_button = ttk.Button(measurement, text='ch2_gen_1 ', width = 30, command=ch2_gen_1)
ch2p1_rx_button.grid(column=1, row=3)

ch2p5_tx_button = ttk.Button(measurement, text='ch2_capture_tx_2 ', width = 30, command=ch2_capture_tx_2)
ch2p5_tx_button.grid(column=0, row=4, pady= 10)
ch2p5_rx_button = ttk.Button(measurement, text='ch2_gen_2 ', width = 30, command=ch2_gen_2)
ch2p5_rx_button.grid(column=1, row=4)

ch3p1_tx_button = ttk.Button(measurement, text='ch3_capture_tx_1 ', width = 30, command=ch3_capture_tx_1)
ch3p1_tx_button.grid(column=0, row=5, pady= 10)
ch3p1_rx_button = ttk.Button(measurement, text='ch3_gen_1 ', width = 30, command=ch3_gen_1)
ch3p1_rx_button.grid(column=1, row=5)

ch3p5_tx_button = ttk.Button(measurement, text='ch3_capture_tx_2 ', width = 30, command=ch3_capture_tx_1)
ch3p5_tx_button.grid(column=0, row=6, pady= 10)
ch3p5_rx_button = ttk.Button(measurement, text='ch3_gen_2 ', width = 30, command=ch3_gen_2)
ch3p5_rx_button.grid(column=1, row=6)

ch4p1_tx_button = ttk.Button(measurement, text='ch4_capture_tx_1 ', width = 30, command=ch4_capture_tx_1)
ch4p1_tx_button.grid(column=0, row=7, pady= 10)
ch4p1_rx_button = ttk.Button(measurement, text='ch4_gen_1 ', width = 30, command=ch4_gen_1)
ch4p1_rx_button.grid(column=1, row=7)

ch4p5_tx_button = ttk.Button(measurement, text='ch4_capture_tx_2 ', width = 30, command=ch4_capture_tx_2)
ch4p5_tx_button.grid(column=0, row=8, pady= 10)
ch4p5_rx_button = ttk.Button(measurement, text='ch4_gen_2 ', width = 30, command=ch4_gen_2)
ch4p5_rx_button.grid(column=1, row=8)

ta_tx_button = ttk.Button(measurement, text='TestAll ', width = 30, command=TestAll)
ta_tx_button.grid(column=0, row=9, pady= 10)



#CW


#Log

def clear():
    log_box.delete(1.0, tk.END)


clear_button = tk.Button(log, text= 'CLEAR', width= 10, command=clear)
clear_button.grid(column=0, row=2)

win.mainloop()