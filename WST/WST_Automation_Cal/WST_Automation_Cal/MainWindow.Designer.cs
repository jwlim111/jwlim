namespace WST_Automation_Cal
{
    partial class MainWindow
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnMeasure24G = new System.Windows.Forms.Button();
            this.btnConnect = new System.Windows.Forms.Button();
            this.btnMeasure5G = new System.Windows.Forms.Button();
            this.btnDisconnect = new System.Windows.Forms.Button();
            this.textbox_TestLog = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // btnMeasure24G
            // 
            this.btnMeasure24G.Location = new System.Drawing.Point(75, 90);
            this.btnMeasure24G.Name = "btnMeasure24G";
            this.btnMeasure24G.Size = new System.Drawing.Size(118, 43);
            this.btnMeasure24G.TabIndex = 0;
            this.btnMeasure24G.Text = "Test";
            this.btnMeasure24G.UseVisualStyleBackColor = true;
            this.btnMeasure24G.Click += new System.EventHandler(this.btnMeasure24G_Click);
            // 
            // btnConnect
            // 
            this.btnConnect.Location = new System.Drawing.Point(283, 97);
            this.btnConnect.Name = "btnConnect";
            this.btnConnect.Size = new System.Drawing.Size(160, 35);
            this.btnConnect.TabIndex = 1;
            this.btnConnect.Text = "Connect";
            this.btnConnect.UseVisualStyleBackColor = true;
            this.btnConnect.Click += new System.EventHandler(this.btnConnect_Click);
            // 
            // btnMeasure5G
            // 
            this.btnMeasure5G.Location = new System.Drawing.Point(74, 169);
            this.btnMeasure5G.Name = "btnMeasure5G";
            this.btnMeasure5G.Size = new System.Drawing.Size(118, 33);
            this.btnMeasure5G.TabIndex = 2;
            this.btnMeasure5G.Text = "5G Test";
            this.btnMeasure5G.UseVisualStyleBackColor = true;
            this.btnMeasure5G.Click += new System.EventHandler(this.btnMeasure5G_Click);
            // 
            // btnDisconnect
            // 
            this.btnDisconnect.Location = new System.Drawing.Point(280, 171);
            this.btnDisconnect.Name = "btnDisconnect";
            this.btnDisconnect.Size = new System.Drawing.Size(162, 30);
            this.btnDisconnect.TabIndex = 3;
            this.btnDisconnect.Text = "Disconnect";
            this.btnDisconnect.UseVisualStyleBackColor = true;
            // 
            // textbox_TestLog
            // 
            this.textbox_TestLog.Location = new System.Drawing.Point(525, 57);
            this.textbox_TestLog.Multiline = true;
            this.textbox_TestLog.Name = "textbox_TestLog";
            this.textbox_TestLog.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.textbox_TestLog.Size = new System.Drawing.Size(306, 221);
            this.textbox_TestLog.TabIndex = 4;
            this.textbox_TestLog.TextChanged += new System.EventHandler(this.textbox_TestLog_TextChanged);
            // 
            // MainWindow
            // 
            this.ClientSize = new System.Drawing.Size(889, 308);
            this.Controls.Add(this.textbox_TestLog);
            this.Controls.Add(this.btnDisconnect);
            this.Controls.Add(this.btnMeasure5G);
            this.Controls.Add(this.btnConnect);
            this.Controls.Add(this.btnMeasure24G);
            this.Name = "MainWindow";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnMeasureStart;
        private System.Windows.Forms.Button btn_Connect;
        private System.Windows.Forms.Button btnMeasure24G;
        private System.Windows.Forms.Button btnConnect;
        private System.Windows.Forms.Button btnMeasure5G;
        private System.Windows.Forms.Button btnDisconnect;
        private System.Windows.Forms.TextBox textbox_TestLog;
    }
}

