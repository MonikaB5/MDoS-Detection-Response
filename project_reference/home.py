from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def dashboard():
    system_status = "Normal"
    memory_usage = 85
    alarm_triggered = memory_usage > 80
    return render_template('dashboard.html',
                           system_status=system_status,
                           memory_usage=memory_usage,
                           alarm_triggered=alarm_triggered)

@app.route('/simulate_attack')
def simulate_attack():
    # Here you can run your stress command or just simulate
    print("⚠️ Simulating attack... High memory load triggered!")
    return redirect(url_for('dashboard'))

@app.route('/initiate_defence')
def initiate_defence():
    # Here you can call AWS Lambda or stop EC2 instance
    print("🛡️ Defence initiated... EC2 stopped and logs saved!")
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
