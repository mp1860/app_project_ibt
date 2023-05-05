

from flask import Blueprint, request, render_template, redirect

from web_app.services.alpha import AlphavantageService


dashboard_routes = Blueprint("dashboard_routes", __name__)

@dashboard_routes.route("/crypto/form")
def crypto_form():
    return render_template("crypto_form.html")


@dashboard_routes.route("/crypto/dashboard", methods=["GET", "POST"])
def crypto_dashboard():
    print("CRYTPO DASHBOARD...")

    # if the form sends the data via POST request, we'll have request.form
    # otherwise if we specify url params in a GET request, we'll have request.args
    request_data = dict(request.form or request.args)
    print("REQUEST DATA:", request_data)

    symbol = request_data.get("symbol") or "MSFT"
    print("SYMBOL:", symbol)

    try:
        alpha = AlphavantageService()
        df = alpha.fetch_stocks_daily(symbol=symbol)
        if not df.empty:
            data = df.to_dict("records") # convert data to list of dictionaries (JSON stucture)
            return render_template("crypto_dashboard.html", symbol=symbol, data=data)
        else:
            #flash("OOPS", "warning")
            return redirect("/crypto/form")
    except Exception as err:
        print("ERROR", err)
        #flash("OOPS", "warning")
        return redirect("/crypto/form")
