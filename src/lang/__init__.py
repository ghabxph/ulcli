def init(lang):
    return getattr(__import__('lang.%s' % lang), lang)
