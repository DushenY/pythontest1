import sys
import socket
import re
import paramiko
from PyQt5.uic.properties import QtCore, QtGui
from PyQt5 import QtCore, QtGui
from paramiko import AuthenticationException
import datetime
from test_test import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox



class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str) #定义一个发送str的信号
    def write(self, text):
      self.textWritten.emit(str(text))

class MyWindow(QWidget, Ui_Dialog):    #使用多继承方法
    def __init__(self):
        super().__init__()
        self.setupUi(self)    # 调用父类的方法
        self.result = set({})
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def outputWritten(self, text):
        cursor = self.showlog.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.showlog.setTextCursor(cursor)
        self.showlog.ensureCursorVisible()


    def Test(self):   #测试连接，测试是否连通
        agent_ip = self.input_agentip.text()
        port = 22
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 判断SSH服务器是否可达
        try:
            if not agent_ip:
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "代理IP为空，请输入")
                msg_box.exec_()
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)  # 设置超时时间为2秒
                result = sock.connect_ex((agent_ip, port))
                if result == 0:
                    print(f'{self.time}--SSH server is reachable')
                else:
                    print(f'{self.time}--SSH server is not reachable')
                    # sys.exit()
        except socket.error as e:
            print('Error: ', e)
            # sys.exit()

    def on_checkBox_shentong_clicked(self):
        if self.ShenTong.isChecked():
            self.result.add("shentong")
        else:
            self.result.remove("shentong")
    def on_checkBox_dm_clicked(self):
        if self.DM.isChecked():
            self.result.add("dm")
        else:
            self.result.remove("dm")
    def on_checkBox_highgo_clicked(self):
        if self.highgo.isChecked():
            self.result.add("highgo")
        else:
            self.result.remove("highgo")
    def on_checkBox_system_clicked(self):
        if self.System.isChecked():
            self.result.add("system")
        else:
            self.result.remove("system")
    def on_checkBox_script_clicked(self):
        if self.Script.isChecked():
            self.result.add("script")
        else:
            self.result.remove("script")
    def on_checkBox_massfile_clicked(self):
        if self.MassFile.isChecked():
            self.result.add("MassFile")
        else:
            self.result.remove("MassFile")
    def on_checkBox_file_clicked(self):
        if self.File.isChecked():
            self.result.add("File")
        else:
            self.result.remove("File")
    def on_checkBox_nas_clicked(self):
        if self.NAS.isChecked():
            self.result.add("NAS")
        else:
            self.result.remove("NAS")
    def on_checkBox_obs_clicked(self):
        if self.OBS.isChecked():
            self.result.add("OBS")
        else:
            self.result.remove("OBS")
    def on_checkBox_oss_clicked(self):
        if self.OSS.isChecked():
            self.result.add("OSS")
        else:
            self.result.remove("OSS")
    def on_checkBox_cos_clicked(self):
        if self.COS.isChecked():
            self.result.add("COS")
        else:
            self.result.remove("COS")
    def on_checkBox_sqlserver_clicked(self):
        if self.SQLServer.isChecked():
            self.result.add("SQLServer")
        else:
            self.result.remove("SQLServer")
    def on_checkBox_mysqllogic_clicked(self):
        if self.MySQLLogical.isChecked():
            self.result.add("MySQLLogical")
        else:
            self.result.remove("MySQLLogical")
    def on_checkBox_kingbasephysical_clicked(self):
        if self.KingbasePhysical.isChecked():
            self.result.add("KingbasePhysical")
        else:
            self.result.remove("KingbasePhysical")
    def on_checkBox_sybase_clicked(self):
        if self.Sybase.isChecked():
            self.result.add("Sybase")
        else:
            self.result.remove("Sybase")
    def on_checkBox_db2_clicked(self):
        if self.DB2.isChecked():
            self.result.add("DB2")
        else:
            self.result.remove("DB2")
    def on_checkBox_oraclephysical_clicked(self):
        if self.OraclePhysical.isChecked():
            self.result.add("OraclePhysical")
        else:
            self.result.remove("OraclePhysical")
    def on_checkBox_uagent_clicked(self):
        if self.UAgent.isChecked():
            self.result.add("UAgent")
        else:
            self.result.remove("UAgent")
    def on_checkBox_ufs_clicked(self):
        if self.UFS.isChecked():
            self.result.add("UFS")
        else:
            self.result.remove("UFS")
    def on_checkBox_volumecbtdriver_clicked(self):
        if self.VolumeCBTDriver.isChecked():
            self.result.add("VolumeCBTDriver")
        else:
            self.result.remove("VolumeCBTDriver")
    def on_checkBox_volumecopy_clicked(self):
        if self.VolumeCopy.isChecked():
            self.result.add("VolumeCopy")
        else:
            self.result.remove("VolumeCopy")
    def on_checkBox_sqlservercdm_clicked(self):
        if self.SQLServerCDM.isChecked():
            self.result.add("SQLServerCDM")
        else:
            self.result.remove("SQLServerCDM")
    def on_checkBox_oraclecdm_clicked(self):
        if self.OracleCDM.isChecked():
            self.result.add("OracleCDM")
        else:
            self.result.remove("OracleCDM")
    def on_checkBox_systemcdm_clicked(self):
        if self.SystemCDM.isChecked():
            self.result.add("SystemCDM")
        else:
            self.result.remove("SystemCDM")
    def on_checkBox_volumecdm_clicked(self):
        if self.VolumeCDM.isChecked():
            self.result.add("VolumeCDM")
        else:
            self.result.remove("VolumeCDM")
    def on_checkBox_cdp_clicked(self):
        if self.CDP.isChecked():
            self.result.add("CDP")
        else:
            self.result.remove("CDP")
    def on_checkBox_kvmdriver_clicked(self):
        if self.KVMDriver.isChecked():
            self.result.add("KVMDriver")
        else:
            self.result.remove("KVMDriver")
    def on_checkBox_esxidriver_clicked(self):
        if self.ESXiDriver.isChecked():
            self.result.add("ESXiDriver")
        else:
            self.result.remove("ESXiDriver")
    def on_checkBox_edr_clicked(self):
        if self.EDR.isChecked():
            self.result.add("EDR")
        else:
            self.result.remove("EDR")
    def on_checkBox_blockcopy_clicked(self):
        if self.BlockCopy.isChecked():
            self.result.add("BlockCopy")
        else:
            self.result.remove("BlockCopy")
    def on_checkBox_vbdinitiator_clicked(self):
        if self.VBDInitiator.isChecked():
            self.result.add("VBDInitiator")
        else:
            self.result.remove("VBDInitiator")
    def on_checkBox_gbase8t_clicked(self):
        if self.Gbase8t.isChecked():
            self.result.add("Gbase8t")
        else:
            self.result.remove("Gbase8t")
    def on_checkBox_informix_clicked(self):
        if self.Informix.isChecked():
            self.result.add("Informix")
        else:
            self.result.remove("Informix")
    def on_checkBox_postgresql_clicked(self):
        if self.PostgreSQL.isChecked():
            self.result.add("PostgreSQL")
        else:
            self.result.remove("PostgreSQL")
    def on_checkBox_mongodb_clicked(self):
        if self.MongoDB.isChecked():
            self.result.add("MongoDB")
        else:
            self.result.remove("MongoDB")
    def on_checkBox_domino_clicked(self):
        if self.Domino.isChecked():
            self.result.add("Domino")
        else:
            self.result.remove("Domino")
    def on_checkBox_gbase8s_clicked(self):
        if self.Gbase8s.isChecked():
            self.result.add("Gbase8s")
        else:
            self.result.remove("Gbase8s")
    def on_checkBox_hadoop_clicked(self):
        if self.Hadoop.isChecked():
            self.result.add("Hadoop")
        else:
            self.result.remove("Hadoop")
    def on_checkBox_kdb_clicked(self):
        if self.KDB.isChecked():
            self.result.add("KDB")
        else:
            self.result.remove("KDB")
    def on_checkBox_tidb_clicked(self):
        if self.TIDB.isChecked():
            self.result.add("TIDB")
        else:
            self.result.remove("TIDB")
    def on_checkBox_goldendb_clicked(self):
        if self.GoldenDB.isChecked():
            self.result.add("GoldenDB")
        else:
            self.result.remove("GoldenDB")
    def on_checkBox_opengauss_clicked(self):
        if self.OpenGauss.isChecked():
            self.result.add("OpenGauss")
        else:
            self.result.remove("OpenGauss")
    def on_checkBox_gaussdb_dws_clicked(self):
        if self.Gaussdb_DWS.isChecked():
            self.result.add("Gaussdb_DWS")
        else:
            self.result.remove("Gaussdb_DWS")
    def on_checkBox_kingbaselogical_clicked(self):
        if self.KingbaseLogical.isChecked():
            self.result.add("KingbaseLogical")
        else:
            self.result.remove("KingbaseLogical")
    def on_checkBox_tdsql_clicked(self):
        if self.TDSQL.isChecked():
            self.result.add("TDSQL")
        else:
            self.result.remove("TDSQL")
    def on_checkBox_dmlogic_clicked(self):
        if self.DMLogic.isChecked():
            self.result.add("DMLogic")
        else:
            self.result.remove("DMLogic")
    def on_checkBox_hcs_gaussdb_clicked(self):
        if self.HCS_GaussDB.isChecked():
            self.result.add("HCS_GaussDB")
        else:
            self.result.remove("HCS_GaussDB")
    def on_checkBox_uxdb_clicked(self):
        if self.UXDB.isChecked():
            self.result.add("UXDB")
        else:
            self.result.remove("UXDB")
    def on_checkBox_gaussdb_clicked(self):
        if self.GaussDB.isChecked():
            self.result.add("GaussDB")
        else:
            self.result.remove("GaussDB")
    def on_checkBox_mysqlphysical_clicked(self):
        if self.MySQLPhysical.isChecked():
            self.result.add("MySQLPhysical")
        else:
            self.result.remove("MySQLPhysical")
    def on_checkBox_oraclelogic_clicked(self):
        if self.OracleLogical.isChecked():
            self.result.add("OracleLogical")
        else:
            self.result.remove("OracleLogical")
    def on_checkBox_hana_clicked(self):
        if self.HANA.isChecked():
            self.result.add("HANA")
        else:
            self.result.remove("HANA")
    def on_checkBox_sequoiadb_clicked(self):
        if self.SequoiaDB.isChecked():
            self.result.add("SequoiaDB")
        else:
            self.result.remove("SequoiaDB")
    def on_checkBox_fusionSphere_clicked(self):
        if self.FusionSphere.isChecked():
            self.result.add("FusionSphere")
        else:
            self.result.remove("FusionSphere")
    def on_checkBox_hyper_clicked(self):
        if self.Hyper_V.isChecked():
            self.result.add("Hyper_V")
        else:
            self.result.remove("Hyper_V")
    def on_checkBox_h3c_clicked(self):
        if self.H3C.isChecked():
            self.result.add("H3C")
        else:
            self.result.remove("H3C")
    def on_checkBox_kubernetes_clicked(self):
        if self.Kubernetes.isChecked():
            self.result.add("Kubernetes")
        else:
            self.result.remove("Kubernetes")
    def on_checkBox_vmware_clicked(self):
        if self.VMware.isChecked():
            self.result.add("VMware")
        else:
            self.result.remove("VMware")
    def on_checkBox_cnware_clicked(self):
        if self.CNware.isChecked():
            self.result.add("CNware")
        else:
            self.result.remove("CNware")
    def on_checkBox_hcs_clicked(self):
        if self.HCS.isChecked():
            self.result.add("HCS")
        else:
            self.result.remove("HCS")
    def on_checkBox_sangfor_clicked(self):
        if self.SangFor.isChecked():
            self.result.add("SangFor")
        else:
            self.result.remove("SangFor")
    def on_checkBox_tencentcloud_clicked(self):
        if self.TencentCloud.isChecked():
            self.result.add("TencentCloud")
        else:
            self.result.remove("TencentCloud")
    def on_checkBox_cce_clicked(self):
        if self.CCE.isChecked():
            self.result.add("CCE")
        else:
            self.result.remove("CCE")
    def on_checkBox_ivs_clicked(self):
        if self.IVS.isChecked():
            self.result.add("IVS")
        else:
            self.result.remove("IVS")
    def on_checkBox_openstack_clicked(self):
        if self.OpenStack.isChecked():
            self.result.add("OpenStack")
        else:
            self.result.remove("OpenStack")
    def on_checkBox_commoncloud_clicked(self):
        if self.CommonCloud.isChecked():
            self.result.add("CommonCloud")
        else:
            self.result.remove("CommonCloud")
    def on_checkBox_zstack_clicked(self):
        if self.Zstack.isChecked():
            self.result.add("Zstack")
        else:
            self.result.remove("Zstack")
    def on_checkBox_easystack_clicked(self):
        if self.EasyStack.isChecked():
            self.result.add("EasyStack")
        else:
            self.result.remove("EasyStack")
    def on_checkBox_incloudsphere_clicked(self):
        if self.InCloudSphere.isChecked():
            self.result.add("InCloudSphere")
        else:
            self.result.remove("InCloudSphere")
    def on_checkBox_topsec_clicked(self):
        if self.TopSec.isChecked():
            self.result.add("TopSec")
        else:
            self.result.remove("TopSec")
    def on_checkBox_fusioninsight_clicked(self):
        if self.FusionInsight.isChecked():
            self.result.add("FusionInsight")
        else:
            self.result.remove("FusionInsight")
    def on_checkBox_tbase_clicked(self):
        if self.Tbase.isChecked():
            self.result.add("Tbase")
        else:
            self.result.remove("Tbase")

    def one_step_ViewAgent(self): ##一键查看代理信息
        username = self.input_username.text()           #获取界面输入的用户名
        password = self.input_password.text()           #获取界面输入的密码
        agent_ip = self.input_agentip.text()            #获取界面输入的代理IP

        # 创建SSH客户端实例
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if not agent_ip  :
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "代理IP为空，请输入")
            msg_box.exec_()
        else:
            ssh_client.connect(agent_ip, 22, username, password)
            print(f'{self.time}--SSH connection is successful')
            stdin, stdout, stderr = ssh_client.exec_command(f"ps -ef|grep java")
            print(stdout.read())
            ssh_client.close()

    def show_message_warning(self):
        QMessageBox.warning(self, "提示", "请输入IP")

    def show_message_critical(self):
        QMessageBox.critical(self, "错误", "系统错误")

    def one_step_DelAgent(self):  ##一键删除代理
        username = self.input_username.text()           #获取界面输入的用户名
        password = self.input_password.text()           #获取界面输入的密码
        agent_ip = self.input_agentip.text()            #获取界面输入的代理IP
        agent_path = self.input_path.text()             #获取界面输入的代理安装路径

        # 创建SSH客户端实例
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if  agent_path == ''or username == '':
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "代理IP或代理路径为空，请输入")
            msg_box.exec_()
        else:
            ssh_client.connect(agent_ip, 22, username, password)
            print(f'{self.time}SSH connection is successful')
            stdin, stdout, stderr = ssh_client.exec_command(f"cd {agent_path}/ubackup/uagent/bin;"
                                                            f"./uninstall.sh;"
                                                            f"ps -ef|grep java")
            print(stdout.read())
            ssh_client.close()
            print(f"{self.time}--代理卸载成功")

    def one_step_view_backupIP(self):
        username = self.input_username.text()           #获取界面输入的用户名
        password = self.input_password.text()           #获取界面输入的密码
        agent_ip = self.input_agentip.text()            #获取界面输入的代理IP
        agent_path = self.input_path.text()
        if  agent_path == ''or agent_ip == '' :
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "代理IP或路径为空，请输入")
            msg_box.exec_()
        else:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=agent_ip, username=username, password=password)
                # 执行Linux命令获取txt文件内容
                stdin, stdout, stderr = ssh.exec_command(f'cat {agent_path}/ubackup/uagent/conf/node.properties;')
                content = stdout.read().decode()
                pattern = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content)  # 第四段 0-255
                str_pattern = ''.join(pattern)
                if str_pattern == '':
                    # print("检查信息输入是否正确")
                    msg_box = QMessageBox(QMessageBox.Critical, "警告", "请检查代理IP或路径输入是否正确")
                    msg_box.exec_()
                else:
                    print(f'{self.time}--当前黑方IP是:%s'%(str_pattern))



    def one_step_change_backupIP(self):  #一键切换代理
        username = self.input_username.text()           #获取界面输入的用户名
        password = self.input_password.text()           #获取界面输入的密码
        agent_ip = self.input_agentip.text()            #获取界面输入的代理IP
        new_backup_ip = self.input_new_backupip.text()
        agent_path = self.input_path.text()
        port = 22
        source_name = f'{agent_path}/ubackup/uagent/conf/node.properties'
        target_name = r'D:\node.properties'

        print("开始修改")


        try:

            if agent_path == ''or username == '' or new_backup_ip == '':
                msg_box = QMessageBox(QMessageBox.Warning, "提示", "代理IP或路径为空或未输入切换后黑方IP，请输入")
                msg_box.exec_()
            else:
                # 类似于ssh+ftp命令
                # 建立与远程主机的通道
                tarnsport = paramiko.Transport((agent_ip, port))
                # 验证用户名和密码是否正确
                tarnsport.connect(username=username, password=password)
                # 根据创建并验证成功的通道
                sftp = paramiko.SFTPClient.from_transport(tarnsport)
                sftp.get(source_name, target_name)
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=agent_ip, username=username, password=password)
                # 执行Linux命令获取txt文件内容
                stdin, stdout, stderr = ssh.exec_command(f'cat {agent_path}/ubackup/uagent/conf/node.properties;')
                content = stdout.read().decode()
                # ssh.close()
                # print(content)
                # 使用正则表达式匹配需要的字段
                pattern = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content)  # 第四段 0-255
                print(pattern)
                str_pattern = ''.join(pattern)
                print(f'{self.time}--原黑方IP是:%s'%(str_pattern))
                f = open(target_name, "r")
                file_data = ''
                for line in f:
                    line = line.replace(str_pattern, new_backup_ip)
                    file_data += line
                f = open(target_name, "w")
                f.write(file_data)
                f.close()
                # 上传文件
                sftp.put(target_name, source_name)
                stdin, stdout, stderr = ssh.exec_command(f'cd {agent_path}/ubackup/uagent/bin && ./agent_stop.sh && ./agent_start.sh;')
                print(stdout.read())
                ssh.close()
                tarnsport.close()
                print(f"{self.time}--黑方IP切换成功！")
        except AuthenticationException as e:
            print('主机%s密码错误' ,e)
        except Exception as e:
            print( '未知错误：', e)


    def connectiontest(self):   # 为继承的ui文件中的按钮添加点击事件
        global username
        global password
        global agent_ip
        global jdk
        global version



        jdk = self.select_jdk.currentText()             #获取界面选择的jdk版本号
        version = self.banbenxuanze.currentText()       #获取界面选择的版本号6.8  6.9等
        cpu = self.cpu.currentText()                    #获取代理架构（ARM、X86）
        weishu = self.weishu1.currentText()             #获取代理位数（X64、X32）
        username = self.input_username.text()           #获取界面输入的用户名
        password = self.input_password.text()           #获取界面输入的密码
        agent_ip = self.input_agentip.text()            #获取界面输入的代理IP
        ubackup_port = self.input_port.text()           #获取界面输入的黑方端口号
        ubackup_ip = self.input_backupip.text()         #获取界面输入的黑方IP
        agent_path = self.input_path.text()             #获取界面输入的代理安装路径






        # 创建SSH客户端实例
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        zujian = '@'.join(self.result)



        if version == '6.8' :
        # 连接远程主机
        # 连接服务器
            version_list = ['agent_demestic_linux.tar','agent_linux_x32.tar','agent_linux_x64.tar']
            try:
                if agent_ip == '' or agent_path == '' or ubackup_ip == '':
                    msg_box = QMessageBox(QMessageBox.Warning, "提示", "代理IP或路径或黑方IP为空，请输入")
                    msg_box.exec_()
                else:
                    print(f"{self.time}开始进行代理一键安装")
                    ssh_client.connect(agent_ip, 22, username, password)
                    print(f'{self.time}SSH connection is successful')

                    stdin, stdout, stderr = ssh_client.exec_command(f"if [ ! -d {agent_path} ]; then mkdir -p {agent_path}; fi")
                    if stderr.read().decode():
                        print(f"创建路径{agent_path}失败")
                    else:
                        print(f"创建路径{agent_path}成功")

                    if cpu == 'ARM' :
                        Version = version_list[0]
                        print(Version)
                        print("我进入了arm代理")
                        print(f'{self.time}所选择的组件有{zujian}')
                        stdin, stdout, stderr = ssh_client.exec_command(
                                                                        f"cd {agent_path}; "
                                                                        f"wget {ubackup_ip}/download/install/linux/{Version} --no-check-certificate;"
                                                                        f"tar -xvf {Version};"
                                                                        f"cd agentsetup;"
                                                                        f"source /etc/profile;"
                                                                        f"./install.sh {agent_path} uagent@file@{zujian} {jdk} https://{ubackup_ip}:{ubackup_port} {agent_ip} {agent_path}/agentsetup;"
                                                                        f"ps -ef|grep java"
                                                                        )
                        current_path = stdout.read().decode().strip()
                        print(stdout.read())
                        print(current_path)
                        print(f"{self.time}--代理安装成功")
                        ssh_client.close()   #关闭连接
                    else:
                        if weishu == "X64" :
                            print("我是X86 64位")
                            Version = version_list[2]
                            print(Version)
                            stdin, stdout, stderr = ssh_client.exec_command(f"cd {agent_path}; "
                                                                            f"wget {ubackup_ip}/download/install/linux/{Version} --no-check-certificate;"
                                                                            f"tar -xvf {Version};"
                                                                            f"cd agentsetup;"
                                                                            f"source /etc/profile;"
                                                                            f"./install.sh {agent_path} uagent@file@{zujian} {jdk} https://{ubackup_ip}:{ubackup_port} {agent_ip} {agent_path}/agentsetup;"
                                                                            f"ps -ef|grep java")
                            current_path = stdout.read().decode().strip()
                            print(current_path)
                            print(stdout.read())
                            ssh_client.close()  # 关闭连接
                        else:
                            print("我是X86 32位")
                            Version = version_list[1]
                            stdin, stdout, stderr = ssh_client.exec_command(f"cd {agent_path}; "
                                                                            f"wget {ubackup_ip}/download/install/linux/{Version} --no-check-certificate;"
                                                                            f"tar -xvf {Version};"
                                                                            f"cd agentsetup;"
                                                                            f"source /etc/profile;"
                                                                            f"./install.sh {agent_path} uagent@file@{zujian} {jdk} https://{ubackup_ip}:{ubackup_port} {agent_ip} {agent_path}/agentsetup;"
                                                                            f"ps -ef|grep java")
                            current_path = stdout.read().decode().strip()
                            print(current_path)
                            print(stdout.read())
                            ssh_client.close()  # 关闭连接

            except paramiko.AuthenticationException as e:
                    print('Authentication failed:', e)
                    ssh_client.close()
                    # sys.exit()
            except Exception as e:
                    print('Error:', e)
                    ssh_client.close()

        else:
            msg_box = QMessageBox(QMessageBox.Warning, "提示", "功能暂未开放，敬请期待！")
            msg_box.exec_()






if __name__ == '__main__':
    app = QApplication(sys.argv)#创建应用程序对象
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
