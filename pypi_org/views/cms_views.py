import flask
from pypi_org.services.cms_service import get_page

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')


@blueprint.route('/<path:full_url>')
def cms_page(full_url: str):
    print("Getting CMS page for {}".format(full_url))

    page = get_page(full_url)
    if not page:
        flask.abort(404)

    return flask.render_template('cms/page.html', page=page)
