# -*- coding: utf-8 -*-
from app import db, get_locale
from app.main import bp
from app.setting_parse import setting_write
from flask import flash, request, redirect, url_for, session
from flask_login import current_user, login_required
from flask import render_template
from app.main.forms import EditProfileForm, IndexForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.xml_parser import xml_parser_read, xml_parser_write
from flask_babel import Babel, lazy_gettext as _l, _


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = IndexForm()
    CID_path = '/home/work/HDD2/sftp/Flask_orion/KALINA.CID'
    bin_path = '/home/work/PycharmProjects/Settings_read/settings.kprm61850'
    # CID_path = '/files_61850/KALINA.CID'
    # bin_path = '/kepm/settings.kprm61850'

    if form.validate_on_submit():
        ip = form.ip.data
        mask = form.mask.data
        gate = form.gate.data
        ied = form.ied.data
        xml_parser_write(ip=ip, mask=mask, gate=gate, path=CID_path, ied=ied)
        setting_write(ip=ip, mask=mask, gate=gate, path=bin_path)
    elif request.method == 'GET':
        ip, mask, gate, ied = xml_parser_read(path=CID_path)
        form.ip.data = ip
        form.mask.data = mask
        form.gate.data = gate
        form.ied.data = ied

    return render_template('index.html', title=_('Home Page'), form=form)



# @bp.route('/<active_language>/account_settings', methods=['GET', 'POST'])
@bp.route('/account_settings', methods=['GET', 'POST'])
@login_required
def account_settings():
    form = EditProfileForm(current_user.username)
    languages = ['uk', 'ru', 'en']

    select = request.form.get("languages")
    form.username.data = current_user.username
    if select == None:
        active_language = languages[0]
        if form.validate_on_submit():
            if form.username.data != None:
                current_user.username = form.username.data
            if form.password.data != None:
                current_user.password_hash = generate_password_hash(form.password.data)
                print(current_user.password_hash)
            db.session.commit()
            flash(_('Your changes have been saved.'))
            return redirect(url_for('main.account_settings'))
    else:
        print(languages.index(select))
        active_language = languages[languages.index(select)]
        # print(session['lang'])
        session['lang'] = active_language
        # form.password.data = current_user.password_hash
        # pbkdf2:sha256:260000$EkCXwYeTYP39AJay$7084d46648ca80703fb6e87ca59378d9ccc4a57fcdd4db972d42b310de9df0bf
    return render_template('account_settings.html',
                           title=_('Account settings'),
                           form=form,
                           languages=languages,
                           active_language=active_language)
