from flask import Flask, render_template, request
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

app = Flask(__name__)

# Function Helper: Logika Fuzzy
def hitung_fuzzy(clock_val, ram_val, heat_val):
    # Deklarasi Variabel
    clock = ctrl.Antecedent(np.arange(1.0, 4.1, 0.1), 'clock')
    ram = ctrl.Antecedent(np.arange(2, 19, 1), 'ram')
    heat = ctrl.Antecedent(np.arange(1, 11, 1), 'heat')
    index = ctrl.Consequent(np.arange(0, 101, 1), 'index')

    # Pembuatan 3 Himpunan
    clock['Rendah'] = fuzz.trimf(clock.universe, [1.0, 1.0, 2.2])
    clock['Sedang'] = fuzz.trimf(clock.universe, [1.8, 2.5, 3.2])
    clock['Tinggi'] = fuzz.trimf(clock.universe, [2.8, 4.0, 4.0])

    ram['Kecil'] = fuzz.trimf(ram.universe, [2, 2, 6])
    ram['Menengah'] = fuzz.trimf(ram.universe, [4, 8, 12])
    ram['Besar'] = fuzz.trimf(ram.universe, [10, 18, 18])

    heat['Buruk'] = fuzz.trimf(heat.universe, [1, 1, 4])
    heat['Normal'] = fuzz.trimf(heat.universe, [3, 5, 7])
    heat['Bagus'] = fuzz.trimf(heat.universe, [6, 10, 10])

    index['Tidak Layak'] = fuzz.trapmf(index.universe, [0, 0, 30, 50])
    index['Cukup Layak'] = fuzz.trimf(index.universe, [40, 60, 80])
    index['Sangat Layak'] = fuzz.trapmf(index.universe, [70, 85, 100, 100])

    # Rule Base
    rule1 = ctrl.Rule(clock['Rendah'] | ram['Kecil'] | heat['Buruk'], index['Tidak Layak'])
    rule2 = ctrl.Rule(clock['Sedang'] & ram['Menengah'] & heat['Normal'], index['Cukup Layak'])
    rule3 = ctrl.Rule(clock['Tinggi'] & ram['Besar'] & heat['Bagus'], index['Sangat Layak'])
    rule4 = ctrl.Rule(clock['Tinggi'] & ram['Kecil'], index['Cukup Layak'])
    rule5 = ctrl.Rule(clock['Sedang'] & heat['Bagus'], index['Sangat Layak'])
    
    indexing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    indexing = ctrl.ControlSystemSimulation(indexing_ctrl)

    # Input Nilai
    indexing.input['clock'] = float(clock_val)
    indexing.input['ram'] = float(ram_val)
    indexing.input['heat'] = float(heat_val)
    indexing.compute()
    
    skor = round(indexing.output['index'], 2)
    
    # Hasil Labeling
    if skor < 45:
        label = "Tidak Layak untuk Heavy Gaming"
    elif skor < 75:
        label = "Cukup Layak (Gunakan Setting Medium)"
    else:
        label = "Sangat Layak (Rata Kanan/High)"
        
    return skor, label

# Function Helper: Logika Pakar
def hitung_pakar(g1, g2, g3, g4, g5, g6, g7, g8):
    hasil_diagnosa = []
    if g5 and g8:
        hasil_diagnosa.append({
            "masalah": "Storage & Memory Swap Bottleneck",
            "solusi": "Hapus file besar (video/game lain) hingga tersisa minimal 15% ruang kosong."
        })
    if g2 and g6:
        hasil_diagnosa.append({
            "masalah": "Severe Battery Degradation & Thermal Issue",
            "solusi": "Segera ganti baterai dan hindari bermain sambil di-charge."
        })
    if g1 and g7 and g4:
        hasil_diagnosa.append({
            "masalah": "CPU/GPU Extreme Overload",
            "solusi": "Turunkan resolusi game ke rata kiri (Lowest), matikan anti-aliasing."
        })
    if (g1 and g2) and not (g2 and g6):
        hasil_diagnosa.append({
            "masalah": "Standard Thermal Throttling",
            "solusi": "Pasang Cooler Fan eksternal atau bermain di ruangan ber-AC."
        })
    if g3:
        hasil_diagnosa.append({
            "masalah": "Network Instability / Packet Loss",
            "solusi": "Switch jaringan ke Wi-Fi 5G, matikan VPN, atau gunakan fitur Game Booster."
        })
    if (g1 or g4) and len(hasil_diagnosa) == 0:
        hasil_diagnosa.append({
            "masalah": "Penurunan Performa General",
            "solusi": "Terjadi antrean proses di RAM. Coba bersihkan cache sistem atau restart perangkat."
        })
    if not hasil_diagnosa:
        hasil_diagnosa.append({
            "masalah": "Kondisi Normal",
            "solusi": "Tidak ada anomali terdeteksi. Pastikan perangkat Anda selalu update software."
        })

    return hasil_diagnosa
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fuzzy', methods=['GET', 'POST'])
def fuzzy():
    skor = None
    label = None
    if request.method == 'POST':
        clock = request.form['clock']
        ram = request.form['ram']
        heat = request.form['heat']
        try:
            skor, label = hitung_fuzzy(clock, ram, heat)
        except Exception as e:
            label = "Error pada komputasi Fuzzy. Pastikan input valid."
    return render_template('fuzzy.html', skor=skor, label=label)

@app.route('/pakar', methods=['GET', 'POST'])
def pakar():
    hasil_pakar = None
    if request.method == 'POST':
        # Mengambil data checklist
        g1 = 'g1' in request.form
        g2 = 'g2' in request.form
        g3 = 'g3' in request.form
        g4 = 'g4' in request.form
        g5 = 'g5' in request.form
        g6 = 'g6' in request.form
        g7 = 'g7' in request.form
        g8 = 'g8' in request.form
        
        # Mengeksekusi mesin inferensi
        hasil_pakar = hitung_pakar(g1, g2, g3, g4, g5, g6, g7, g8)   
    return render_template('pakar.html', hasil_pakar=hasil_pakar)

if __name__ == '__main__':
    app.run(debug=True)
