#!/usr/bin/env python3
"""Publish the committed static site; credentials stay in process memory."""
import argparse, base64, json, os, shlex, subprocess, sys, urllib.error, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REPO = 'gradinnovate-capstone/115-project'
p = argparse.ArgumentParser()
p.add_argument('--token-file', type=Path, required=True, help='Local env file containing one PAT/token')
a = p.parse_args()
values = {}
for raw in a.token_file.expanduser().read_text().splitlines():
    line = raw.strip()
    if line and not line.startswith('#') and '=' in line:
        key, value = line.removeprefix('export ').split('=', 1)
        parts = shlex.split(value, comments=True)
        if parts: values[key.strip()] = parts[0]
tokens = [v for k, v in values.items() if 'TOKEN' in k.upper() or 'PAT' in k.upper()]
if len(tokens) != 1: sys.exit('Expected exactly one PAT/token entry.')
token = tokens[0]
def api(path, method='GET', data=None):
    req = urllib.request.Request('https://api.github.com' + path,
        headers={'Authorization': 'Bearer ' + token, 'User-Agent': '115-project-publisher',
                 'Accept': 'application/vnd.github+json', 'Content-Type': 'application/json'},
        data=None if data is None else json.dumps(data).encode(), method=method)
    with urllib.request.urlopen(req, timeout=30) as response:
        body = response.read()
        return json.loads(body) if body else {}
def git(*args, env=None):
    result = subprocess.run(['git', *args], cwd=ROOT, env=env, capture_output=True, text=True)
    if result.returncode:
        sys.exit((result.stderr or result.stdout).replace(token, '[REDACTED]'))
    return result.stdout.strip()
try:
    # Verify org policy first; a hidden repo can otherwise also return 404.
    api('/orgs/gradinnovate-capstone/repos?per_page=1')
    try: repo = api('/repos/' + REPO)
    except urllib.error.HTTPError as exc:
        if exc.code != 404: raise
        repo = api('/orgs/gradinnovate-capstone/repos', 'POST', {
            'name':'115-project', 'description':'115 學年度 AI 專題學習資料與實作指南',
            'private':False, 'auto_init':False})
    if git('status', '--porcelain'): sys.exit('Commit local changes before publishing.')
    git('rev-parse', '--verify', 'HEAD')
    remote = 'https://github.com/' + REPO + '.git'
    if 'origin' not in git('remote').splitlines(): git('remote', 'add', 'origin', remote)
    elif git('remote', 'get-url', 'origin') != remote: sys.exit('origin differs from intended repository.')
    encoded = base64.b64encode(('x-access-token:' + token).encode()).decode()
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GIT_CONFIG_COUNT='1',
        GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
        GIT_CONFIG_VALUE_0='Authorization: Basic ' + encoded)
    # Normal push only: never overwrite divergent remote history.
    git('push', '-u', 'origin', 'HEAD:main', env=env)
    try: page = api('/repos/' + REPO + '/pages')
    except urllib.error.HTTPError as exc:
        if exc.code != 404: raise
        page = api('/repos/' + REPO + '/pages', 'POST', {'source':{'branch':'main','path':'/docs'},'build_type':'legacy'})
    else:
        source = page.get('source', {})
        if source.get('branch') != 'main' or source.get('path') != '/docs' or page.get('build_type') != 'legacy':
            api('/repos/' + REPO + '/pages', 'PUT', {'source':{'branch':'main','path':'/docs'},'build_type':'legacy'})
    print(json.dumps({'repository':repo['html_url'], 'pages':page.get('html_url'),
                      'status':'Source pushed and Pages configured; check build status before claiming deployed.'}, ensure_ascii=False))
except urllib.error.HTTPError as exc:
    print(f'GitHub HTTP {exc.code}: ' + exc.read().decode().replace(token, '[REDACTED]'), file=sys.stderr)
    sys.exit(1)
