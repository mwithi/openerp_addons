{
    'name': 'One2Many Limit Enabler',
    'category': 'Tools',
    'version': '0.1',
    'description':
        """
One2Many limit enabler.
=======================

This module enables 'limit' attribute on one2many fields in order to set the pagination limit.

Example:

<field name="MyOne2ManyField" limit="2000">
        """,
    'author': 'Alessandro Domanico (alessandro.domanico@informaticisenzafrontiere.org)',
    'website': 'www.informaticisenzafrontiere.org',
    'license': 'AGPL-3',
    'depends': ['web'],
    'js' : [
        "static/src/js/view_form.js",
    ],
    'installable' : True,
}
