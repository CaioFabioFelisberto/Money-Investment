from flask import Flask, render_template, request
from funcs import selic_plot, plot_heritage_composition, plot_savings_composition

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/accumulated_vs_inflation', methods=['GET','POST'])
def accumulated_vs_inflation():
    if request.method == 'POST':
        monthly_cont = request.form.get('amount')
        time = request.form.get('months')

        plot = selic_plot(monthly_cont,time)

        return render_template('accumulated.html', plot=plot)
    return render_template('accumulated.html')

@app.route('/heritage_composition', methods=['GET','POST'])
def heritage_composition():
    if request.method == 'POST':
        monthly_cont = request.form.get('amount')
        time = request.form.get('months')

        plot = plot_heritage_composition(monthly_cont,time)

        return render_template('heritage.html', plot=plot)
    return render_template('heritage.html')

@app.route('/savings', methods=['GET','POST'])
def savings():
    if request.method == 'POST':
        monthly_cont = request.form.get('amount')
        time = request.form.get('months')

        plot = plot_savings_composition(monthly_cont,time)

        return render_template('savings.html', plot=plot)
    return render_template('savings.html')

if __name__ == '__main__':
    app.run(debug=True)