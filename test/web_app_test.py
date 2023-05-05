from conftest import parse_page

#
# TESTING HOME ROUTES
#

def test_home(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert "Welcome Home" in response.text

def test_overview(test_client):
    response = test_client.get("/overview")
    assert response.status_code == 200
    assert "Overview" in response.text

def test_history(test_client):

    # default:
    response = test_client.get("/history")
    assert response.status_code == 200
    page = parse_page(response.data)
    assert "History" in response.text

    # with custom parameter:
    response = test_client.get("/history?name=Jon%20Snow")
    assert response.status_code == 200
    assert "Hello, Jon Snow" in response.text


#
# TESTING DASHBOARD ROUTES
#


def test_stocks_form(test_client):
    response = test_client.get("/crypto/form")
    assert response.status_code == 200
    page = parse_page(response.data)
    assert page.find("h2").text == "Crypto Form"


def test_stocks_dashboard(test_client):

    # GET request uses MSFT by default:
    response = test_client.get("/crypto/dashboard")
    assert response.status_code == 200
    page = parse_page(response.data)
    assert page.find("h2").text == "Crypto Dashboard"
    assert page.find("span", id="display-symbol").text == "MSFT"

    # GET request with custom param:
    response = test_client.get("/crypto/dashboard?symbol=GOOGL")
    assert response.status_code == 200
    page = parse_page(response.data)
    assert page.find("h2").text == "Crypto Dashboard"
    assert page.find("span", id="display-symbol").text == "GOOGL"

    # POST request with custom param:

    response = test_client.post("/crypto/dashboard", data={"symbol": "GOOGL"})
    assert response.status_code == 200
    page = parse_page(response.data)
    assert page.find("h2").text == "Crypto Dashboard"
    assert page.find("span", id="display-symbol").text == "GOOGL"
