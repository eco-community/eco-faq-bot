#! /bin/bash

pygettext -d base -o locales/base.pot bot.py

msgmerge locales/ru/LC_MESSAGES/base.po locales/base.pot -U --no-fuzzy-matching
msgmerge locales/en/LC_MESSAGES/base.po locales/base.pot -U --no-fuzzy-matching
msgmerge locales/fr/LC_MESSAGES/base.po locales/base.pot -U --no-fuzzy-matching
msgmerge locales/kr/LC_MESSAGES/base.po locales/base.pot -U --no-fuzzy-matching
msgmerge locales/jp/LC_MESSAGES/base.po locales/base.pot -U --no-fuzzy-matching

msgfmt locales/ru/LC_MESSAGES/base.po -o locales/ru/LC_MESSAGES/base.mo
msgfmt locales/en/LC_MESSAGES/base.po -o locales/en/LC_MESSAGES/base.mo
msgfmt locales/fr/LC_MESSAGES/base.po -o locales/fr/LC_MESSAGES/base.mo
msgfmt locales/kr/LC_MESSAGES/base.po -o locales/kr/LC_MESSAGES/base.mo
msgfmt locales/jp/LC_MESSAGES/base.po -o locales/jp/LC_MESSAGES/base.mo