
from PyQt5 import QtCore, QtWidgets
from configurator import Ui_configurator
import generator as gen
import numpy as np


class ShipHolderApplication(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ShipHolderApplication, self).__init__(parent)
        self.createWidgets()
        self.connectActions()

    def createWidgets(self):
        self.ui = Ui_configurator()
        self.ui.setupUi(self)
		
    def connectActions(self):
        self.ui.generate_buttom.clicked.connect(self.generate_click)
        self.ui.actionAbout.triggered.connect(self.about_click)
        self.ui.actionSave.triggered.connect(self.save_click)
        self.ui.actionLoad.triggered.connect(self.load_click)
        self.ui.path_button.clicked.connect(self.path_click)


    def generate_click(self):
        

        var = self.call_var(self)
        temp_path = "config_file_temp.conf"
        self.create_conf_file(temp_path,var)
        gen.test_config(temp_path)

    def path_click(self):
        self.PathName = QtWidgets.QFileDialog.getSaveFileName( self, 
			"Define Save File for OnStep Conf", QtCore.QDir.homePath(), 
			"text File (*.txt)")
        self.ui.path_line.setText(self.PathName[0])
        print(self.PathName[0])

    def about_click(self):
        QtWidgets.QMessageBox.about(self,'About',"Onstep configurator GUI\n about sebastien Durand")
        
    def call_var(self):
                # General ____________________________________________
        mount_type = self.ui.mount_combo.currentText()
        board_type = self.ui.board_combo.currentText()
        max_rate = self.ui.maxrate_spin.value()
        pec_spin = self.ui.pec_spin.value()
        auto_sid = self.ui.auto_side_combo.currentText()

        worm1 = self.ui.axis1_worm_spindouble.value()
        gear1 = self.ui.axis1_gear_spindouble.value()
        stepper1 = self.ui.axis1_motor_combo.currentText()
        micro1 = self.ui.axis1_micro_combo.currentText()
        slew1 = self.ui.axis1_mod_combo.currentText()
        driver1 = self.ui.axis1_driver_combo.currentText()
        reverse1 = self.ui.axis1_reverse_checkBox.isChecked()
        ena1 = self.ui.axis1_enable_comboBox.currentText()
        fault1 = self.ui.axis1_fault_comboBox.currentText()
        
        worm2 = self.ui.axis2_worm_spindouble.value()
        gear2 = self.ui.axis2_gear_spindouble.value()
        stepper2 = self.ui.axis2_motor_combo.currentText()
        micro2 = self.ui.axis2_micro_combo.currentText()
        slew2 = self.ui.axis2_mod_combo.currentText()
        driver2 = self.ui.axis2_driver_combo.currentText()
        reverse2 = self.ui.axis2_reverse_checkBox.isChecked()
        ena2 = self.ui.axis2_enable_comboBox.currentText()
        fault2 = self.ui.axis2_fault_comboBox.currentText()
        
        # Axis3/2 ____________________________________________
        rot3 = self.ui.rot_checkBox.isChecked()
        foc1 = self.ui.focus1_checkBox.isChecked()
        foc2 = self.ui.focus2_checkBox.isChecked()
        
        rot_rate = self.ui.rot_mrate_spinBox.value()
        rot_step = self.ui.rot_step_comboBox.currentText()
        rot_micro = self.ui.rot_mode_comboBox.currentText()
        rot_gear = self.ui.rot_gear1_doubleSpinBox.value()
        rot_gear_2 = self.ui.rot_gear2_doubleSpinBox.value()
        rot_reverse = self.ui.rot_reverse_checkBox.isChecked()
        rot_min_degr = self.ui.rot_min_angle_doubleSpinBox.value()
        rot_max_degr = self.ui.rot_max_angle_doubleSpinBox.value()
        
        foc1_rate = self.ui.focus1_mrate_spinBox.value()
        foc1_ratio = self.ui.focus1_micro_doubleSpinBox.value()
        foc1_reverse = self.ui.focus1_reverse_checkBox.isChecked()
        foc1_min_mm = self.ui.focus1_min_mil_doubleSpinBox.value()
        foc1_max_mm = self.ui.focus1_max_mil_doubleSpinBox.value()
        
        foc2_rate = self.ui.focus2_mrate_spinBox.value()
        foc2_ratio = self.ui.focus2_micro_doubleSpinBox.value()
        foc2_reverse = self.ui.focus2_reverse_checkBox.isChecked()
        foc2_min_mm = self.ui.focus2_min_mil_doubleSpinBox.value()
        foc2_max_mm = self.ui.focus2_max_mil_doubleSpinBox.value()
        
        # option ____________________________________________
        baud = self.ui.serial_baud_comboBox.currentText()
        
        pec = self.ui.pec_checkBox.isChecked()
        pec_buffer = self.ui.pec_buffer_spin.value()
        pec_set = self.ui.pec_set_checkBox.isChecked()
        analog_pec = self.ui.analog_pec_spinBox.value()
        pec_logic = self.ui.pec_logic_comboBox.currentText()
        
        goto_assist = self.ui.goto_assist_checkBox.isChecked()
        
        strict_park = self.ui.strict_checkBox.isChecked()
        
        st4 = self.ui.st4_checkBox.isChecked()
        alt_st4 = self.ui.alternative_st4_checkBox.isChecked()
        hand = self.ui.hand_checkBox.isChecked()
        
        pulse = self.ui.separate_pulse_checkBox.isChecked()
        
        guide_time = self.ui.guide_time_spinBox.value()
        
        rtc = self.ui.rtc_checkBox.isChecked()
        rtc_time = self.ui.rtc_time_comboBox.currentText()
        
        pps = self.ui.pps_checkBox.isChecked()
        
        limit = self.ui.limit_checkBox.isChecked()
        
        led1 = self.ui.led_state_checkBox.isChecked()
        reticule = self.ui.reticule_checkBox.isChecked()
        led_intensity = self.ui.intensity_led_spinBox.value()
        
        led2 = self.ui.state_led2_checkBox.isChecked()
        
        buzzer = self.ui.buzzer_checkBox.isChecked()
        freq_sound = self.ui.freq_spinBox.value()
        def_sound = self.ui.default_sound_checkBox.isChecked()
        
        atmos = self.ui.atmos_checkBox.isChecked()
        
        home_pause = self.ui.home_pause_checkBox.isChecked()
        
        max_rate = self.ui.max_rate_save_checkBox.isChecked()
        
        accel = self.ui.degre_accel_doubleSpinBox.value()
        
        rapid_stop = self.ui.degre_rapid_stop_doubleSpinBox.value()
        
        backlash = self.ui.backlash_rate_spinBox.value()
        
        off_axis = self.ui.off_axis_checkBox.isChecked()
        
        degre_e = self.ui.degre_e_spinBox.value()
        degre_w = self.ui.degre_w_spinBox.value()
        
        min_dec = self.ui.min_dec_spinBox.value()
        max_dec = self.ui.max_dec_spinBox.value()
        
        pol_limit = self.ui.pol_limit_spinBox.value()
        
        max_az = self.ui.max_az_spinBox.value()
    
        
        #________________________________________________________________
        
        var = [mount_type, board_type, max_rate, pec_spin, auto_sid, worm1, 
               gear1, stepper1, micro1, slew1, driver1, reverse1, ena1, fault1,
               worm2, gear2, stepper2, micro2, slew2, driver2, reverse2, ena2,
               fault2, rot3, foc1, foc2, rot_rate, rot_step, rot_micro, 
               rot_gear, rot_gear_2, rot_reverse, rot_min_degr, rot_max_degr,
               foc1_rate, foc1_ratio, foc1_reverse, foc1_min_mm, foc1_max_mm,
               foc2_rate, foc2_ratio, foc2_reverse, foc2_min_mm, foc2_max_mm, 
               baud, pec, pec_buffer, pec_set, analog_pec, pec_logic, 
               goto_assist, strict_park, st4, alt_st4, hand, pulse, guide_time,
               rtc, rtc_time, pps, limit, led1, reticule, led_intensity, led2,
               buzzer, freq_sound, def_sound, atmos, home_pause, max_rate, 
               accel, rapid_stop, backlash, off_axis, degre_e, degre_w, 
               min_dec, max_dec, pol_limit, max_az]
        
        return var
    
    def save_click(self):
        self.SaveName = QtWidgets.QFileDialog.getSaveFileName( self, 
			"Definir nom de sauvegarde", QtCore.QDir.homePath(), 
			"Fichiers texte (*.txt)")
        print(self.SaveName[0])
        var = self.call_var()
        self.create_conf_file(self.SaveName[0],var)

    def load_click(self):
        self.LoadName = QtWidgets.QFileDialog.getOpenFileName( self, 
			"Ouvrir un fichier monture", QtCore.QDir.homePath())
        print(self.LoadName[0])
        self.read_conf_file(self.LoadName[0])
        
    def create_conf_file(self,path_name,var):
        
        file = open(path_name,'w')
        
        for i in range(len(var)):
            file.write(var[i])
            
        file.close()
        
        
    def read_conf_file(self,path_name):
        file = open(path_name,'r')
        
        text = file.readlines()
        text = np.array(text)
        for i in range(text.size) : text[i]=text[i].strip()
        # Convertion des variables (float32, int32, bool)
        #text[[1,2,3]] = np.float32(text[[1,2,3]])
        
        
        file.close()
        
        return var
    
    def main(self):
        self.show()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	#conf = QtWidgets.QMainWindow()
	myapp = ShipHolderApplication()
	myapp.main()
	#QTimer.singleShot(1,myapp.createWidgets())
	sys.exit(app.exec_())

