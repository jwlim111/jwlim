#!/usr/bin/python

import pyvisa as visa
from time import sleep

rm = visa.ResourceManager()
inst = rm.open_resource('TCPIP0::192.168.100.252::inst0::INSTR',  
    write_termination = '\n', read_termination='\n')

def Init():
    # TX  INIT
    inst.write(":TRIGger:RFSA:WLAN:TOUT 2")
    inst.write(":TRIGger:RFSA:WLAN:THReshold -22.0000")
    inst.write(":TRIGger:RFSA:WLAN:DELay 0.0 ms")
    
    inst.write(":CONFigure:RFSA:WLAN:POWer:AUTO OFF")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:TXPower:AVERaging 1")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:SEM:AVERaging 1")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:AVERaging 1")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp:AVERages 1")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:TXPower ON")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:SEM ON")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation ON")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:GPOW OFF")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp OFF")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:HDETection ON")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:EQUalization OFF")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:TRACking:PHASe STANdard")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter RCOSine")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:DSSS:PSFilter:COEFficient 0.5")
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:AMPLitude OFF")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:PHASe STANdard")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:TIME ON")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:TRACking:CHANnel ON")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:MSYMbols 16")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:CFOMethod PDATa")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP ON")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLCP:FFORmat GREenfield")
    
    inst.query("*OPC?")
    while True:
        result = str(inst.query(":SYST:ERR?")).split(',')
        if result[0] == '0' : break
    return result[0]
    
    
    
    
def wifi11b():
    
    # ==TX[11B_11M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====
    
    #Tx Config
    
    inst.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2442, 9.00")
    inst.query(":SYST:ERR?")
    
    inst.write(":CONFigure:RFSA:WLAN:STANdard B")
    inst.write(":CONFigure:RFSA:WLAN:BWIDth BW20")
    inst.write(":CONFigure:RFSA:WLAN:FREquency 2442 MHz")
    inst.write(":CONFigure:RFSA:WLAN:POWer 21.00")                      # 측정 power + 3(11b, bluetooth)
    
    inst.write(":CONFigure:RFSA:WLAN:ALENgth 1.50 ms")                  # ramp on / off 를 측정하기 위해서는 전체 한 packet 을 캡쳐해야 함
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:PRAMp ON")             # ramp on / off를 측정할 때만 ON, 아닌 경우 OFF
    
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:CFResponse OFF")
    inst.write(":CONFigure:RFSA:WLAN:MEASurement:MODulation:OFDM:HDETection:PLENgth 1024")
    
    inst.query("*OPC?")
    
    # Tx capture
    
    inst.write(":INITiate:RFSA:WLAN")
    inst.query("*OPC?")
    
    inst.query(":FETCh:RFSA:WLAN:STATe?")
    
    inst.query(":SYST:ERR?")
    
    # Tx stop
    # Fetch
    
    # /* transmitPower,PeakPower,TransmitPowerWGap*/
    print(inst.query(":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults?"))
    
    print(inst.query(":FETCh:RFSA:WLAN:MEASurement:PRAMp:RTIMe?"))
    
    #Average sample clock offset, Average carrier frequency offset, Average RMS phase noise, Average carrier suppression, Average IQ imbalance, Average quadrature skew
    inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:IMPairments?")
    
    #RMS EVM, Peak EVM, 802.11B Peak EVM, 802.11B Peak EVM (2007) dB
    print(inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:DSSS:EVM?"))
    
    print(inst.query(":FETCh:RFSA:WLAN:MEASurement:SEM:RESults?"))
    return print('11b ok')

def wifi11g():
    # ==TX[11G_54M_2442MHz(CH:7)_Ant1]==

    # =====[DUT_CONTROL_WIFI_TX]=====


    #  config 
    inst.write(":CONFigure:ATTenuation:LOSS:EXTernal 0, 2442, 9.00")
    inst.query(":SYST:ERR?")
    
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
    
    inst.query("*OPC?")
    
    # capture
    
    inst.write(":INITiate:RFSA:WLAN")
    print(inst.query("*OPC?"))
    
    while True :
        state = str(inst.query(":FETCh:RFSA:WLAN:STATe?"))
        off = str('OFF\r')
        print(off)
        if state == off: break
    
    
    inst.query(":SYST:ERR?")
    
    # =====[DUT_CONTROL_WIFI_TX_STOP]=====

    # // fetch


    # /* transmitPower,PeakPower,TransmitPowerWGap*/
    
    inst.query(":FETCh:RFSA:WLAN:MEASurement:TXPower:RESults?")
    
    #/*	Average sample clock offset, (ppm)
	# Average carrier frequency offset, (Hz)
	# Average RMS common pilot error, 
	# Average carrier frequency leakage, 
	# Average IQ imbalance, 
	# Average quadrature skew, 
	# Average timing skew
    # */
    
    inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:IMPairments?")
    
    # /*RMS EVM, Max EVM, Data EVM, Pilot EVM*/
    
    inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:EVM?")
    
    # /*Average spectral flatness margin, Smallest spectral flatness margin, Index of smallest spectral flatness margin*/
    
    inst.query(":FETCh:RFSA:WLAN:MEASurement:MODulation:OFDM:SFMargin?")
    
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
    
    return result