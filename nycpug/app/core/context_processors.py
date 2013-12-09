from nycpug.app.core.models import Conference

def sponsors(request):
    """returns grouped list of all core.Sponsor objects, grouped by sponsor.Category"""
    try:
        conference = Conference.objects.filter(active=True).order_by('start_date').all()[0]
        sponsors = []
        for category in conference.sponsor_categories.all():
            sponsors.append({
                'category': category.name,
                'sponsors': [sponsor for sponsor in conference.sponsors.filter(category=category).all()]
            })
    except IndexError:
        return {}
    return { 'sponsors': sponsors }
