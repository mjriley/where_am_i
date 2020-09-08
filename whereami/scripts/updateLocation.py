#!/usr/bin/env python

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'dimagi_coding_exercise.settings')
django.setup()


def main():
    print('hello world!')


if __name__ == '__main__':
    main()
