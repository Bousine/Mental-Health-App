from flask import render_template, request
from flask_login import login_required, current_user
from app import db
from app.activities import bp


@bp.route('/exercises')
@login_required
def exercises():
    return render_template('activities/exercises.html', title='Exercises', user=current_user, points=current_user.points)


@bp.route('/activity4')
@login_required
def activity4():
    return render_template('activities/activity4.html', title='Activity 4', user=current_user, points=current_user.points)


@bp.route('/activity6')
@login_required
def activity6():
    return render_template('activities/activity6.html', title='Activity 6', user=current_user, points=current_user.points)


@bp.route('/activity101')
@login_required
def activity101():
    return render_template('activities/activity101.html', title='Activity 1', user=current_user, points=current_user.points)


@bp.route('/activity2')
@login_required
def activity2():
    return render_template('activities/activity2.html', title='Activity 2', user=current_user, points=current_user.points)


@bp.route('/activity2_classical')
@login_required
def activity2_classical():
    return render_template('activities/activity2_classical.html', title='Classical Music', user=current_user,
                           points=current_user.points)


@bp.route('/activity2_stringed')
@login_required
def activity2_stringed():
    return render_template('activities/activity2_stringed.html', title='String Music', user=current_user,
                           points=current_user.points)


@bp.route('/activity2_piano')
@login_required
def activity2_piano():
    return render_template('activities/activity2_piano.html', title='Music: Piano', user=current_user, points=current_user.points)


@bp.route('/activity2_wind')
@login_required
def activity2_wind():
    return render_template('activities/activity2_wind.html', title='Wind Music', user=current_user, points=current_user.points)


@bp.route('/activity2_natural')
@login_required
def activity2_natural():
    return render_template('activities/activity2_natural.html', title='Natural Sound', user=current_user,
                           points=current_user.points)


@bp.route('/activity2_popular')
@login_required
def activity2_popular():
    return render_template('activities/activity2_popular.html', title='Popular Music', user=current_user,
                           points=current_user.points)


@bp.route('/activity5')
@login_required
def activity5():
    return render_template('activities/activity5.html', title='Activity 5', user=current_user, points=current_user.points)


@bp.route('/activity1')
@login_required
def activity1():
    return render_template('activities/activity1.html', title='Activity 1', user=current_user, points=current_user.points)


# @bp.route('/activity4')
# @login_required
# def activity4():
#     return render_template('activities/activity4.html', title='Activity 4')


# @bp.route('/activity6')
# @login_required
# def activity6():
#     return render_template('activities/activity6.html', title='Activity 6')
