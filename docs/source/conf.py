import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = 'opensource_programming'
copyright = '2026, maeng'
author = 'maeng'


extensions = [
    'sphinx.ext.autodoc',      # 코드 자동 분석
    'sphinx.ext.napoleon',    # Google 스타일 docstring 해석
    'sphinx.ext.viewcode'     # 소스코드 보기 추가 (선택)
]

templates_path = ['_templates']
exclude_patterns = []



html_theme = 'alabaster'
html_static_path = ['_static']
