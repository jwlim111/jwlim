#!/usr/bin/python

import tkinter as tk
from tkinter import ttk
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

now = datetime.now()


win = ThemedTk(theme='blue')

win.title('WTS Tester') 

#LabelFrame
entry = tk.LabelFrame(win,text='WTS')
entry.grid(column=0, row=0)

#Connection

connection = tk.LabelFrame(entry, text='Connection')
connection.grid(column=0,row=0, pady= 20)



def Init():
    # TX  INIT
    inst.write(" :TRIGger:RFSA:WLAN:TOUT 2")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :TRIGger:RFSA:WLAN:TOUT 2\n")
    inst.write(":TRIGger:RFSA:WLAN:THReshold -22.0000")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :TRIGger:RFSA:WLAN:THReshold -22.0000\n")
    inst.write(":TRIGger:RFSA:WLAN:DELay 0.0 ms")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :TRIGger:RFSA:WLAN:DELay 0.0 ms\n")
    
    inst.write(":CONFigure:RFSA:WLAN:POWer:AUTO OFF")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:POWer:AUTO OFF\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:TXPower:AVERaging 1")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + ":CONFigure:RFSA:WLAN:MEASurement:TXPower:AVERaging 1\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:SEM:AVERaging 1")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:SEM:AVERaging 1\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:AVERaging 1")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + ":CONFigure:RFSA:WLAN:MEASurement:MODulation:AVERaging 1\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp:AVERages 1")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:PRAMp:AVERages 1\n")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:TXPower ON")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:TXPower ON\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:SEM ON")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:SEM ON\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation ON")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation ON\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:GPOW OFF")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:GPOW OFF\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF\n")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:HDETection ON")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:HDETection ON\n")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:EQUalization OFF")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:EQUalization OFF\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:TRACking:PHASe STANdard")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:TRACking:PHASe STANdard\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter RCOSine")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter RCOSine\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter:COEFficient 0.5")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter:COEFficient 0.5\n")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:AMPLitude OFF")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:AMPLitude OFF ms\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:PHASe STANdard")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:PHASe STANdard\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:TIME ON")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:TIME ON\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:CHANnel ON")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:CHANnel ON\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:MSYMbols 16")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:MSYMbols 16\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:CFOMethod PDATa")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:CFOMethod PDATa\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP ON")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP ON\n")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP:FFORmat GREenfield")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP:FFORmat GREenfield\n")
    
    opc = inst.query("*OPC?")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" +"*OPC? \n" + " \n")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA RECV]"  + opc + " \n")
    syserr = inst.query(":SYSTem:ERRor?")

    log_box.insert(tk.END,  "[VISA SEND]" +":SYST:ERR? \n" + syserr + '\n')
    log_box.insert(tk.END,  "[VISA RECV]" +syserr + '\n')
    log_box.see(tk.END)

ret = tk.StringVar()
connect_button = ttk.Button(connection, text='Connect Tester', width = 30, command=Init)
connect_button.grid(column=0, row=0, pady= 15)
disconnect_button = ttk.Button(connection, text='Disconnect Tester', width = 30)
disconnect_button.grid(column=1, row=0)

#Measurement

def sa11b():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    log_box.insert(tk.END, "---------------Sense---------------\n")
    
    inst.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00\n")
    inst.write(":CONFigure:RFSA:GPRF:FREQuency 2405000000")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:FREQuency 2405000000\n")
    inst.write(":CONFigure:RFSA:GPRF:POWer -10.00")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:POWer -10.00\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000\n")
    inst.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:TXPower:INTerval 1\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DELay 0\n")
    inst.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.01")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:RFSA:GPRF:SLOT:DURation 0.01\n")
    inst.write("TRIGger:RFSA:GPRF:EDGE RISING")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:EDGE RISING\n")
    inst.write("TRIGger:RFSA:GPRF:SOUR SOURCE_LM")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR SOURCE_LM\n")
    inst.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:THREshold -40.00\n")
    inst.write("TRIGger:RFSA:GPRF:SOUR SOURCE_LM")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " TRIGger:RFSA:GPRF:SOUR SOURCE_LM\n")
    inst.write(":INITiate:RFSA:GPRF:POWer")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :INITiate:RFSA:GPRF:POWer\n")
    
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + "*OPC? \n" + " \n")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA RECV]" +  opc + " \n")
    log_box.see(tk.END)
    fetch = inst.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + "FETCh:RFSA:GPRF:POWer? \n" + '\n')
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA RECV]" +  fetch + '\n')
    log_box.see(tk.END)

def sa11g():
    # ==TX[11G_54M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====


    #  config 
    inst.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2442, 9.00")
    syserr = inst.query(":SYST:ERR?")
    log_box.insert(tk.END, ":SYST:ERR? \n" + syserr + '\n')
    log_box.see(tk.END)
    
    inst.write(":CONFigure:RFSA:WLAN:STANdard A_G")
    inst.write(":CONFigure:RFSA:WLAN:BWIDth BW20")
    inst.write(":CONFigure:RFSA:WLAN:FREquency 2442 MHz")
    inst.write(":CONFigure:RFSA:WLAN:POWer 26.00")                                          # 측정 power + 11 (ofdm)
    
    inst.write(":CONFigure:RFSA:WLAN:ALENgth 0.50 ms")
    
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:CFResponse ON")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:CHANnel ON")       # channel estimation on : ON, channel estimation on : OFF
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLENgth 1024")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:GINTerval LONG")
    
    opc = inst.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    syserr = inst.query(":SYSTem:ERRor?")
    
    # capture
    
    inst.write(":INITiate:RFSA:WLAN")
    
    state = str(inst.query(":FETCh:RFSA:WLAN:STATe?"))
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:STATe? \n" + state + '\n')
    log_box.see(tk.END)
    
    syserr = inst.query(":SYST:ERR?")
    log_box.insert(tk.END, ":SYST:ERR? \n" + syserr + '\n')
    log_box.see(tk.END)
    
    
    # =====[DUT_CONTROL_WIFI_TX_STOP]=====

    # // fetch


    # /* transmitPower,PeakPower,TransmitPowerWGap*/
    
    reuslt = inst.query(":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults? \n" + reuslt + " \n")
    log_box.see(tk.END)
    
    #/*	Average sample clock offset, (ppm)
	# Average carrier frequency offset, (Hz)
	# Average RMS common pilot error, 
	# Average carrier frequency leakage, 
	# Average IQ imbalance, 
	# Average quadrature skew, 
	# Average timing skew
    # */
    
    impair = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:IMPairments?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:IMPairments? \n" + impair + " \n")
    log_box.see(tk.END)
    
    # /*RMS EVM, Max EVM, Data EVM, Pilot EVM*/
    
    evm = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:EVM?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:EVM? \n" + evm + " \n")
    log_box.see(tk.END)
    
    # /*Average spectral flatness margin, Smallest spectral flatness margin, Index of smallest spectral flatness margin*/
    
    margin = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:SFMargin?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:SFMargin? \n" + margin + " \n")
    log_box.see(tk.END)
    
    # /*	
	# // 처음 2개,
	# Worst margin for all segments,
	# Worst frequency for all segments,
	
	# // 반복
	# margin for frequncy segment,
	# Reference level for frequncy segment,
	# Violation for for frequncy segment,
	# Frequency of smallest margin for frequncy segment
	# */
 
    result = inst.query(":FETCh:RFSA:WLAN:MEASurement:SEM:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:SEM:RESults? \n" + result + '\n')
    log_box.see(tk.END)
    
def sa11n():
    # ==TX[11N_HT20_MCS7_2442MHz(CH:7)_Ant1]==


    # =====[DUT_CONTROL_WIFI_TX]=====


    # // config 
        
    inst.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2442, 9.00")
    syserr = inst.query(":SYST:ERR?")
    log_box.insert(tk.END, ":SYST:ERR? \n" + syserr + '\n')
    log_box.see(tk.END)
    
    inst.write(":CONFigure:RFSA:WLAN:STANdard N")
    inst.write(":CONFigure:RFSA:WLAN:BWIDth BW20")
    inst.write(":CONFigure:RFSA:WLAN:FREquency 2442 MHz")
    inst.write(":CONFigure:RFSA:WLAN:POWer 25.00")                                          # 측정 power + 11 (ofdm)
    
    inst.write(":CONFigure:RFSA:WLAN:ALENgth 0.50 ms")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:CFResponse ON")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:CHANnel ON")      # channel estimation on : ON, channel estimation on : OFF
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLENgth 1024")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:GINTerval LONG")
    
    opc = inst.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    # // capture
    
    inst.write(":INITiate:RFSA:WLAN")
    opc = inst.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    state = str(inst.query(":FETCh:RFSA:WLAN:STATe?"))
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:STATe? \n" + state + '\n')
    log_box.see(tk.END)
    
    syserr = inst.query(":SYST:ERR?")
    log_box.insert(tk.END, ":SYST:ERR? \n" + syserr + '\n')
    log_box.see(tk.END)
    
    txpower = inst.query(":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults? \n" + txpower + '\n')
    log_box.see(tk.END)
    
    impair = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:IMPairments?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:IMPairments? \n" + impair + '\n')
    log_box.see(tk.END)
    
    evm = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:EVM?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:EVM? \n" + evm + '\n')
    log_box.see(tk.END)
    
    sfmargin = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:SFMargin?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:SFMargin \n" + sfmargin + '\n')
    log_box.see(tk.END)
    
    sem = inst.query(":FETCh:RFSA:WLAN:MEASurement:SEM:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:SEM:RESults? \n" + sem + '\n')
    log_box.see(tk.END)
    
def sa11ac():
    # ==TX[11AC_VHT80_MCS9_5210MHz(CH:42)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====


    # // config 
    inst.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 5210, 10.00")
    syserr = inst.query(":SYST:ERR?")
    log_box.insert(tk.END, ":SYST:ERR? \n" + syserr + '\n')
    log_box.see(tk.END)
    
    inst.write(":CONFigure:RFSA:WLAN:STANdard AC")
    inst.write(":CONFigure:RFSA:WLAN:BWIDth BW80")
    inst.write(":CONFigure:RFSA:WLAN:FREquency 5210 MHz")
    inst.write(":CONFigure:RFSA:WLAN:POWer 17.00")
    inst.write(":CONFigure:RFSA:WLAN:ALENgth 0.50 ms")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:CFResponse ON")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:CHANnel ON")          # channel estimation on : ON, channel estimation on : OFF
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLENgth 1024")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:GINTerval LONG")
    
    opc = inst.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    # // capture
    
    inst.write(":INITiate:RFSA:WLAN")
    opc = inst.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    state = str(inst.query(":FETCh:RFSA:WLAN:STATe?"))
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:STATe? \n" + state + '\n')
    log_box.see(tk.END)
    
    syserr = inst.query(":SYST:ERR?")
    log_box.insert(tk.END, ":SYST:ERR? \n" + syserr + '\n')
    log_box.see(tk.END)
    
    # // fetch
    txpower = inst.query(":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults? \n" + txpower + '\n')
    log_box.see(tk.END)
    
    impair = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:IMPairments?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:IMPairments? \n" + impair + '\n')
    log_box.see(tk.END)
    
    evm = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:EVM?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:EVM? \n" + evm + '\n')
    log_box.see(tk.END)
    
    sfmargin = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:SFMargin?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:SFMargin \n" + sfmargin + '\n')
    log_box.see(tk.END)
    
    sem = inst.query(":FETCh:RFSA:WLAN:MEASurement:SEM:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:SEM:RESults? \n" + sem + '\n')
    log_box.see(tk.END)
    
def rx11b():
    #==RX Min PER[11B_11M_2442MHz(CH:7)_Ant1]==
    log_box.insert(tk.END, "--------------SOURCE-----------\n")
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " :CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00\n")
    inst1.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " SOURce:RFSG:GPRF:LIST:WAVeform CW\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:IDLEtime 5")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:IDLEtime 5\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:REPetition 1")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:REPetition 1\n")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " SOURce:RFSG:GPRF:RFSettings:LEVel -30.00\n")
    inst1.write("SOURce:RFSG:GPRF:ARB:CYCLes 1000")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " SOURce:RFSG:GPRF:ARB:CYCLes 1000\n")
    inst1.write("SOURce:RFSG:GPRF:STATe ON")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + " SOURce:RFSG:GPRF:STATe ON\n")
    
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + "*OPC? \n" )
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA RECV]"+ opc + " \n")
    log_box.see(tk.END)
    fetch = inst.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA SEND]" + ":SOURce:RFSG:GPRF:STATUS? \n")
    log_box.insert(tk.END, now.strftime('%Y-%m-%d %H:%M:%S') + "[VISA RECV]" + fetch + '\n')
    log_box.see(tk.END)
    
def rx11g():
    # ==RX Min PER[11G_54M_2442MHz(CH:7)_Ant1]==
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2442, 30.00")
    inst1.write(":SOURce:RFSG:WLAN:PAYLoad:TYPE PN9")
    inst1.write(":SOURce:RFSG:WLAN:PAYLoad:MACAddress 0x010000C0FFEE")
    inst1.write(":SOURce:RFSG:WLAN:PAYLoad:LENGth 1024")
    inst1.write(":SOURce:RFSG:WLAN:STANdard A_G")
    inst1.write(":SOURce:RFSG:WLAN:IINTerval 0.001")
    inst1.write(":SOURce:RFSG:WLAN:BWIDth BW20")
    inst1.write(":SOURce:RFSG:WLAN:CFRequency 2.442 GHz")
    inst1.write(":SOURce:RFSG:WLAN:POWer -31.00")
    inst1.write(":SOURce:RFSG:WLAN:DRATe OFDM_54M")
    inst1.write(":SOURce:RFSG:WLAN:NOCHains 1")
    inst1.write(":SOURce:RFSG:WLAN:PACKets 5000000")
    
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    inst1.write(":SOURce:RFSG:WLAN:CWAVeform")
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    syserr = inst1.query(":SYST:ERR?")
    log_box.insert(tk.END, ":SYST:ERR? \n" + syserr + '\n')
    log_box.see(tk.END)
    
    # =====[DUT_CONTROL_WIFI_RX]=====
    inst1.write(":SOURce:RFSG:WLAN:GENerate ON")
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    state = str(inst.query(":FETCh:RFSA:WLAN:STATe?"))
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:STATe? \n" + state + '\n')
    log_box.see(tk.END)
    
    txpower = inst.query(":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults? \n" + txpower + '\n')
    log_box.see(tk.END)
    
    pramp = inst.query(":FETCh:RFSA:WLAN:MEASurement:PRAMp:RTIMe?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:PRAMp:RTIMe? \n" + pramp + '\n')
    log_box.see(tk.END)
    
    #Average sample clock offset, Average carrier frequency offset, Average RMS phase noise, Average carrier suppression, Average IQ imbalance, Average quadrature skew
    impair = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:IMPairments?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:IMPairments? \n" + impair + '\n')
    log_box.see(tk.END)
    
    #RMS EVM, Peak EVM, 802.11B Peak EVM, 802.11B Peak EVM (2007) dB
    evm = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:EVM?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:EVM? \n" + evm + '\n')
    log_box.see(tk.END)
    
    sem = inst.query(":FETCh:RFSA:WLAN:MEASurement:SEM:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:SEM:RESults? \n" + sem + '\n')
    log_box.see(tk.END)
    
    # =====[DUT_CONTROL_WIFI_RX_Fetch]=====
    
    inst1.write(":SOURce:RFSG:WLAN:GENerate OFF")
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
def rx11n():
    
    #// RX 11N HT20
    
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2442, 30.00")
    inst1.write(":SOURce:RFSG:WLAN:PAYLoad:TYPE PN9")
    inst1.write(":SOURce:RFSG:WLAN:PAYLoad:MACAddress 0x010000C0FFEE")
    inst1.write(":SOURce:RFSG:WLAN:PAYLoad:LENGth 1024")
    inst1.write(":SOURce:RFSG:WLAN:STANdard N")
    inst1.write(":SOURce:RFSG:WLAN:IINTerval 0.001")
    inst1.write(":SOURce:RFSG:WLAN:BWIDth BW20")
    inst1.write(":SOURce:RFSG:WLAN:CFRequency 2.442 GHz")
    inst1.write(":SOURce:RFSG:WLAN:POWer -19.00")
    inst1.write(":SOURce:RFSG:WLAN:DRATe MCS7")
    inst1.write(":SOURce:RFSG:WLAN:NOCHains 1")
    inst1.write(":SOURce:RFSG:WLAN:NRATe:PLCPformat MIXed")
    inst1.write(":SOURce:RFSG:WLAN:NRATe:GINTerval LONG")
    inst1.write(":SOURce:RFSG:WLAN:NRATe:FECType BCC")
    inst1.write(":SOURce:RFSG:WLAN:PACKets 5000000")
    
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    inst1.write(":SOURce:RFSG:WLAN:CWAVeform")
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    syserr = inst1.query(":SYST:ERR?")
    log_box.insert(tk.END, ":SYST:ERR? \n" + syserr + '\n')
    log_box.see(tk.END)
    
    #=====[DUT_CONTROL_WIFI_RX]=====
    
    inst1.write(":SOURce:RFSG:WLAN:GENerate ON")
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    state = str(inst.query(":FETCh:RFSA:WLAN:STATe?"))
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:STATe? \n" + state + '\n')
    log_box.see(tk.END)
    
    txpower = inst.query(":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults? \n" + txpower + '\n')
    log_box.see(tk.END)
    
    pramp = inst.query(":FETCh:RFSA:WLAN:MEASurement:PRAMp:RTIMe?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:PRAMp:RTIMe? \n" + pramp + '\n')
    log_box.see(tk.END)
    
    #Average sample clock offset, Average carrier frequency offset, Average RMS phase noise, Average carrier suppression, Average IQ imbalance, Average quadrature skew
    impair = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:IMPairments?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:IMPairments? \n" + impair + '\n')
    log_box.see(tk.END)
    
    #RMS EVM, Peak EVM, 802.11B Peak EVM, 802.11B Peak EVM (2007) dB
    evm = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:EVM?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:EVM? \n" + evm + '\n')
    log_box.see(tk.END)
    
    sem = inst.query(":FETCh:RFSA:WLAN:MEASurement:SEM:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:SEM:RESults? \n" + sem + '\n')
    log_box.see(tk.END)
    
    #=====[DUT_CONTROL_WIFI_RX_Fetch]=====
    
    inst1.write(":SOURce:RFSG:WLAN:GENerate OFF")
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
def rx11ac():
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 5210, 30.00")
    inst1.write(":SOURce:RFSG:WLAN:PAYLoad:TYPE PN9")
    inst1.write(":SOURce:RFSG:WLAN:PAYLoad:MACAddress 0x010000C0FFEE")
    inst1.write(":SOURce:RFSG:WLAN:PAYLoad:LENGth 1024")
    inst1.write(":SOURce:RFSG:WLAN:STANdard AC")
    inst1.write(":SOURce:RFSG:WLAN:IINTerval 0.001")
    inst1.write(":SOURce:RFSG:WLAN:BWIDth BW80")
    inst1.write(":SOURce:RFSG:WLAN:CFRequency 5.210 GHz")
    inst1.write(":SOURce:RFSG:WLAN:POWer -37.00")
    inst1.write(":SOURce:RFSG:WLAN:DRATe MCS9NSS1")
    inst1.write(":SOURce:RFSG:WLAN:NOCHains 1")
    inst1.write(":SOURce:RFSG:WLAN:PACKets 5000000")
    
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    inst1.write(":SOURce:RFSG:WLAN:CWAVeform")
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    syserr = inst1.query(":SYST:ERR?")
    log_box.insert(tk.END, ":SYST:ERR? \n" + syserr + '\n')
    log_box.see(tk.END)
    
    #=====[DUT_CONTROL_WIFI_RX]=====
    
    inst1.write(":SOURce:RFSG:WLAN:GENerate ON")
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
    state = str(inst.query(":FETCh:RFSA:WLAN:STATe?"))
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:STATe? \n" + state + '\n')
    log_box.see(tk.END)
    
    txpower = inst.query(":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults? \n" + txpower + '\n')
    log_box.see(tk.END)
    
    pramp = inst.query(":FETCh:RFSA:WLAN:MEASurement:PRAMp:RTIMe?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:PRAMp:RTIMe? \n" + pramp + '\n')
    log_box.see(tk.END)
    
    #Average sample clock offset, Average carrier frequency offset, Average RMS phase noise, Average carrier suppression, Average IQ imbalance, Average quadrature skew
    impair = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:IMPairments?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:IMPairments? \n" + impair + '\n')
    log_box.see(tk.END)
    
    #RMS EVM, Peak EVM, 802.11B Peak EVM, 802.11B Peak EVM (2007) dB
    evm = inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:EVM?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:EVM? \n" + evm + '\n')
    log_box.see(tk.END)
    
    sem = inst.query(":FETCh:RFSA:WLAN:MEASurement:SEM:RESults?")
    log_box.insert(tk.END, ":FETCh:RFSA:WLAN:MEASurement:SEM:RESults? \n" + sem + '\n')
    log_box.see(tk.END)
    
    #=====[DUT_CONTROL_WIFI_RX_Fetch]=====
    inst.write(":SOURce:RFSG:WLAN:GENerate OFF")
    opc = inst.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    
def CW_TX():
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00")
    inst1.write(":CONFigure:RFSA:GPRF:FREQuency 2405000000")
    inst1.write(":CONFigure:RFSA:GPRF:POWer 13.00")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:RBWidth 20000000")
    inst1.write(":CONFigure:RFSA:GPRF:TXPower:INTerval 1")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DELay 0")
    inst1.write(":CONFigure:RFSA:GPRF:SLOT:DURation 0.01")
    inst1.write("TRIGger:RFSA:GPRF:EDGE RISING")
    inst1.write("TRIGger:RFSA:GPRF:SOUR SOURCE_LM")
    inst1.write("TRIGger:RFSA:GPRF:THREshold -40.00")
    inst1.write("TRIGger:RFSA:GPRF:SOUR SOURCE_LM")
    inst1.write(":INITiate:RFSA:GPRF:POWer")
    
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    fetch = inst.query("FETCh:RFSA:GPRF:POWer?")
    log_box.insert(tk.END, "FETCh:RFSA:GPRF:POWer? \n" + fetch + '\n')
    log_box.see(tk.END)
    
def CW_RX():
    inst1.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2405, 2.00")
    inst1.write("SOURce:RFSG:GPRF:LIST:WAVeform CW")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:FREQuency 2405E6")
    inst1.write("SOURce:RFSG:GPRF:ARB:IDLEtime 5")
    inst1.write("SOURce:RFSG:GPRF:ARB:REPetition 1")
    inst1.write("SOURce:RFSG:GPRF:RFSettings:LEVel -30.00")
    inst1.write("SOURce:RFSG:GPRF:ARB:CYCLes 1000")
    inst1.write("SOURce:RFSG:GPRF:STATe ON")
    
    opc = inst1.query("*OPC?")
    log_box.insert(tk.END, "*OPC? \n" + opc + " \n")
    log_box.see(tk.END)
    fetch = inst.query(":SOURce:RFSG:GPRF:STATUS?")
    log_box.insert(tk.END, ":SOURce:RFSG:GPRF:STATUS? \n" + fetch + '\n')
    log_box.see(tk.END)
    
    

measurement = tk.LabelFrame(entry, text='Measurement')
measurement.grid(column=0,row=1)

b_tx_button = ttk.Button(measurement, text='11b SA Setting', width = 30, command=sa11b)
b_tx_button.grid(column=0, row=1, pady= 10)
b_rx_button = ttk.Button(measurement, text='11b Rx Per Measurement', width = 30, command=rx11b)
b_rx_button.grid(column=1, row=1)

ag_tx_button = ttk.Button(measurement, text='11ag SA Setting', width = 30, command=sa11g)
ag_tx_button.grid(column=0, row=2, pady= 10)
ag_rx_button = ttk.Button(measurement, text='11ag Rx Per Measurement', width = 30, command=rx11g)
ag_rx_button.grid(column=1, row=2)

n_tx_button = ttk.Button(measurement, text='11n SA Setting', width = 30, command=sa11n)
n_tx_button.grid(column=0, row=3, pady= 10)
n_rx_button = ttk.Button(measurement, text='11n Rx Per Measurement', width = 30, command=rx11n)
n_rx_button.grid(column=1, row=3)

ac_tx_button = ttk.Button(measurement, text='11ac SA Setting', width = 30, command=sa11ac)
ac_tx_button.grid(column=0, row=4, pady= 10)
ac_rx_button = ttk.Button(measurement, text='11ac Rx Per Measurement', width = 30, command=rx11ac)
ac_rx_button.grid(column=1, row=4)

ax_tx_button = ttk.Button(measurement, text='11ax SA Setting', width = 30)
ax_tx_button.grid(column=0, row=5, pady= 10)
ax_rx_button = ttk.Button(measurement, text='11ax Rx Per Measurement', width = 30)
ax_rx_button.grid(column=1, row=5)

#CW

cw_rx_button = ttk.Button(measurement, text='CW Tx Genereation', width = 30, command = CW_TX)
cw_rx_button.grid(column=0, row=6, pady= 10)

cw_rx_button = ttk.Button(measurement, text='CW Rx Genereation', width = 30, command = CW_RX)
cw_rx_button.grid(column=1, row=6, pady= 10)

#Log

def clear():
    log_box.delete(1.0, tk.END)

log = ttk.LabelFrame(win, text='Log')
log.grid(column=1, row=0)

log_box = scrolledtext.ScrolledText(log)

log_box.grid(column=0,row=0)

clear_button = tk.Button(log, text= 'CLEAR', width= 10, command=clear)
clear_button.grid(column=0, row=2)

win.mainloop()