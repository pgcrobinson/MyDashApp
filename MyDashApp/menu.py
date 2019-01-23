import dash_html_components as html
import dash_core_components as dcc


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/dash-vanguard-report/overview', className="tab first"),

        dcc.Link('Price Performance   ', href='/dash-vanguard-report/price-performance', className="tab"),

        dcc.Link('Portfolio & Management   ', href='/dash-vanguard-report/portfolio-management', className="tab"),

        dcc.Link('Fees & Minimums   ', href='/dash-vanguard-report/fees', className="tab"),

        dcc.Link('Distributions   ', href='/dash-vanguard-report/distributions', className="tab"),

        dcc.Link('News & Reviews   ', href='/dash-vanguard-report/news-and-reviews', className="tab")

    ], className="row ")
    return menu
