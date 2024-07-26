using CellularTM.JPMIC.Definition;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using static CellularTM.JPMIC.Conf.Conf.ResultSetting;
using Excel = Microsoft.Office.Interop.Excel;

namespace CellularTM.JPMIC.ExcelWrapper
{
    public class ExcelWrapper
    {
        protected Excel.Application ExcelApp;
        protected Excel.Workbook ExcelWorkbook;
        protected Excel._Worksheet CurrWhorkSheet;
        string CurretSheetName { get; set; }

        bool AutoCloseExcel = false;
        public string SaveTargetFolder { get; set; }
        public string TargetFileName { get; set; }
        public bool IsOpened { get; set; } //Report에만 해당되는  Flag

        public ExcelWrapper()
        {
            ExcelApp = null;
        }

        public bool MakeNewFile()
        {
            try
            {
                object misValue = System.Reflection.Missing.Value;
                ExcelApp = new Excel.Application();
                ExcelWorkbook = ExcelApp.Workbooks.Add(misValue);
                CurrWhorkSheet = (Excel.Worksheet)ExcelWorkbook.Worksheets.get_Item(1);
            }
            catch (Exception ex)
            {
                ExtendedLog(LogType.Error, ex.Message);
                Log(LogType.Debug, ex.ToString());
                return false;
            }

            return true;
        }

        int UsedLine = 0;
        public bool OpenExcel(string filePath, bool readOnly)
        {
            try
            {
                Log("Open Excel Worksheet");
                Log(filePath);
                ExcelApp = new Excel.Application();
                Object Opt = Missing.Value;
                ExcelWorkbook = ExcelApp.Workbooks.Open(filePath, Opt, readOnly);

                CurrWhorkSheet = (Excel.Worksheet)ExcelWorkbook.Worksheets.get_Item(1);

                CurretSheetName = CurrWhorkSheet.Name;
                UsedLine = CurrWhorkSheet.UsedRange.Rows.Count;

                return true;
            }
            catch (Exception ex)
            {
                ExtendedLog(LogType.Error, ex.Message);
                Log(LogType.Debug, ex.ToString());

                //CurretSheetName
                //MessageBox.Show(ex.Message, "", MessageBoxButton.OK, MessageBoxImage.Exclamation);//, MessageBoxBut.OK, BkMessageBox.MessageBoxImage.Error);
                //Log(Conf.LogType.Error, "ErrorCatch[[[[" + ex.ToString() + "]]]]] in " + MethodBase.GetCurrentMethod().Name);
                return false;
            }
        }
#if false
        public bool OpenExcel(LteExcelParam lteExcelParam)//  string filePath)
        {
            SaveTargetFolder = lteExcelParam.ResultFolder;
            TargetFileName = lteExcelParam.ResExcelFileName + ".xlsx";//20220614"TestResult.xlsx";
            string srcExcelfile = string.Empty;
            bool fileExist = false;


            DirectoryInfo di = new DirectoryInfo(SaveTargetFolder);
            if (di.Exists == false)
            {
                di.Create();
            }
            foreach (FileInfo File in di.GetFiles())
            {
                if (File.Extension.ToLower().CompareTo(".xlsx") == 0)
                {
                    fileExist = true;
                    TargetFileName = File.Name;
                    Log(LogType.Debug, $"Found File :{TargetFileName}");
                    break;
                }
            }

            srcExcelfile = fileExist ? $"{SaveTargetFolder}\\{TargetFileName}" : lteExcelParam.TemplatePath;
            try
            {
                Log("Open Excel Worksheet");
                Log(LogType.Info, srcExcelfile);//  filePath);
                ExcelApp = new Excel.Application();
                ExcelWorkbook = ExcelApp.Workbooks.Open(srcExcelfile);

                ExcelApp.Visible = true;
                ExcelApp.DisplayAlerts = false; //SaveAs시 덮어쓰기 메시지박스 삭제
                CurretSheetName = string.Empty;

                string savePath = $"{SaveTargetFolder}\\{TargetFileName}";
                Log($"Save Result File : {savePath}");
                ExcelWorkbook.SaveAs(savePath);

                return true;
            }
            catch (Exception ex)
            {
                ExtendedLog(LogType.Error, ex.Message);
                Log(LogType.Debug, ex.ToString());

                BkMessageBox.ShowDialog(ex.Message, BkMessageBox.MessageBoxButtonType.OK, BkMessageBox.MessageBoxImage.Error);
                //Log(Conf.LogType.Error, "ErrorCatch[[[[" + ex.ToString() + "]]]]] in " + MethodBase.GetCurrentMethod().Name);
                return false;
            }
        }
#endif
        public void SetParam(bool autoClose)
        {
            AutoCloseExcel = autoClose;
        }
        public void SaveExcel(string flowFilePath)
        {
            CurretSheetName = string.Empty;
            try
            {
                if (ExcelWorkbook == null)
                {
                    Log("Excel worksheet is Null");
                    return;
                }

                DirectoryInfo di = new DirectoryInfo(System.IO.Path.GetDirectoryName(flowFilePath));
                if (di.Exists == false)
                {
                    di.Create();
                }
                Log("Save File :" + flowFilePath);
                ExcelWorkbook.SaveAs(flowFilePath);
            }
            catch (Exception ex)
            {
                //BkMessageBox.ShowDialog(ex.Message, BkMessageBox.MessageBoxButtonType.OK, BkMessageBox.MessageBoxImage.Error);
                //MessageBox.Show(ex.Message, "ERROR", MessageBoxButton.OK, MessageBoxImage.Error);
                Log(LogType.Debug, ex.ToString());
                ExtendedLog(LogType.Error, ex.Message);
            }

            return;
        }
        public void CloseExcel()//string strNewName)
        {
            CurretSheetName = string.Empty;
            try
            {
                Log("Excel Close");
                ExcelWorkbook.Close(false);// misValue, misValue);
                ExcelWorkbook = null;
                //ExcelWorkbook.Close();
                Log("ExclApp Close");
                ExcelApp.Quit();
                ExcelApp = null;

                Log("Guarbage Collection Perform");
                GC.Collect();
                GC.WaitForPendingFinalizers();
            }
            catch (Exception ex)
            {
                //BkMessageBox.ShowDialog(ex.Message, BkMessageBox.MessageBoxButtonType.OK, BkMessageBox.MessageBoxImage.Error);
                //System.Windows.MessageBox.Show(ex.Message, "ERROR", MessageBoxButton.OK, MessageBoxImage.Error);
                Log(LogType.Debug, ex.ToString());
                ExtendedLog(LogType.Error, ex.Message);
            }

            return;
        }
        
        public bool FindWorkSheet(string sheetName)
        {
            int usedLined = 0;
            return FindWorkSheet( sheetName, ref  usedLined);
        }
        public bool FindWorkSheet(string sheetName, ref int usedLined)
        {
            if (CurretSheetName.Equals(sheetName))
            {
                usedLined = UsedLine;
                return true;
            }

            try
            {
                bool searched = false;
                //CurrWhorkSheet = (Excel.Worksheet)ExcelWorkbook.Sheets[sheetName];
                foreach (Excel.Worksheet sheet in ExcelWorkbook.Sheets)
                {
                    Log(LogType.Debug, "[Sheet Name : " + sheet.Name + "]");

                    if (sheet.Name.Equals(sheetName))
                    {
                        CurrWhorkSheet = sheet;
                        CurretSheetName = sheetName;
                        searched = true; 
                        usedLined = UsedLine = CurrWhorkSheet.UsedRange.Rows.Count;
                        break;
                    }
                }
                if (!searched)
                {
                    usedLined = UsedLine= -1;
                    //함수밖에서 메시지 처리
                    //string msg = string.Format("[sheetName] Workhseet가 Template Excel에 존재하지 않습니다.", sheetName);
                    //BkMessageBox.ShowDialog(msg, BkMessageBox.MessageBoxButtonType.OK, BkMessageBox.MessageBoxImage.Error);
                    return false;
                }
            }
            catch (Exception ex)
            {
                Log(LogType.Debug, ex.ToString());
                ExtendedLog(LogType.Error, ex.Message);

                return false;
            }
            Log(LogType.Debug, "[Searching Sheet Name : " + sheetName + "]");
            Log(LogType.Debug, "[Searched Sheet Name : " + CurrWhorkSheet.Name + "]");
            return true;
        }

        void SetValue(Excel._Worksheet sheet, string cell, string value)
        {
            sheet.Range[cell/*"E2"*/].Value = value;
        }
        public void SetValue(string cell, string value)
        {
            try
            {
                CurrWhorkSheet.Range[cell/*"E2"*/].Value = value;
            }
            catch (Exception e)
            {
                ExtendedLog(LogType.Error, e.Message);
            }
        }
        public void GetValue(string cell, ref string value)
        {
            try
            {
                Excel.Range range = CurrWhorkSheet.Range[cell/*"E2"*/];
                if (range.Value2 == null)
                {
                    value = string.Empty;
                }
                else if (typeof(double) == range.Value2.GetType())
                {
                    value = ((double)range.Value).ToString();
                }
                else if (typeof(bool) == range.Value2.GetType())
                {
                    value = ((bool)range.Value).ToString();
                }
                else if (typeof(int) == range.Value2.GetType())
                {
                    value = ((int)range.Value).ToString();
                }
                else
                    value = range.Value;
            }
            catch (Exception e)
            {
                ExtendedLog(LogType.Error, e.Message);
            }
            //Log($"[{value}]");
        }
        public int ReadInt(string Cell)
        {
            string value = "";
            GetValue(Cell, ref  value);

           return (string.IsNullOrEmpty(value)) ? 0 : Convert.ToInt32(value);
        }
        public double ReadDoble(string Cell)
        {
            string value = "";
            GetValue(Cell, ref value);

            return (string.IsNullOrEmpty(value)) ? 0 : Convert.ToDouble(value);
        }

        public void ReadExcelData(ref List<string[]> Data, int numOfColumn)
        {
            // 현재 Worksheet에서 사용된 Range 전체를 선택
            Excel.Range rng = CurrWhorkSheet.UsedRange;

            // Range 데이타를 배열 (1-based array)로
            object[,] data = (object[,])rng.Value;

            for (int r = 1; r <= data.GetLength(0); r++)
            {
                int length = Math.Min(data.GetLength(1), numOfColumn);
                string[] arr = new string[length];

                for (int c = 1; c <= length; c++)
                {
                    if (data[r, c] == null)
                    {

                        arr[c - 1] = string.Empty;
                        //continue;
                    }
                    else if (data[r, c] is string)
                    {
                        arr[c - 1] = data[r, c] as string;
                    }
                    else
                    {
                        arr[c - 1] = data[r, c].ToString();
                    }
                }

#if true //20240627
                Data.Add(arr);
#else
                for (int i = 0; i < arr.Length; i++)
                {
                    //if (string.IsNullOrWhiteSpace(arr[i]) == false)
                    {
                        Data.Add(arr);
                        break;
                    }
                }
#endif

            }

        }

        #region LOG
        public void Log(string msg)
        {
         //   mainWnd.Log(LogType.Debug, "[EXCEL] " + msg);
        }
        public void Log(LogType type, string msg)
        {
         //   mainWnd.Log(type, "[EXCEL] " + msg);
        }
        private void ExtendedLog(LogType type, string logText,
                        [CallerFilePath] string file = "",
                        [CallerMemberName] string member = "",
                        [CallerLineNumber] int line = 0)
        {

            Log(type, $"[{System.IO.Path.GetFileName(file)}] [{member}({line})]: {logText}");
        }
        #endregion

    }
}
