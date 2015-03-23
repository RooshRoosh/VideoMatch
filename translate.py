#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint

__author__ = 'Ruslan Talipov'

from apiclient.discovery import build

try:
    from settings_api import DEVELOPER_KEY
except:
    DEVELOPER_KEY = '' # Устанавливаем свой ключ

def translate(russian_string):
  service = build(
      'translate',
      'v2',
      developerKey=DEVELOPER_KEY
  )
  translations = service.translations().list(
      source='ru',
      target='en',
      q=russian_string
  ).execute().get('translations',[])
  for item in translations:
      yield item['translatedText']



if __name__ == '__main__':
  pprint.pprint(translate('Как приготовить борщ спускаясь вниз?'))