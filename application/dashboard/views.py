from flask import render_template
from flask_login import current_user, login_required
from flask import Blueprint


dashboard_bp = Blueprint('dashboard_bp',
                         __name__,
                         template_folder="templates",
                         static_folder="static",
                         url_prefix="/dashboard")


@dashboard_bp.route("/", methods=["GET"])
@login_required
def home():
    """Return the homepage."""
    return render_template("dashboard_home.html", current_user=current_user)
