using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Threading;
using System.Net;

namespace BkSocket
{
    /// <summary>
    /// BkTcpSocket 의 통신 구조 
    /// 1. 항상 HEADER 를 먼저 전송. 
    /// 2. HEADER 에 맞는 데이터 송수신 처리 
    /// </summary>
    class BkTcpSocket
    {
        Socket socket;
        int MAX_BUFFER=10240;
        //bool IsConnected;

        
        /// <summary>
        /// #server side. 
        /// 접속된 client의 주소를 리턴한다 
        /// </summary>
        /// <param name="clientAddr"></param>
        public void GetClientAddr(ref System.Net.IPEndPoint clientAddr)
        {
            clientAddr = (System.Net.IPEndPoint)socket.RemoteEndPoint;
        }

        public bool IsConnected()
        {
            if (socket == null)
                return false;

            return socket.Connected;
        }

        /// <summary>
        /// #for client side. 
        /// </summary>
        /// <param name="addr"></param>
        /// <param name="port"></param>
        public bool Connect(string addr, int port, int recvTimetout =2000)
        {
            //IP = addr;
            bool ret = false;

            socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.IP);
            socket.ReceiveTimeout = recvTimetout;
            socket.SendTimeout = 2000;
            try
            {
                socket.Connect(addr, port);

                ret = true;
            }
            catch (Exception)
            {
            }

            return ret;
        }

        public void Close()
        {
            socket.Close();
        }

        public int SendString(string msg, ref string error)
        {
            int sentlen = -1;
            byte[] data = Encoding.UTF8.GetBytes(msg);

            try
            {
                sentlen = Send(data, data.Length, ref error);
            }
            catch(Exception e)
            {
                error = e.ToString();
            }

            return sentlen;
        }

        public string ReceiveString(ref string error)
        {
            string recved = "";
            byte[] buffer = new byte[MAX_BUFFER];

            for (int i = 0; i < 10; i++)
            {
                try
                {
                    socket.Receive(buffer, MAX_BUFFER, SocketFlags.None);
                    recved = Encoding.UTF8.GetString(buffer);
                    
                    if (recved != "")
                    {
                        recved = recved.TrimEnd('\0');
                        break;
                    }
                }
                catch (Exception ex)
                {
                    error = ex.Message;
                }

                Thread.Sleep(100);
            }

            return recved;
        }

        public string Receive(ref string error)
        {
            string recved = "";
            byte[] buffer = new byte[MAX_BUFFER];

                try
                {
                    socket.Receive(buffer);
                    recved = Encoding.UTF8.GetString(buffer);

                    if (recved != "")
                    {
                        recved = recved.TrimEnd('\0');
                        //break;
                    }
                }
                catch (Exception ex)
                {
                    error = ex.Message;
                }

            //Thread.Sleep(100);

            return recved;
        }

        // send
        private int Send(byte[] buffer, int nBytes, ref string error)
        {
            int sendBytes = -1;

            if(socket == null)
            {
                error = "need to connect! ";
                return -1;
            }

            try
            {
                sendBytes = socket.Send(buffer, nBytes, SocketFlags.None);
            }
            catch (Exception ex)
            {
                //IsConnected = false;
                socket.Close();
                error = "Send() > " + ex.Message;
            }

            return sendBytes;
        }

        // receive
        private int Receive(byte[] buffer, int length, ref string error)
        {
            int nbytes = -1;

            if (socket == null)
            {
                error = "need to connect! ";
                return -1;
            }

            try
            {
                nbytes = socket.Receive(buffer, length, SocketFlags.None);

            }
            catch (Exception se)
            {
                //IsConnected=false;
                socket.Close();
                error = "Receive() > " + nbytes.ToString() + " bytes received. (" + se.Message + ")";
            }

            return nbytes;
        }



        
    
    }
}
