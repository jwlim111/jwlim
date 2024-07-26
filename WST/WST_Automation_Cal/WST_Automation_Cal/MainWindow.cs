using System;
using System.Collections.Generic;
using System.IO;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Sockets;
using System.Runtime.Remoting.Channels;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using BkSocket;
using NationalInstruments.Visa;
using Ivi.Visa;

namespace WST_Automation_Cal
{
    public partial class MainWindow : Form
    {
        const int WST100APORT = 20245;
        const int ALIVECHECKPORT = 20247;
        BkTcpSocket socket = new BkTcpSocket();
        BkTcpSocket aliveSocket = new BkTcpSocket();
        ResourceManager rm = new ResourceManager();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            ConnectoWstServer();
            rm.Open("USB0::0x2A8D::0x2A18::MY61140006::INSTR");
        }
        private void btnMeasure5G_Click(object sender, EventArgs e)
        {
            Measure5GWifiTx();
        }

        private void btnMeasure24G_Click(object sender, EventArgs e)
        {
            Measure24GWifiTx();
        }

        void Measure24GWifiTx()
        {
            string band = "B";
            string[] proto = { "B", "G", "N" };
            int[] bw = { 20 };
            int[] chan_24g = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 };
            int[] pwr = {0, 5, 10, 15, 20, 25};
            string[] modulation_ofdm = { "1M", "2M", "5.5M", "11M" };
            string[] modulation_dsss = { "6M", "9M", "12M", "18M", "24M", "36M", "48M", "54M" };
            string[] modulation_mcs = { "M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9" };

            int protoCnt = proto.GetLength(0);
            int bwCnt = bw.GetLength(0);
            int chan24gCnt = chan_24g.GetLength(0);
            int pwrCnt = pwr.GetLength(0);
            int modofdmCnt = modulation_ofdm.GetLength(0);
            int modmcsCnt = modulation_mcs.GetLength(0);

            //band
            string recved;
            string error = "";
            string cmd = "";
            int ret = 0;

            //band
            cmd = $"CONF:WLAN:BAND {band}";
            ret = socket.SendString(cmd, ref error);
            recved = socket.ReceiveString(ref error);

            for (int i = 0; i < bwCnt; i++)
            {
                cmd = $"CONF:WLAN:BW {bw[i]}";
                ret = socket.SendString(cmd, ref error);
                recved = socket.ReceiveString(ref error);
                // protocol 
                for (int j = 0; j < protoCnt; j++)
                {
                    if (proto[j] == "B")
                    {
                        cmd = $"CONF:WLAN:PROT {proto[j]}";
                        ret = socket.SendString(cmd, ref error);
                        recved = socket.ReceiveString(ref error);

                        //channel
                        for (int k = 0; k < chan24gCnt; k++)
                        {
                            cmd = $"CONF:WLAN:CHAN {chan_24g[k]}";
                            ret = socket.SendString(cmd, ref error);
                            recved = socket.ReceiveString(ref error);

                            //power
                            for (int l = 0; l < pwrCnt; l++)
                            {
                                cmd = $"CONF:WLAN:POW {pwr[l]}";
                                ret = socket.SendString(cmd, ref error);
                                recved = socket.ReceiveString(ref error);

                                //modulation
                                for (int m = 0; m < modofdmCnt; m++)
                                {
                                    cmd = $"CONF:WLAN:MOD {modulation_ofdm[m]}";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    cmd = $"INIT:WLAN:TX ON";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    Thread.Sleep(200);

                                    cmd = $"INIT:WLAN:TX OFF";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);
                                }
                            }
                        }
                    }
                    else if (proto[j] == "G")
                    {
                        cmd = $"CONF:WLAN:PROT {proto[j]}";
                        ret = socket.SendString(cmd, ref error);
                        recved = socket.ReceiveString(ref error);

                        //channel
                        for (int k = 0; k < chan24gCnt; k++)
                        {
                            cmd = $"CONF:WLAN:CHAN {chan_24g[k]}";
                            ret = socket.SendString(cmd, ref error);
                            recved = socket.ReceiveString(ref error);

                            //power
                            for (int l = 0; l < pwrCnt; l++)
                            {
                                cmd = $"CONF:WLAN:POW {pwr[l]}";
                                ret = socket.SendString(cmd, ref error);
                                recved = socket.ReceiveString(ref error);

                                //modulation
                                for (int m = 0; m < modofdmCnt; m++)
                                {
                                    cmd = $"CONF:WLAN:MOD {modulation_dsss[m]}";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    cmd = $"INIT:WLAN:TX ON";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    Thread.Sleep(200);

                                    cmd = $"INIT:WLAN:TX OFF";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);
                                }
                            }
                        }
                    }
                    else 
                    {
                        cmd = $"CONF:WLAN:PROT {proto[j]}";
                        ret = socket.SendString(cmd, ref error);
                        recved = socket.ReceiveString(ref error);

                        //channel
                        for (int k = 0; k < chan24gCnt; k++)
                        {
                            cmd = $"CONF:WLAN:CHAN {chan_24g[k]}";
                            ret = socket.SendString(cmd, ref error);
                            recved = socket.ReceiveString(ref error);

                            //power
                            for (int l = 0; l < pwrCnt; l++)
                            {
                                cmd = $"CONF:WLAN:POW {pwr[l]}";
                                ret = socket.SendString(cmd, ref error);
                                recved = socket.ReceiveString(ref error);

                                //modulation
                                for (int m = 0; m < modofdmCnt; m++)
                                {
                                    cmd = $"CONF:WLAN:MOD {modulation_mcs[m]}";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    cmd = $"INIT:WLAN:TX ON";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    Thread.Sleep(200);

                                    cmd = $"INIT:WLAN:TX OFF";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);
                                }
                            }
                        }
                    }
                }
            }
        }

        void Measure5GWifiTx()
        {
            string band = "a";
            string[] proto = { "A", "N", "AC" };
            string[] bw = { "20", "40", "80" };
            int[] chan_5g_20M = { 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 149, 153, 157, 161, 165 };
            int[] chan_5g_40M = { 36, 44, 52, 60, 100, 108, 116, 124, 132, 149, 157 };
            int[] chan_5g_80M = { 36, 52, 100, 116, 149};
            int[] pwr = { 0, 5, 10, 15, 20, 25 };
            string[] modulation_dsss = { "6M", "9M", "12M", "18M", "24M", "36M", "48M", "54M" };
            string[] modulation_mcs = { "M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8" };

            int protoCnt = proto.GetLength(0);
            int bwCnt = bw.GetLength(0);
            int chan5g20MCnt = chan_5g_20M.GetLength(0);
            int chan5g40MCnt = chan_5g_40M.GetLength(0);
            int chan5g80MCnt = chan_5g_80M.GetLength(0);
            int pwrCnt = pwr.GetLength(0);
            int moddsssCnt = modulation_dsss.GetLength(0);
            int modmcsCnt = modulation_mcs.GetLength(0);

            //band
            string recved;
            string cmd = "";
            string error = "";
            int ret = 0;

            //band
            cmd = $"CONF:WLAN:BAND {band}";
            ret = socket.SendString(cmd, ref error);
            recved = socket.ReceiveString(ref error);

            for (int i = 0; i < bwCnt; i++)
            {
                if (bw[i] == "20")
                {
                    MessageBox.Show(bw[i]);
                    cmd = $"CONF:WLAN:BW {bw[i]}";
                    ret = socket.SendString(cmd, ref error);
                    recved = socket.ReceiveString(ref error);

                
                    // protocol 
                    for (int j = 0; j < protoCnt; j++)
                    {
                        if (proto[j] == "A")
                        {
                            cmd = $"CONF:WLAN:PROT {proto[j]}";
                            ret = socket.SendString(cmd, ref error);
                            recved = socket.ReceiveString(ref error);

                            //channel
                            for (int k = 0; k < chan5g20MCnt; k++)
                            {
                                cmd = $"CONF:WLAN:CHAN {chan_5g_20M[k]}";
                                ret = socket.SendString(cmd, ref error);
                                recved = socket.ReceiveString(ref error);

                                //power
                                for (int l = 0; l < pwrCnt; l++)
                                {
                                    cmd = $"CONF:WLAN:POW {pwr[l]}";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    //modulation
                                    for (int m = 0; m < moddsssCnt; m++)
                                    {
                                        cmd = $"CONF:WLAN:MOD {modulation_dsss[m]}";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        cmd = $"INIT:WLAN:TX ON";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        Thread.Sleep(500);

                                        cmd = $"INIT:WLAN:TX OFF";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);
                                    }
                                }
                            }
                        }
                        if (proto[j] == "N")
                        {
                            cmd = $"CONF:WLAN:PROT {proto[j]}";
                            ret = socket.SendString(cmd, ref error);
                            recved = socket.ReceiveString(ref error);

                            //channel
                            for (int k = 0; k < chan5g20MCnt; k++)
                            {
                                cmd = $"CONF:WLAN:CHAN {chan_5g_20M[k]}";
                                ret = socket.SendString(cmd, ref error);
                                recved = socket.ReceiveString(ref error);

                                //power
                                for (int l = 0; l < pwrCnt; l++)
                                {
                                    cmd = $"CONF:WLAN:POW {pwr[l]}";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    //modulation
                                    for (int m = 0; m < modmcsCnt; m++)
                                    {
                                        cmd = $"CONF:WLAN:MOD {modulation_mcs[m]}";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        cmd = $"INIT:WLAN:TX ON";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        Thread.Sleep(200);

                                        cmd = $"INIT:WLAN:TX OFF";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);
                                    }
                                }
                            }
                        }
                        if (proto[j] == "AC")
                        {
                            cmd = $"CONF:WLAN:PROT {proto[j]}";
                            ret = socket.SendString(cmd, ref error);
                            recved = socket.ReceiveString(ref error);

                            //channel
                            for (int k = 0; k < chan5g20MCnt; k++)
                            {
                                cmd = $"CONF:WLAN:CHAN {chan_5g_20M[k]}";
                                ret = socket.SendString(cmd, ref error);
                                recved = socket.ReceiveString(ref error);

                                //power
                                for (int l = 0; l < pwrCnt; l++)
                                {
                                    cmd = $"CONF:WLAN:POW {pwr[l]}";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    //modulation
                                    for (int m = 0; m < modmcsCnt; m++)
                                    {
                                        cmd = $"CONF:WLAN:MOD {modulation_mcs[m]}";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        cmd = $"INIT:WLAN:TX ON";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        Thread.Sleep(200);

                                        cmd = $"INIT:WLAN:TX OFF";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);
                                    }
                                }
                            }
                        }
                    }
                    MessageBox.Show(bw[i] + "끝");
                }
                else if (bw[i] == "40")
                {
                    MessageBox.Show(bw[i]);
                    cmd = $"CONF:WLAN:BW {bw[i]}";
                    ret = socket.SendString(cmd, ref error);
                    recved = socket.ReceiveString(ref error);

                    for (int j = 0; j < protoCnt; j++)
                    {
                        if (proto[j] == "N")
                        {
                            cmd = $"CONF:WLAN:PROT {proto[j]}";
                            ret = socket.SendString(cmd, ref error);
                            recved = socket.ReceiveString(ref error);

                            //channel
                            for (int k = 0; k < chan5g40MCnt; k++)
                            {
                                cmd = $"CONF:WLAN:CHAN {chan_5g_40M[k]}";
                                ret = socket.SendString(cmd, ref error);
                                recved = socket.ReceiveString(ref error);

                                //power
                                for (int l = 0; l < pwrCnt; l++)
                                {
                                    cmd = $"CONF:WLAN:POW {pwr[l]}";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    //modulation
                                    for (int m = 0; m < modmcsCnt; m++)
                                    {
                                        cmd = $"CONF:WLAN:MOD {modulation_mcs[m]}";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        cmd = $"INIT:WLAN:TX ON";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        Thread.Sleep(200);

                                        cmd = $"INIT:WLAN:TX OFF";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);
                                    }
                                }
                            }
                        }
                        if (proto[j] =="AC")
                        {
                            cmd = $"CONF:WLAN:PROT {proto[j]}";
                            ret = socket.SendString(cmd, ref error);
                            recved = socket.ReceiveString(ref error);

                            //channel
                            for (int k = 0; k < chan5g40MCnt; k++)
                            {
                                cmd = $"CONF:WLAN:CHAN {chan_5g_40M[k]}";
                                ret = socket.SendString(cmd, ref error);
                                recved = socket.ReceiveString(ref error);

                                //power
                                for (int l = 0; l < pwrCnt; l++)
                                {
                                    cmd = $"CONF:WLAN:POW {pwr[l]}";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    //modulation
                                    for (int m = 0; m < modmcsCnt; m++)
                                    {
                                        cmd = $"CONF:WLAN:MOD {modulation_mcs[m]}";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        cmd = $"INIT:WLAN:TX ON";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        Thread.Sleep(200);

                                        cmd = $"INIT:WLAN:TX OFF";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);
                                    }
                                }
                            }
                        }
                    }
                    MessageBox.Show(bw[i] + "끝");
                }
                else
                {
                    MessageBox.Show(bw[i]);
                    cmd = $"CONF:WLAN:BW {bw[i]}";
                    ret = socket.SendString(cmd, ref error);
                    recved = socket.ReceiveString(ref error);

                    for (int j = 0; j < protoCnt; j++)
                    {
                        if(proto[j] == "AC")
                        {
                            cmd = $"CONF:WLAN:PROT {proto[j]}";
                            ret = socket.SendString(cmd, ref error);
                            recved = socket.ReceiveString(ref error);

                            //channel
                            for (int k = 0; k < chan5g80MCnt; k++)
                            {
                                cmd = $"CONF:WLAN:CHAN {chan_5g_80M[k]}";
                                ret = socket.SendString(cmd, ref error);
                                recved = socket.ReceiveString(ref error);

                                //power
                                for (int l = 0; l < pwrCnt; l++)
                                {
                                    cmd = $"CONF:WLAN:POW {pwr[l]}";
                                    ret = socket.SendString(cmd, ref error);
                                    recved = socket.ReceiveString(ref error);

                                    //modulation
                                    for (int m = 0; m < modmcsCnt; m++)
                                    {
                                        cmd = $"CONF:WLAN:MOD {modulation_mcs[m]}";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        cmd = $"INIT:WLAN:TX ON";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);

                                        Thread.Sleep(200);

                                        cmd = $"INIT:WLAN:TX OFF";
                                        ret = socket.SendString(cmd, ref error);
                                        recved = socket.ReceiveString(ref error);
                                    }
                                }
                            }
                        }
                    }
                    MessageBox.Show(bw[i] + "끝");
                }
            }
        }

        void ConnectoWstServer()
        {
            string addr = "192.168.100.100";
            int port = WST100APORT;

            //tester.Connect(addr, port);     //"127.0.0.1", 2000);
            socket.Connect(addr, port);
            MessageBox.Show("성공");

        }

        private void textbox_TestLog_TextChanged(object sender, EventArgs e)
        {

        }
    }   
}
